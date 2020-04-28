import random
from enum import Enum
from blockchain import Blockchain, Block
from typing import List
from raft_events import *
from Logger import LoggerAux


# Nodes for the topology
class State(Enum):
    idle = 1
    busy = 2
    proposing = 3
    waiting = 4


class Node:

    def __init__(self, neighbors: List[object], topology=None, id=None):
        self.id = id
        self.topology = topology
        self.blockchain = Blockchain()
        self.blockchain.genesis()
        self.neighbors = neighbors
        self.candidates = []
        self.state = State.idle
        self.callbacks = {"eventShowNeighbors": self.event_print_neighbors,
                          "eventGenerateBlock": self.event_propose_block}

    def complete_neighborhood(self):
        for neighbor in self.neighbors:
            for candidate in neighbor.neighbors:
                if candidate != self and candidate not in self.neighbors and candidate not in self.candidates:
                    self.candidates.append(candidate)

    def event_print_neighbors(self):
        print("Node ID {}, neighbors = {}".format(self.ID, self.neighbors))

    def event_propose_block(self):
        pass

    def get_dict(self):
        data = self.__dict__
        return data

    def __str__(self):
        return "Node: {}\nNeighbors: {}\nCandidates: {}".format(self.id, [n.id for n in self.neighbors],
                                                                [c.id for c in self.candidates])


class RaftNode:
    votes = []
    current_proposal = None
    voting_timeout = -1

    def __init__(self, node_id: int, is_faulty: bool, neighbors: List[object], logger: LoggerAux):
        self.id = node_id
        self.neighbors = neighbors
        self.logger = logger
        self.blockchain = Blockchain()
        self.blockchain.genesis()
        self.is_leader = False
        self.state = State.idle
        self.is_faulty = is_faulty
        self.callbacks = {"propose_block": self.propose_block,
                          "validate_block": self.validate_block,
                          "receive_response": self.receive_response,
                          "append_block": self.append_block}

    def propose_block(self, params):
        '''
           params[0] --> timestamp
           params[1] --> target node
       '''

        if not self.is_leader:
            return
        self.votes = []
        self.voting_timeout = params[0] + 300
        self.current_proposal = Block(self.blockchain.last_block, self.id, params[0])
        if self.is_faulty:
            self.current_proposal.is_correct = False
        validate_events = []
        for neighbor in self.neighbors:
            resp_params = [params[0] + random.randint(10, 100), neighbor, self.current_proposal, self]
            validate_events.append(EventRaftValidateBlock(resp_params))
        self.logger.create_log("{} - Node {} Proposed block".format(params[0], self.id))
        return validate_events

    def validate_block(self, params):
        '''
                params[0] --> timestamp
                params[1] --> target node
                params[2] --> block
                params[3] --> proposer
        '''
        if params[2].hash == self.blockchain.last_block.hash:
            return

        if (params[2].is_correct and not self.is_faulty) or (not params[2].is_correct and self.is_faulty):
            self.logger.create_log(
                "{} - Node {} validated block {}".format(params[0], self.id, params[2].hash))
            return [EventRaftAppendBlock([params[0], self, params[2]]),
                    EventRaftReceiveResponse([params[0] + random.randint(10, 100), params[3], self, True, params[2]])]

    def receive_response(self, params):
        '''
                params[0] --> timestamp
                params[1] --> target node
                params[2] -->proposer
                params[3] --> response
                params[4] --> block
        '''
        returned_events = []

        if not self.is_leader:
            return

        self.logger.create_log(
            "{} - Node {} received response from node {}".format(params[0], self.id, params[2].id))

        if params[4].hash == self.current_proposal.hash:
            self.votes.append(params[1])
            if self.voting_timeout <= params[0]:
                returned_events.append(EventRaftProposeBlock([params[0], self]))

        if len(self.votes) > int(round(len(self.neighbors) / 2)) and \
                self.blockchain.last_block.hash != self.current_proposal.hash:
            returned_events.append(EventRaftAppendBlock([params[0], self, params[4]]))

        if len(self.votes) == len(self.neighbors):
            self.current_proposal = None
            returned_params = [(params[0] + 150), self]
            self.voting_timeout = -1
            return [EventRaftProposeBlock(returned_params)]

        return returned_events

    def append_block(self, params):
        '''
                params[0] --> timestamp
                params[1] --> target node
                params[2] --> block
        '''
        if params[2].hash == self.blockchain.last_block.hash:
            return

        new_block = Block(self.blockchain.last_block, params[2].proposer, params[2].timestamp)
        new_block.hash = params[2].hash
        self.blockchain.add_block(new_block)
        self.logger.create_log("{} - Node {} append block {}".format(params[0], self.id, params[2].hash))

    def __str__(self):
        return self.id
