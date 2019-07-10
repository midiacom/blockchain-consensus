import sys
from events import *
import random

class Blockchain:

    blockchain_hash = None
    blockchain_old_hash = None
    level = 0

    def __init__(self):
        pass

    def generate_and_update(self, nodes, main):
        print("Block Generated and Blockchain Updated")
        self.blockchain_old_hash = self.blockchain_hash
        self.blockchain_hash = self.generate_new_hash()
        self.level += 1

        #self.send_updates(nodes)
        #self.create_events_for_nodes(nodes)
        return

    def generate_new_hash(self):
        return


    def create_events_for_nodes(self, nodes):
        events = []

        for i in range(len(nodes)):
            tmp_time = random.randint(1,100)
            tmp_event = EventChangeArrived((tmp_time, i))
            events.append(tmp_event)
            print("Event {} added to the queue ".format(tmp_event.name))
            sys.exit()

    def send_updates(self, nodes):
        for node in nodes:
            #do something
            pass
        return
