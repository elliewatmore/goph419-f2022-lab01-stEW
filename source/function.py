"""function for Assignment #1 to calculate arcsin(x)"""

import numpy

x = 1

def arcsin(x):
	""" function to calculate arcsin(x)
	    parameters:
	    x = angle in degrees
	    returns:
	    y = calulated value of arcsin(x)
	"""
	y = numpy.arcsin(x)
	return y

y = arcsin(x)
print(y)