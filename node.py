import datetime as dt
import datetime as date
import json
import sys


# Nodes for the topology

class Node():

    public_key = None # public key generated with rsa
    private_key = None # private key generated with rsa
    timestamp = None
    topology = None
    ID = None

    blockchain = None

    neighbors = None

    def __init__(self, topology=None, blockchain=None):
        self.topology = topology
        self.blockchain = blockchain
        self.callbacks = {"eventShowNeighbors": self.eventPrintNeighbors}
        return

    def eventPrintNeighbors(self, event):
        event.returned = True
        print("Node ID {}, neighbors = {}".format(self.ID, self.neighbors))

    def handle_event(self, event):
        try:
            self.callbacks[event.name](event)
        except KeyError:
            print(event.name + " event not implemented on node.")

    def get_dict(self):
        data = self.__dict__
        return data


class NewNode (Node):

    def __init__(self):
        Node.callbacks["newEvent"] = self.newEvent
    def newEvent(self, params):
        print("This is a new Event from NewNode")
