"""
this files contains functions to find the optimal path from the start point to the end
"""
from util import get_index


def h(point, end_point, width):
	"""
	From a point (tuple) finds the manhattan distance to the end point (tuple)
	"""
	p = get_index(point, width)
	e_point = get_index(end_point, width)
	return (abs(e_point[0]-p[0]) + abs(e_point[1]-p[1]))


def A_star(start, end, graph, height, width):
	"""
	:param start: an int representing the index of the start node
	:param end: an int representing the index of the end node
	:param graph:
	:return: a list of index for the path
	"""
	path = []

	current_node = start #start point
	current_cuple = tuple()
	g = 0 #start distance
	min_g = 0

	min_node_index = 0
	min_node = start

	can_go = []  #the nodes that we can go. form: (node_num, g+h)

	#end condition
	Found = False

	while not(Found):

		neighboors = graph.get_adj(current_node)
		#add the neigbors to can_go
		for n in neighboors:
			temp_g = g
			temp_g+=n[1] #add the weight
			#if the case is not already in the path
			if n[0] not in path:
				can_go.append((n[0],temp_g + h(n[0], end, width)))

		for case in can_go:
			# remove already discovered
			if case[0] in path:
				can_go.remove(case)

		#print(can_go)
		#print(path)

		#get the minimum distance indicies
		min_dist_val = 10000000
		for case in can_go:
			temp_g = g
			temp_g += case[1]
			dist = temp_g + h(case[0], end, width)
			#print(min_dist_val, dist)
			if min_dist_val > dist:
				min_dist_val = dist
				min_node_index = can_go.index(case)
				min_node = case[0]
				current_cuple = case
				min_g = graph.get_weight_from_node(current_node, min_node)#case[1] - h(min_node, end, height)
				#if we decide to go back <--> we don't chose a neighboor
				if min_g == -1:
					min_g = case[1] - h(min_node, end, width)
				#print(f"case[0]: {case[0]} case[1]: {case[1]} heuristique: {h(min_node, end, width)}, min_g: {min_g}")

		#go to min valued node
		current_node = min_node
		path.append(current_node)
		g+=min_g  #can_go[min_node_index][1]
		#print("value of g is " + str(g) + " value of h " +)

		if current_cuple in can_go:
			can_go.remove(current_cuple)

		#print(current_node)

		#if the current node is the end node than end the loop
		if current_node == end:
			Found = True
	#print([get_index(n, width) for n in path])
	return [get_index(n, width) for n in path]



