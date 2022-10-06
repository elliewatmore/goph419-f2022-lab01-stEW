"""function for Assignment #1 to calculate launch angle range"""

import numpy as np

from function2 import launch_angle

def launch_angle_range(ve_v0,alpha,tol_alpha):
	"""
	"""
	phi_range = []
	max_alt = ((1 + tol_alpha)*alpha)
	min_alt = ((1 - tol_alpha)*alpha)
    
	min_phi = launch_angle(ve_v0, max_alt)
	phi_range.append(min_phi)
	max_phi = launch_angle(ve_v0, min_alt)
	phi_range.append(max_phi)
    
	return(phi_range)

x = 2
y = 0.25
tol = 0.02
c = launch_angle_range(x,y,tol)
print(c)
