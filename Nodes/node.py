from Blockchain.blockchain import Blockchain
from typing import List
from Utils.logger import LoggerAux


# Abstract Node for the topology

class Node:
    def __init__(self, node_id: int, is_faulty: bool, neighbors: List[object], logger: LoggerAux):
        self.id = node_id
        self.is_faulty = is_faulty
        self.neighbors = neighbors
        self.logger = logger
        self.blockchain = Blockchain()
        self.blockchain.genesis()


