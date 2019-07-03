import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

class Pixel:
	def __init__(self, x, y, z, rgb):
		self.x = x
		self.y = y
		self.z = z
		self.rgb = rgb

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
# Solve Quadratic Eqn
def SolveIntersect(x,y,d,o,sphere):
	c = sphere.center
	r = sphere.radius
	#oc = o - C
	for dimension in o:
		dimension = dimension + C[o.index(dimension)]
	k1 = (x*x) + (y*y)
	k2 = 2 * ((oc[0]*x) + (oc[1]*y))
	k3 = ((oc[0]*oc[0]) + (oc[1]*oc[1])) - (r*r)
	discriminant = k2*k2 - 4*k1*k3
	if discriminant < 0:
		return false,false
	t1 = ((-k2) + sqrt(discriminant)) / (2*k1)
	t2 = ((-k2) - sqrt(discriminant)) / (2*k1)
	return t1,t2

# Create Spheres in Main
def Main():
	# Initialize Pixels in Canvas
	canvas_width = 100
	canvas_height = 100
	canvas_empty_pixel = [0,0,0]
	canvas_pixel_list = []
	for x in range(0,len(canvas_width)):
		for y in range(0,len(canvas_height)):
			canvas_pixel_list.append(Pixel(x,y,d,canvas_empty_pixel))

	# Need to Dot Product o
	o = [0,0,0]
	# List of Spheres
	list_of_spheres = []
	s1 = Sphere([0,-1,3],1,[255,0,0])
	list_of_spheres.append(s1)
	for sphere in list_of_spheres:
		t1,t2 = SolveIntersect(x,y,d,o,sphere)

'''
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

'''
