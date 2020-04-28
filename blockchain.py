import sys
from events import *
import random



class Block:

    def __init__(self, last_block, proposer_id: int, timestamp):
        self.last_block = last_block
        self.proposer = proposer_id
        self.timestamp = timestamp
        self.is_correct = True

        self.hash = hash((self.last_block.hash, random.randint(0, 1000)))

class GenesisBlock:

    def __init__(self):
        self.hash = 0
        self.last_block = None
        self.proposer = None
        self.timestamp = 0
        self.is_correct = True

class Blockchain:

    def __init__(self):
        self.last_block = None
        self.level = 0
        self. is_correct = True

    def genesis(self):
        self.last_block = GenesisBlock()
        self.level = 1

    def generate_block(self, proposer_id: int):
        return Block(self.last_block, proposer_id)

    def add_block(self, block: Block):
        if block.last_block != self.last_block:
            return
        self.last_block = block
        self.level += 1

    def __str__(self):
        resp = "Level: {}\n".format(self.level)
        blocks = []
        block_aux = self.last_block
        while block_aux.last_block:
            blocks.append(block_aux.hash)
            block_aux = block_aux.last_block
        blocks.append(block_aux.hash)

        resp += str(blocks)
        return resp



