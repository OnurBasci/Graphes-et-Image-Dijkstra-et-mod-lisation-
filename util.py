import numpy as np
import math
from graphe import Graph
from PIL import Image
import cv2 as cv

def get_distance(color1, color2, coef_index):
	"""
	This function takes two color (black and white) and return euclidien distance of it
	"""
	if coef_index == 0:
		return 0
	dist = abs(color1 - color2)
	d_normalized = dist/(255/coef_index)

	return d_normalized

def get_distance_color(color1, color2, coef_index):
	"""
		This function takes two color (RGB) and return euclidien distance of it
	"""
	if coef_index == 0:
		return 0
	dist = math.sqrt(math.pow(int(color1[0]) - int(color2[0]), 2) + math.pow(int(color1[1]) - int(color2[1]), 2) + math.pow(int(color1[2]) - int(color2[2]), 2))
	d_normalized = dist/(442/coef_index)

	return d_normalized

def get_index(node_num, width):
	"""
	return i and j values from index
	"""
	return (int(node_num/width), node_num%width)

def getValues(img, graph, elem, i, j, height, width, coef_index):
	"""for x in range(i-1, i+2):
		for y in range(j-1, j + 2):
			valued_matrix[x,y] = get_distance(int(img[x][y]), int(img[i][j]))"""
	c_pixel_value = int(img[i, j])
	current_pix = i * width + j
	if i != 0 and j != 0 and i != height - 1 and j != width -1 :
		#add 4 connex pixels
		graph.add_edge(current_pix, current_pix +1, get_distance(c_pixel_value, int(img[i, j+1], coef_index)))
		graph.add_edge(current_pix, current_pix - 1, get_distance(c_pixel_value, int(img[i, j-1],coef_index)))
		graph.add_edge(current_pix, (i-1)*width + j, get_distance(c_pixel_value, int(img[i-1, j],coef_index)))
		graph.add_edge(current_pix, (i+1) * width + j, get_distance(c_pixel_value, int(img[i+1, j],coef_index)))
	if i == 0 or i == height-1:
		if j>0 and j < width - 1:
			graph.add_edge(current_pix, current_pix + 1, get_distance(c_pixel_value, int(img[i, j + 1],coef_index)))
			graph.add_edge(current_pix, current_pix - 1, get_distance(c_pixel_value, int(img[i, j - 1],coef_index)))
		elif j == 0:
			graph.add_edge(current_pix, current_pix + 1, get_distance(c_pixel_value, int(img[i, j + 1],coef_index)))
		elif j == width - 1:
			graph.add_edge(current_pix, current_pix - 1, get_distance(c_pixel_value, int(img[i, j - 1],coef_index)))
		if i == 0:
			graph.add_edge(current_pix, (i + 1) * width + j, get_distance(c_pixel_value, int(img[i + 1, j],coef_index)))
		else:
			graph.add_edge(current_pix, (i - 1) * width + j, get_distance(c_pixel_value, int(img[i - 1, j],coef_index)))
	if j == 0 or j == width - 1:
		if i>0 and i < height-1:
			graph.add_edge(current_pix, (i - 1) * width + j, get_distance(c_pixel_value, int(img[i - 1, j],coef_index)))
			graph.add_edge(current_pix, (i + 1) * width + j, get_distance(c_pixel_value, int(img[i + 1, j],coef_index)))
		if j == 0:
			graph.add_edge(current_pix, current_pix + 1, get_distance(c_pixel_value, int(img[i, j + 1],coef_index)))
		else:
			graph.add_edge(current_pix, current_pix - 1, get_distance(c_pixel_value, int(img[i, j - 1],coef_index)))


def getValuesColored(img, graph, elem, i, j, height, width,coef_index):

	c_pixel_value = img[i, j]
	current_pix = i * width + j
	if i != 0 and j != 0 and i != height - 1 and j != width - 1:
		# add 4 connex pixels
		graph.add_edge(current_pix, current_pix + 1, get_distance_color(c_pixel_value, img[i, j + 1],coef_index))
		graph.add_edge(current_pix, current_pix - 1, get_distance_color(c_pixel_value, img[i, j - 1],coef_index))
		graph.add_edge(current_pix, (i - 1) * width + j, get_distance_color(c_pixel_value, img[i - 1, j],coef_index))
		graph.add_edge(current_pix, (i + 1) * width + j, get_distance_color(c_pixel_value, img[i + 1, j],coef_index))
	if i == 0 or i == height - 1:
		if j > 0 and j < width - 1:
			graph.add_edge(current_pix, current_pix + 1, get_distance_color(c_pixel_value, img[i, j + 1],coef_index))
			graph.add_edge(current_pix, current_pix - 1, get_distance_color(c_pixel_value, img[i, j - 1],coef_index))
		elif j == 0:
			graph.add_edge(current_pix, current_pix + 1, get_distance_color(c_pixel_value, img[i, j + 1],coef_index))
		elif j == width - 1:
			graph.add_edge(current_pix, current_pix - 1, get_distance_color(c_pixel_value, img[i, j - 1],coef_index))
		if i == 0:
			graph.add_edge(current_pix, (i + 1) * width + j, get_distance_color(c_pixel_value, img[i + 1, j],coef_index))
		else:
			graph.add_edge(current_pix, (i - 1) * width + j, get_distance_color(c_pixel_value, img[i - 1, j],coef_index))
	if j == 0 or j == width - 1:
		if i > 0 and i < height - 1:
			graph.add_edge(current_pix, (i - 1) * width + j, get_distance_color(c_pixel_value, img[i - 1, j],coef_index))
			graph.add_edge(current_pix, (i + 1) * width + j, get_distance_color(c_pixel_value, img[i + 1, j],coef_index))
		if j == 0:
			graph.add_edge(current_pix, current_pix + 1, get_distance_color(c_pixel_value, img[i, j + 1],coef_index))
		else:
			graph.add_edge(current_pix, current_pix - 1, get_distance_color(c_pixel_value, img[i, j - 1],coef_index))


def toValuedGraphe(img_path, coef_index):
	"""
	this function takes an image and returns a numpy array representing adjacency matrix
	"""
	#read the image
	im = Image.open(img_path)


	#Let's instanciate the graph size of number of pixels
	graph = Graph(im.size[0] * im.size[1])
	#if it is a colored image
	if im.mode == "RGB" or im.mode == "RGBA":
		img = cv.imread(img_path, cv.IMREAD_COLOR)
		for i, ligne in enumerate(img):
			for j, elem in enumerate(ligne):
				getValuesColored(img, graph, elem, i, j, img.shape[0], img.shape[1], coef_index)
	else:
		img = cv.imread(img_path, cv.IMREAD_GRAYSCALE)
		for i, ligne in enumerate(img):
			for j, elem in enumerate(ligne):
				getValues(img, graph, elem, i, j, img.shape[0], img.shape[1], coef_index)

	return graph, img


def read_imag(img_path):
	# read the image
	im = Image.open(img_path)

	if im.mode == "RGB":
		img = cv.imread(img_path, cv.IMREAD_COLOR)
	else:
		img = cv.imread(img_path, cv.IMREAD_GRAYSCALE)

	return img