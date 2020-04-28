from node import RaftNode
import random
from raft_events import *
from Logger import LoggerAux
from simulation import Simulation


if __name__ == "__main__":

    nodes = []
    event_flow = []
    logger = LoggerAux("Raft_Log.txt")

    for node in range(10):
        nodes.append(RaftNode(node, False, [], logger))

    for node in nodes:
        node.neighbors = [x for x in nodes if x != node]
        #print([x.id for x in node.neighbors])
        if node.id == 1:
            node.is_leader = True
            event_flow.append(EventRaftProposeBlock([0, node]))

    #simulation_steps = 8640000
    simulation_steps = 1000

    sim = Simulation(simulation_steps, nodes, event_flow)
    sim.run()

    for node in nodes:
        print(node.blockchain.last_block.hash)

    print("\n")
    print(nodes[1].blockchain)



