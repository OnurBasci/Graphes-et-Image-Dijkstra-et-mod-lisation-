"""
Representation of a general tree
"""


class Tree:
	def __init__(self, data):
		self.children = []
		self.data = data
		self.size = 0 #number of nodes

	def insert(self, child):
		new_node = Tree(child)
		self.children.append(new_node)
		self.size+=1
		return new_node

	def insert_p_c(self, parent, child):
		node = self.recherche(parent)
		node.insert(child)
		self.size += 1

	def recherche(self, node_value):
		if self.data == node_value:
			return self
		for child in self.children:
			val = child.recherche(node_value)
			if val != None:
				return val
		return None


	def find_path(self, n_to_find):
		"""This method returns the path from this node  to n_to_find"""
		if self.data == n_to_find:
			return [self.data]
		elif len(self.children) == 0:
			return None
		else:
			for child in self.children:
				val = child.find_path(n_to_find)
				if val != None:
					val.append(self.data)
					return val
			return None