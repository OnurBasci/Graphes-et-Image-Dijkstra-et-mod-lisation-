import cv2 as cv
from PIL import Image
import numpy as np
from util import *
from Astar import *
from graphe import Graph
from tree import Tree
from interface import show, gui
from Astar import get_index
from dijkstra import dijkstra
from PIL import Image

def main():
	img_path = "D:\Pycharm_project\AlgorithmiqueAvancee\images\collab1.png"
	#print(img2[0])
	#gui()
	#print(img.shape)
	#print(int(img[0, 0]) - int(img[0, 1]))

	g = toValuedGraphe(img_path)
	g.print_adj_list()

	#path = dijkstra(g, 55, 62, img.shape[1])

	#path = A_star(9, 54, g, img.shape[0], img.shape[1])
	#print(path)
	#show(img, path)

	#test()




def test():
	g = Graph(8, False)

	g.add_edge(0, 1, 3)
	g.add_edge(0, 2, 1)
	g.add_edge(1, 2, 1)
	g.add_edge(1, 4, 5)
	g.add_edge(1, 3, 3)
	g.add_edge(4, 6, 4)
	g.add_edge(3, 6, 2)
	g.add_edge(3, 7, 3)
	g.add_edge(7, 6, 1)
	g.add_edge(7, 5, 6)
	g.add_edge(2, 5, 2)

	p = dijkstra(g, 0, 5)
	print(f"path is {p}")

	#print(dist)

if __name__ == '__main__':
	main()
