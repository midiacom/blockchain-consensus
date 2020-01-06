from node import RaftNode
import random
from raft_events import *
from Logger import LoggerAux

if __name__ == "__main__":

    nodes = []
    event_flow = {}
    logger = LoggerAux("Raft_Log.txt")

    for node in range(10):
        nodes.append(RaftNode(node, False, [], logger))

    for node in nodes:
        node.neighbors = [x for x in nodes if x != node]
        #print([x.id for x in node.neighbors])
        if node.id == 1:
            node.is_leader = True
            event_flow[0] = []
            event_flow[0].append(EventRaftProposeBlock([0, node]))

    #simulation_steps = 8640000
    simulation_steps = 1000
    for step in range(simulation_steps):
        if step in event_flow.keys():
            for event in event_flow[step]:
                returned_events = event.event_handler()
                if returned_events:
                    for e in returned_events:
                        if e.timestamp not in event_flow.keys():
                            event_flow[e.timestamp] = []

                        event_flow[e.timestamp].append(e)

            event_flow.pop(step)

    for node in nodes:
        print(node.blockchain.last_block.hash)

    print("\n")
    print(nodes[1].blockchain)



