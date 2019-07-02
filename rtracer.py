import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

class Sphere:
	def __init__(self, center, radius, color):
		self.center = center
		self.radius = radius
		self.color = color

# Multiply Color to Manipulate Brightness
def Change_Brightness(pixel,intensity):
	for color in pixel:
		color = int(round(color * intensity))
		if color > 255:
			print('Invalid Muliplication, > 255')
			return ValueError
	return pixel

# Combine Colors
def Change_Color(first_color,second_color):
	new_color = np.add(first_color,second_color)
	for color in pixel:
		if color > 255:
			print('Invalid Sum, > 255')
			return ValueError
	return new_color

# Canvas Pixel to Viewport
def Canvas_to_Viewport(x,y,width_scale,height_scale):
	x = x * width_scale
	y = y * height_scale
	# d is basically the z and distance to the viewport from canvas in z space
	d = 1
	return x,y,d

# Tracing Ray (Computes intersection of ray with every sphere and return color of sphere at nearest intersection.)
# Ax * Bx + Ay * By + Az * Bz
def SolveIntersect(x,y,d,o,sphere):
	c = sphere.center
	r = sphere.radius
	oc = O - C
	k1 = 

# Create Spheres in Main
def Main():
	# Need to Dot Product o
	o = [0,0,0]
	s1 = Sphere([0,-1,3],1,[255,0,0])
# Solve Quadratic Equation
# Empty 2D Canvas Generator
canvas_width = 100
canvas_height = 100
canvas_empty_pixel = np.array([0,0,0])
canvas_pixel_list = np.zeros((canvas_width,canvas_height,3))

# Scene Settings (X,Y,Z)
camera_position = np.array([0,0,0])

# Canvas to Viewport (Canvas to Viewport is Change of Scale as Viewport Axes Match Orientation of Canvas
view_width = 200
view_height = 200
view_dist_from_camera = 100

