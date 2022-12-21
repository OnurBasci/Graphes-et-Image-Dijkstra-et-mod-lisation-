from dijkstra import dijkstra
from graphe import Graph
from util import toValuedGraphe
import cv2 as cv
from Astar import A_star
from interface import show

def dijkstraEvent(image_path):
	img = cv.imread(image_path, cv.IMREAD_GRAYSCALE)

	g = toValuedGraphe(img)

	path = A_star(9, 54, g, img.shape[0], img.shape[1])

	show(img, path)
	print(path)


class deneme():
	def __init__(self):
		self.name = "a"
	def print(self):
		print(self.name)

if __name__ == '__main__':
	d = deneme()
	d.print()