import networkx as nx
from node import *
import time
import blockchain as bc
import pandas as pd
import sys

# Class Graph with methods to generate Miners and Nodes

class Graph(nx.Graph):

    dict_nodes = {}
    nodes_object = {}


    def __init__(self):
        nx.Graph.__init__(self)

    def make_nodes(self, amount, topology=None):
        print("Creating nodes in topology = ", topology.name)
        print("")
        nodes = []
        for i in range(amount):
            new_node = Node(topology=topology, blockchain=bc.Blockchain(), ID=i)
            #nodes.append((i, new_node))
            nodes.append((i))
            self.nodes_object[i] = new_node

        # Adding nodes from nodes array
        self.add_nodes_from(nodes)
        print("Nodes added to Topology")
        print("Number of nodes = ", self.number_of_nodes())
        #print("Nodes are = ", list(self.nodes))

        df = pd.read_csv("Graph Generate/soc-sign-bitcoinotc.csv")

        source = df["6"]

        target = df["2"]

        rating = df["4"]

        timestamp = df["1289241911.72836"]

        #self.set_dict_nodes()
        #print(list(self.nodes))
        self.set_edges(source, target)

        #print(self.adj.items())
        #sys.exit()
        self.set_neighbors()
        largest_cc = max(nx.connected_components(self), key=len)

    def set_dict_nodes(self):
        for node in list(self.nodes):
            self.dict_nodes[node[0]] = node[1]
        return

    def set_edges(self, source, target):
        #for i in range(len(source)):
            #self.add_edge((source[i],self.dict_nodes[source[i]]), (target[i],self.dict_nodes[target[i]]))
        for i in range(len(source)):
            self.add_edge(source[i], target[i])

    def set_neighbors(self):
        print("\nSetting Initial Neighbors")
        for node in list(self.nodes):
            #node[1].neighbors = self[(node[0], node[1])]
            #print("Neighbors for Node {} = {}".format(node[0], node[1].neighbors))
            #print("node = ",self[node], end="\n\n")
            #if(node == 7):
            #    sys.exit()
            self.nodes_object[node].neighbours = self[node]
            pass
        return
