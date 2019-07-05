# imports
from node import *
from constants import *
#from threading import Thread
from nxgraph import Graph
from scipy.stats import dgamma
import os
import json
import sys


class Topology(Graph):
	name = "Generic Topology"
	block_closed_flow = []

	def __init__(self, initial_nodes=initial_nodes):
		Graph.__init__(self)
		# Creating Nodes
		print("Creating Nodes in Topology.py")
		self.member_nodes = self.make_nodes(initial_nodes, self)

	# generating block flow with dgamma.rvs
	def make_block_flow(self,max_steps):
		step = 0
		# default parameters from multichain
		while step <= max_steps:
			time_block = dgamma.rvs(2.0000170661444634, 5.4611854838492295, 0.8244588748930897)
			time_block = int(round(time_block)) * 1000
			step += time_block
			self.block_closed_flow.append(step)

		print("Block flow generated = ", self.block_closed_flow)
		return
