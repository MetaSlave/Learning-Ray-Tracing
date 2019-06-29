import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

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
def Canvas_to_Viewport(canvas_array,width_scale,height_scale):
	new_canvas_array = []
	for row in canvas_array:
		for pixel in row:

# Tracing Ray (Computes intersection of ray with every sphere and return color of sphere at nearest intersection.)


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

