"""function for Assignment #1 to calculate launch angle range"""

import numpy as np

from tests import launch_angle_tests

def launch_angle_range(ve_v0,alpha,tol_alpha):
	"""
	function to calculate launch angle range of launch vehicle
	
	Parameters
	----------
	ve_vo : ratio of velocities, (escape velocity)/(initial velocity)
	alpha : desired maximum altitude as a fraction of Earth's radius
	alpha_tol : tolerance of alpha

	Returns
	----------
	phi_range : array of launch angles, containing 2 values, minimum launch and maximum launch angle

	"""
	# create empty array
	phi_range = []

	# calculate maximum and minimum altitide using alpha and tol_alpha
	max_alt = ((1 + tol_alpha)*alpha)
	min_alt = ((1 - tol_alpha)*alpha)
	
    	# calculate minimum phi using maximum alpha
	min_phi = launch_angle_tests(ve_v0, max_alt)
	phi_range.append(min_phi) # append value to array
	# calculate maximum phi using minimum alpha
	max_phi = launch_angle_tests(ve_v0, min_alt)
	phi_range.append(max_phi) # append value to array
    
	return(phi_range)

# tests for function
x = 2
y = 0.25
tol = 0.02
c = launch_angle_range(x,y,tol)
print(c)
