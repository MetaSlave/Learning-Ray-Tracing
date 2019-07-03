from PIL import Image

import numpy as np
import math
import operator

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
def TraceRay(o,x,y,d,t_min,t_max,list_of_spheres,BACKGROUND_COLOR):
	closest_t = float('inf')
	closest_sphere = None
	for sphere in list_of_spheres:
		t1,t2 = SolveIntersect(x,y,d,o,sphere)
		if (t_min < t1 < t_max) and (t1 < closest_t):
			closest_t = t1
			closest_sphere = sphere
		if (t_min < t2 < t_max) and (t2 < closest_t):
			closest_t = t2
			closest_sphere = sphere
	print(t1,t2)
	if closest_sphere is None:
		print("Pixel " + str(x) + "," + str(y) + " is background.")
		return BACKGROUND_COLOR
	print("Pixel" + str(x) + "," + str(y) + " is sphere.")
	return closest_sphere.color

# Ax * Bx + Ay * By + Az * Bz
# Solve Quadratic Eqn
def SolveIntersect(x,y,d,o,sphere):
	c = sphere.center
	r = sphere.radius
	#oc = o - C
	o = list(map(operator.sub,c,o))
	#Change to 3D Calculation
	oc = o
	k1 = (x*x) + (y*y) + (d*d)
	k2 = 2 * ((oc[0]*x) + (oc[1]*y) + (oc[2]*d))
	k3 = ((oc[0]*oc[0]) + (oc[1]*oc[1]) + (oc[2]*oc[2])) - (r*r)
	discriminant = (k2*k2) - (4*k1*k3)
	print(k1,k2,k3)
	if discriminant < 0:
		return False,False
	if k1 == 0:
		t1 = 0
		t2 = 0
	else:
		t1 = ((-k2) + math.sqrt(discriminant)) / (2*k1)
		t2 = ((-k2) - math.sqrt(discriminant)) / (2*k1)
	return t1,t2

# Create Spheres in Main
def Main():

	# Need to Dot Product o
	o = [0,0,0]
	BACKGROUND_COLOR = [0,0,0]
	t_min = 1
	t_max = float('inf')
	list_of_colors = []

	# List of Spheres
	list_of_spheres = []
	s1 = Sphere([0,-1,3],1,[255,0,0])
	list_of_spheres.append(s1)

	# Initialize Pixels in Canvas
	canvas_width = 100
	canvas_height = 100
	width_scale = 0.01
	height_scale = 0.01
	canvas_empty_pixel = [0,0,0]
	canvas_pixel_list = []
	for x in range(0,canvas_width):
		for y in range(0,canvas_height):
			canvas_pixel_list.append(Pixel(x,y,False,canvas_empty_pixel))

	# Trace Pixels in Canvas
	for pixel in canvas_pixel_list:
		x,y,d = Canvas_to_Viewport(pixel.x,pixel.y,width_scale,height_scale)
		color = TraceRay(o,x,y,d,t_min,t_max,list_of_spheres,BACKGROUND_COLOR)
		pixel.rgb = color
		list_of_colors.extend(color)

	# Plot to Image
	list_of_colors = bytes(list_of_colors)
	img = Image.frombytes('RGB',(canvas_width,canvas_height),list_of_colors)
	img.show()
	img.save('test.png')

	# Coordinate Calculator len(list)%width = y len(list)-len(list)%width
if __name__ == "__main__":
	Main()
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
