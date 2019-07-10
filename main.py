# imports
from node import *
from constants import *
#from threading import Thread
from events import *
import topology
from scipy.stats import dgamma
import os
import json
import sys
import random


events = []

def generate_events(list):
	for timestamp in list:
		id = random.randint(0, initial_nodes)
		new_event = GenerateBlockEvent([timestamp, id])
		events.append(new_event)

	return

def node_do_event(event, id, topology):
	for nodes in topology.nodes:
		if(nodes[1].ID == id):
			print("Node {} has to do event\n".format(nodes[1].ID))
			nodes[1].handle_event(event)
	return

def sort_events(list):
	return

if __name__ == "__main__":

	print("Criando Topologia")
	topo = topology.Topology()
	#topo.make_block_flow(simulation_steps)
	generate_events(block_generated_flow)
	#print("Events created = ", events)

	for step in range(simulation_steps):
		if(events[0].timestamp == step):
			tmp_event = events[0]
			events.remove(tmp_event)
			#print("\nStep for Event = ", step)
			#node_do_event(tmp_event, tmp_event.node_ID, topo)
