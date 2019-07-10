
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