pi = 3.14  # global constant

#advanced way to set globals is given here: https://www.programiz.com/python-programming/variables-constants-literals


def area_circle(radius):
	area = pi * radius * radius
	return area 


def volume_sphere(radius):
	volume = 4.0/3.0 * pi * radius**3
	return volume


def volume_cylinder(radius, height):
	area = area_circle (radius)
	volume = area * height
	return volume, area




# now we call the above functions 
#ask the user (exercise)
radius = float(input('Please enter the radius of a circle: '))

area = area_circle(radius)
print(f'{area} is the area in square meters.')

height = float(input('Please enter the height of a cylinder: '))
volume, area = volume_cylinder(radius, height)

print(f'{volume} is the volume  in cubic meters')
print(f'{area} is the area of the top of the cylinder')

radius_sphere = float(input('Please enter the raduius of a sphere: '))
print(f'The volume of the sphere is: {volume_sphere(radius_sphere)}.')


#warm up exercise. Try implementing different functions for the rest 
# of the examples here: https://byjus.com/volume-formulas/

# try to ask the user to input information (such as base, height, radius etc)