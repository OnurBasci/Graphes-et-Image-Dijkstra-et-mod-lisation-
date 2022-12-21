from tree import Tree
from math import inf
from util import get_index

def dijkstra(graphe, node_s, node_e, width):
	"""
	this function takes a graphe and apply the dijkdtra Algorithme it returns the path to go from
	the node_s to node_e
	"""

	T = Tree(node_s)
	#distance initialization
	parent = [None for x in range(graphe.m_num_of_nodes)]
	dist_prov = [inf for x in range(graphe.m_num_of_nodes)]
	dist_finale = [-1 for x in range(graphe.m_num_of_nodes)]
	dist_finale[node_s] = 0
	last_added = node_s
	tree_nodes = [node_s]

	while graphe.m_num_of_nodes != T.size:
		for v in graphe.get_adj(last_added):
			if dist_finale[last_added] + v[1] < dist_prov[v[0]]:
				dist_prov[v[0]] = dist_finale[last_added] + v[1]
				parent[v[0]] = last_added

		#print([number for number in dist_prov if dist_prov.index(number) not in tree_nodes])
		#min_v = dist_prov.index(min(number for number in dist_prov if dist_prov.index(number) not in tree_nodes))#dist_prov.index(min(dist_prov))
		#print(dist_prov)

		#put -1 for already used node
		for i in range(len(dist_prov)):
			ind = []
			if (i in tree_nodes) and i not in ind:
				dist_prov[i] = -1
				ind.append(i)

		min_val = max(dist_prov)
		for d in dist_prov:
			if d != -1:
				if d < min_val:
					min_val = d
		min_v = dist_prov.index(min_val)

		#print(f"tree: {tree_nodes}, min: {min_v}, parent {parent[min_v]} longuer {len(tree_nodes)}")
		T.insert_p_c(parent[min_v], min_v)
		dist_finale[min_v] = dist_prov[min_v]
		last_added = min_v
		tree_nodes.append(last_added) #we add tree(node) to be able to compare

	path = T.find_path(node_e)
	path.reverse()

	return [get_index(n, width) for n in path]

