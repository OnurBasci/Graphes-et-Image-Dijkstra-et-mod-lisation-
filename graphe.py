"""
Representation of a graphe as a list of adjacency containing the adjacent nodes and their weight
"""



class Graph:
	def __init__(self, num_of_nodes, directed=True):
		self.m_num_of_nodes = num_of_nodes
		self.m_nodes = range(self.m_num_of_nodes)

		# Define the type of a graph
		self.m_directed = directed

		self.m_adj_list = {node: set() for node in self.m_nodes}

	def add_edge(self, node1, node2, weight=1):
		self.m_adj_list[node1].add((node2, weight))

		if not self.m_directed:
			self.m_adj_list[node2].add((node1, weight))

	def get_adj(self, node):
		return self.m_adj_list[node]

	def print_adj_list(self):
		for key in self.m_adj_list.keys():
			print("node", key, ": ", self.m_adj_list[key])

	def get_weight_from_node(self, node1, node2):
		neighboors = self.get_adj(node1)
		for n in neighboors:
			if n[0] == node2:
				return n[1]
		#if it 's not a neighboor than we can't add g so 0
		return -1