import datetime as dt
import datetime as date
import json
import sys
import random
from events import *
from enum import Enum
from blockchain import Blockchain, Block
from typing import List
from raft_events import *


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
        return "Node: {}\nNeighbors: {}\nCandidates: {}".format(self.id, [n.id for n in self.neighbors], [c.id for c in self.candidates])


class RaftNode:

    votes = []
    current_proposal= None

    def __init__(self, node_id: int, neighbors: List[object]):
        self.id = node_id
        self.neighbors = neighbors
        self.blockchain = Blockchain()
        self.blockchain.genesis()
        self.is_leader = False
        self.state = State.idle
        self.callbacks = {"propose_block": self.propose_block,
                          "validate_block": self.validate_block,
                          "receive_response": self.receive_response}

    def propose_block(self, params):
        if not self.is_leader:
            return
        self.votes = []
        self.current_proposal = Block(self.blockchain.last_block, self.id, params[0])
        validate_events = []
        for neighbor in self.neighbors:
            resp_params = [params[0]+random.randint(10, 100), neighbor, self.current_proposal, self]
            validate_events.append(EventRaftValidateBlock(resp_params))
        return validate_events

    def validate_block(self, params):
        if params[2].is_correct:
            new_block = Block(self.blockchain.last_block, params[2].proposer, params[2].timestamp)
            new_block.hash = params[2].hash
            self.blockchain.add_block(new_block)
            return [EventRaftReceiveResponse([params[0]+random.randint(10, 100), params[3], self, True, params[2]])]

    def receive_response(self, params):
        if params[4].hash == self.current_proposal.hash:
            self.votes.append(params[1])
        if len(self.votes) > int(round(len(self.neighbors)/2)):
            self.blockchain.add_block(self.current_proposal)
        if len(self.votes) > len(self.neighbors):
            self.current_proposal = None
            returned_params = [(params[0] + 150), self]
            return [EventRaftProposeBlock(returned_params)]

    def __str__(self):
        return self.id