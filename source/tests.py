"""edited version of launch_angle to implement tests"""

# import libraries
import numpy as np 

# import arcsin function
from function import arcsin

def launch_angle_tests(ve_v0, alpha):
	"""
	implementing tests using my launch_angle function

	Parameters
	----------
	ve_v0 : velocity ratio (escape velocity)/(initial velocity)
	alpha : desired maximum altitude

	Returns
	----------
	y : launch angle 

	"""
	# calculate value under bracket in equation (17)
	a = (1-((alpha/(1+alpha))*(ve_v0)**2))
	# test for if a is negative 
	if a < 0:
        	return("test failed") # if test failed exit function
	else:
		sinphi = (1 + alpha) * (np.sqrt(a)) # calculate value of sinphi
		# test for if sinphi is greater than 1
		if sinphi > 1:
            		return("test failed") # if test failed exit function
		# if tests pass return value for launch angle using arcsin function
		else:
            		y = arcsin(sinphi)
            		return y
	
    


# test for if value under square root is negative 
a = 7
b = 0.25
c = launch_angle_tests(a, b)
print(c)

# test for if value to calculate arcsin from is greater than 1
a = 7
b = - 0.25
d = launch_angle_tests(a, b)
print(d)
