import networkx as nx
from node import *
import time
import blockchain as bc

# Class Graph with methods to generate Miners and Nodes

class Graph(nx.Graph):

    def __init__(self):
        nx.Graph.__init__(self)

    def make_nodes(self, amount, topology=None):
        print("Creating nodes in topology = ", topology.name)
        print("")
        nodes = []
        for i in range(amount):
            new_node = Node(topology=topology, blockchain=bc.Blockchain())
            nodes.append((i, new_node))
            # Adding nodes from nodes array
        self.add_nodes_from(nodes)
        print("Nodes added to Topology")
        print("Number of nodes = ", self.number_of_nodes())
        #print("Nodes are = ", list(self.nodes))

        self.set_neighbors()

    def set_neighbors(self):
        print("\nSetting Initial Neighbors")
        for node in list(self.nodes):
            node[1].neighbors = self[(node[0], node[1])]
            print("Neighbors for Node {} = {}".format(node[0], node[1].neighbors))
            pass
        return
