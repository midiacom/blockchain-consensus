from enum import Enum
from typing import List
from Utils.logger import LoggerAux
from Nodes import Node


class State(Enum):
    idle = 1
    busy = 2
    proposing = 3
    waiting = 4


class ConservationNode(Node):

    def __init__(self, node_id: int, is_faulty: bool, neighbors: List[object], logger: LoggerAux):
        super().__init__(node_id, is_faulty, neighbors, logger)

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
