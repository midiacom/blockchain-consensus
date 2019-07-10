import datetime as dt
import datetime as date
import json
import sys
import random
from events import *


# Nodes for the topology

class Node():

    public_key = None # public key generated with rsa
    private_key = None # private key generated with rsa
    timestamp = None
    topology = None
    ID = None

    blockchain = None

    neighbors = None

    def __init__(self, topology=None, blockchain=None,ID=None):
        self.ID = ID
        self.topology = topology
        self.blockchain = blockchain
        self.callbacks = {"eventShowNeighbors": self.event_Print_Neighbors,
                          "eventGenerateBlock": self.event_Generate_Block,
                          "eventChangeArrived": self.event_Change_Arrived,
                          "eventSendMsg": self.event_Send_Message}
        return

    def event_Print_Neighbors(self, event, step):
        event.returned = True
        print("Node ID {}, neighbors = {}".format(self.ID, self.neighbors))

    def event_Generate_Block(self, event, step):
        event.returned = True
        self.generate_Block(event.params)

    def event_Change_Arrived(self, event, step):
        pass

    def event_Send_Message(self, event, step):
        event.returned = True

        for neighbour in self.neighbours:
            delay = random.randint(0,100)
            new_event = Event_Send_Msg([(step+delay), neighbour])
            print("Event Send Msg Created for timestamp = {} on NODE ID = {}".format((step+delay), neighbour))


    def generate_Block(self, params):
        print("Block Generated on NODE ID = ", self.ID)
        self.blockchain.generate_and_update(self.topology.nodes, self)


    def handle_event(self, event, step):
        try:
            self.callbacks[event.name](event, step)
        except KeyError:
            print(event.name + " event not implemented on node.")

    def get_dict(self):
        data = self.__dict__
        return data


class New_Node (Node):

    def __init__(self):
        Node.callbacks["newEvent"] = self.newEvent
    def new_Event(self, params):
        print("This is a new Event from NewNode")
