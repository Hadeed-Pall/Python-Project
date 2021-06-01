# Calculating the volume of the given shapes
import math

#function for calculating the voulme of the cube
def volume_cube(cube_length):
    volume = cube_length**3
    return volume
#function for calculating the voulme of the pyramid
def volume_pyramid(pyramid_base, pyramid_height):
    volume = ((pyramid_base**2)*pyramid_height/3)
    return volume
#function for calculating the voulme of the pyramid
def volume_elliposoid(radius_P, radius_T, radius_TH):
    volume = ((4/3)*math.pi)*radius_P*radius_T*radius_TH
    return volume
