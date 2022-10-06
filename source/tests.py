"""edited version of launch_angle to implement tests"""

import numpy as np 

from function import arcsin

def launch_angle_tests(ve_v0, alpha):
	"""
	"""
	a = (1-((alpha/(1+alpha))*(ve_v0)**2))
	if a < 0:
        	print("test failed")
	else:
		sinphi = (1 + alpha) * (np.sqrt(a))
		if sinphi > 1:
            		print("test failed")
		else:
            		y = arcsin(sinphi)
            		return y
	
    


# test for if value under square root is negative 
a = 7
b = 0.25
c = launch_angle_tests(a, b)
print(c)

a = 7
b = - 0.25
d = launch_angle_tests(a, b)
print(d)
