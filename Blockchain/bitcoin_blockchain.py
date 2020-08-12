from Blockchain import Blockchain, Block


class BitcoinBlockchain(Blockchain):

    def __init__(self):
        super().__init__()
        self.fork = self.last_block
        self.fork_level = 0

    def add_block(self, block: Block):
        if block.last_block.hash == self.last_block.hash:
            self.last_block = block
            self.level += 1
        elif block.last_block.hash == self.fork.hash:
            self.fork = block
            self.fork_level += 1
        else:
            block_aux = self.last_block
            fork_height = 0
            while block_aux.last_block:
                fork_height -= 1
                if block_aux.last_block.hash == block.hash:
                    self.fork = block
                    self.fork_level = self.level - fork_height
                    break

        if (self.level - self.fork_level) > 6:
            if self.level > self.fork_level:
                self.fork = self.last_block
                self.fork_level = self.level
            else:
                self.last_block = self.fork
                self.level = self.fork_level

    def genesis(self):
        super().genesis()
        self.fork = self.last_block
        self.fork_level = self.level

    def __str__(self):
        resp = super().__str__()

        fork_height = abs(self.fork_level - self.level)

        if fork_height > 0:
            resp += f'\nFork {fork_height}:\n'
            fork_aux = self.fork
            resp_aux = []
            for i in range(fork_height):
                resp_aux.append(str(fork_aux.hash))
                fork_aux = fork_aux.last_block
        resp += str(resp_aux)

        return resp
