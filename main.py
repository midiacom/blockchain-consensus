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

	"""for timestamp in list:
		id = random.randint(0, initial_nodes)
		new_event = GenerateBlockEvent([timestamp, id])
		print("({}, {}),".format(timestamp, id), end=" ")
		events.append(new_event)

	sys.exit()"""

	for item in list:
		new_event = Event_Generate_Block([item[0], item[1]])
		events.append(new_event)
	return

def node_do_event(event, id, topology, step):
	"""
	for nodes in topology.nodes:
		if(nodes[1].ID == id):
			print("Node {} has to do event\n".format(nodes[1].ID))
			nodes[1].handle_event(event)
	"""
	topology.nodes_object[id].handle_event(event, step)
	return

def sort_events(list):
	return

if __name__ == "__main__":

	print("Criando Topologia")
	topo = topology.Topology()

	#topo.make_block_flow(simulation_steps)
	#generate_events(block_generated_flow)

	"""generate_events(block_generated_event_flow)"""

	#print("Events created = ", events)

	event_msg = Event_Send_Msg([5000, 5494])
	events.append(event_msg)

	for step in range(simulation_steps):
		if(len(events) != 0):
			if(events[0].timestamp == step):
				tmp_event = events[0]
				events.remove(tmp_event)
				print("\nStep for Event = ", step)
				node_do_event(tmp_event, tmp_event.node_ID, topo, step)
