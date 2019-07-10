from PIL import Image

import numpy as np
import math
import operator

# Self Modules
import color

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

class Light:
	def __init__(self, type, intensity, position, direction):
		self.type = type
		self.intensity = intensity
		self.position = position
		self.direction = direction

# Canvas Pixel to Viewport
def Canvas_to_Viewport(x,y,width_scale,height_scale):
	x = x * width_scale
	y = y * height_scale
	# d is basically the z and distance to the viewport from canvas in z space
	d = 1
	return x,y,d

# Tracing Ray (Computes intersection of ray with every sphere and return color of sphere at nearest intersection.)
def TraceRay(o,x,y,d,t_min,t_max,list_of_spheres,list_of_lights,BACKGROUND_COLOR):
	closest_t = float('inf')
	closest_sphere = None
	for sphere in list_of_spheres:
		t1,t2 = SolveIntersect(x,y,d,o,sphere)
		t1 = -t1
		t2 = -t2
		if (t_min < t1 < t_max) and (t1 < closest_t):
			closest_t = t1
			closest_sphere = sphere
		if (t_min < t2 < t_max) and (t2 < closest_t):
			closest_t = t2
			closest_sphere = sphere
	if closest_sphere is None:
		#print("Pixel " + str(x) + "," + str(y) + " is background.")
		return BACKGROUND_COLOR
	# Lighting
	D = [x,y,d]
	p = list(map(operator.add,o,[coord*closest_t for coord in D])) # Intersection
	n = list(map(operator.sub,p,closest_sphere.center)) # Normal
	n = [coord/(math.sqrt(n[0]**2 + n[1]**2 + n[2]**2)) for coord in n] # n / length of n
	#print("T1 and T2 is:",T1,T2)
	#print("Pixel" + str(x) + "," + str(y) + " is sphere.")
	return [round(channel*ComputeLighting(p,n,list_of_lights)) for channel in closest_sphere.color]

# Ax * Bx + Ay * By + Az * Bz
# Solve Quadratic Eqn
def SolveIntersect(x,y,d,o,sphere):
	c = sphere.center
	r = sphere.radius
	#o = o - c
	o = list(map(operator.sub,c,o))
	oc = o
	k1 = (x*x) + (y*y) + (d*d)
	k2 = 2 * ((oc[0]*x) + (oc[1]*y) + (oc[2]*d))
	k3 = ((oc[0]*oc[0]) + (oc[1]*oc[1]) + (oc[2]*oc[2])) - (r*r)
	discriminant = (k2*k2) - (4*k1*k3)
	if discriminant < 0:
		return np.inf,np.inf
	if k1 == 0:
		t1 = 0
		t2 = 0
	else:
		t1 = ((-k2) + math.sqrt(discriminant)) / (2*k1)
		t2 = ((-k2) - math.sqrt(discriminant)) / (2*k1)
	return t1,t2

def ComputeLighting(p,n,list_of_lights):
	i = 0.0
	for light in list_of_lights:
		if light.type == 'ambient':
			i+=light.intensity
		else:
			if light.type == 'point':
				l = list(map(operator.sub,p,light.position))
			elif light.type == 'directional':
				l = light.direction
			n_dot_l = (n[0]*l[0]) + (n[1]*l[1]) + (n[2]*l[2])
			if n_dot_l > 0:
				i += (light.intensity*n_dot_l)/((math.sqrt(n[0]**2 + n[1]**2 + n[2]**2))*(math.sqrt(l[0]**2 + l[1]**2 + l[2]**2)))
	return i

# Create Spheres in Main
def Main():

	# Need to Dot Product o
	o = [0,0,0]
	BACKGROUND_COLOR = [255,255,255]
	t_min = 1
	t_max = np.inf
	list_of_colors = []

	# List of Spheres
	list_of_spheres = []
	s1 = Sphere([0,-1,3],2,[255,0,0])
	s2 = Sphere([2,0,4],2,[0,0,255])
	s3 = Sphere([-2,0,4],2,[0,255,0])
	s4 = Sphere([0,-5001,0],5000,[255,255,0])
	list_of_spheres.extend((s1,s2,s3,s4))

	# Initialize Lights in Scene (Less than 1.0 Intensity as Eqn does not allow)
	list_of_lights = []
	l1 = Light('ambient',0.2,None,None)
	l2 = Light('point',0.6,[2,1,0],None)
	l3 = Light('directional',0.2,None,[1,4,4])
	list_of_lights.extend((l1,l2,l3))

	# Initialize Pixels in Canvas
	canvas_width = 500
	canvas_height = 500
	width_scale = 0.01
	height_scale = 0.01
	canvas_empty_pixel = [0,0,0]
	canvas_pixel_list = []
	for x in range(int(-canvas_width/2),int(canvas_width/2)):
		for y in range(int(-canvas_height/2),int(canvas_height/2)):
			canvas_pixel_list.append(Pixel(x,y,False,canvas_empty_pixel))

	# Trace Pixels in Canvas
	for pixel in canvas_pixel_list:
		x,y,d = Canvas_to_Viewport(pixel.x,pixel.y,width_scale,height_scale)
		color = TraceRay(o,x,y,d,t_min,t_max,list_of_spheres,list_of_lights,BACKGROUND_COLOR)
		pixel.rgb = color
		list_of_colors.extend(color)

	# Plot to Image
	print(list_of_colors)
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
