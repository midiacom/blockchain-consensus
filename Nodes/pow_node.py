import random
from typing import List
from Events.raft_events import *
from Utils.logger import LoggerAux
from Nodes import Node


class PoWNode(Node):

    def __init__(self, node_id: int, is_faulty: bool, neighbors: List[object], logger: LoggerAux):
        super().__init__(node_id, is_faulty, neighbors, logger)
        self.callbacks = []

    def propose_block(self, params):
        '''
           params[0] --> timestamp
           params[1] --> target node
        '''

        if self.is_faulty:
            self.current_proposal.is_correct = False
        validate_events = []
        for neighbor in self.neighbors:
            resp_params = [params[0] + random.randint(10, 100), neighbor, self.current_proposal, self]
            validate_events.append(EventPoWValidateBlock(resp_params))
        self.logger.create_log("{} - Node {} Published block".format(params[0], self.id))
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