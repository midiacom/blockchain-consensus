from Nodes import RaftNode
from Events.raft_events import *
from Utils.logger import LoggerAux
from Simulation.simulation import Simulation
from Blockchain.blockchain import BitcoinBlockchain, Block


def raft_tests():
    nodes = []
    event_flow = []
    logger = LoggerAux("Raft_Log.txt")

    for node in range(10):
        nodes.append(RaftNode(node, False, [], logger))

    for node in nodes:
        node.neighbors = [x for x in nodes if x != node]
        # print([x.id for x in node.neighbors])
        if node.id == 1:
            node.is_leader = True
            event_flow.append(EventRaftProposeBlock([0, node]))

    # simulation_steps = 8640000
    simulation_steps = 1000

    sim = Simulation(simulation_steps, nodes, event_flow)
    sim.run()

    for node in nodes:
        print(node.blockchain.last_block.hash)

    print("\n")
    print(nodes[1].blockchain)

def bitcoin_tests():
    bc = BitcoinBlockchain()

    bc.genesis()

    for i in range(10):
        block = Block(bc.last_block, 1)
        bc.add_block(block)

    print(bc)


if __name__ == "__main__":

    #raft_tests()

    bitcoin_tests()



