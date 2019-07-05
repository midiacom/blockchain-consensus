# imports
from node import *
from constants import *
#from threading import Thread
import topology
from scipy.stats import dgamma
import os
import json
import sys

if __name__ == "__main__":

	print("Criando Topologia")
	topo = topology.Topology()
	topo.make_block_flow(simulation_steps)

	for step in range(simulation_steps):
		#print("Step being Executed = ", step)
		pass
