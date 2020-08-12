import networkx as nx
from Nodes.node import *
from Blockchain import blockchain as bc
import pandas as pd


# Class Graph with methods to generate Miners and Nodes

class Graph(nx.Graph):

    dict_nodes = {}
    nodes_object = {}

    nodes_took = [0,11,12,14,18,22,24,27,30,38,40,42,43,48,49,50,58,59,63,67,73,82,84,85,90,91,92,98,102,117,118,121,123,124,126,128,130,136,151,226,568,1339,1398,1563,1638,1652,1996,2075,2294,2361,2457,2467,2554,2560,2583,2650,2764,2842,2951,2957,2967,2979,3004,3007,3014,3039,3057,3152,3186,3339,3350,3356,3402,3461,3530,3638,3762, 3763,3809,3833,3912, 3911,4009,4021,4193,4194,4223,4260,4272,4332,4500,4510,4561,4575,4817,4827,5102,5266,5493,5509,5535,5562,5572,5584,5620,5621,5628,5637,5651,5671,5690,5696,5697,5716,5727,5728,5734,5735,5751,5758,5771,5787,5794,5812,5834,5841,5842,5865,6000, 6002,6001]

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

        df = pd.read_csv("../Graph Generate/soc-sign-bitcoinotc.csv")

        source = df["6"]

        target = df["2"]

        rating = df["4"]

        timestamp = df["1289241911.72836"]

        """
        self.set_dict_nodes()
        print(list(self.nodes))
        print(self.adj.items())
        sys.exit()
        largest_cc = max(nx.connected_components(self), key=len)
        """

        self.set_edges(source, target)
        self.set_neighbors()
        largest_cc = nx.node_connected_component(self,8)
        for node in list(self.nodes):
            if node not in largest_cc:
                self.remove_node(node)


        """
        #print(nx.number_connected_components(self))
        #for c in nx.connected_components(self):
        #    print(c)
        #for c in nx.connected_components(self):
        #    print(self.subgraph(c))
        #print(largest_cc)
        #nx.write_gml(self, "bitcoinotc.gml")
        """

    def set_dict_nodes(self):
        for node in list(self.nodes):
            self.dict_nodes[node[0]] = node[1]
        return

    def set_edges(self, source, target):
        """
        for i in range(len(source)):
            self.add_edge((source[i],self.dict_nodes[source[i]]), (target[i],self.dict_nodes[target[i]]))
        """

        for i in range(len(source)):
            self.add_edge(source[i], target[i])

    def set_neighbors(self):
        print("\nSetting Initial Neighbors")
        for node in list(self.nodes):

            """
            node[1].neighbors = self[(node[0], node[1])]
            print("Neighbors for Node {} = {}".format(node[0], node[1].neighbors))
            print("node = ",self[node], end="\n\n")
            if(node == 7):
                sys.exit()
            """
            self.nodes_object[node].neighbours = self[node]
            pass
        return
