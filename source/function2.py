"""function for Assignment #1 to calculate launch angle"""


import numpy 

def launch_angle(ve_v0, alpha):
	""" function to calculate launch angle from the vertical 
	    given the ratio of ve/v0, and alpha
	    
	    Parameters:
	    ve_v0 = ratio of escape velocity over terminal velocity (maximum initial velocity that vehicle
	    reaches shortly after launch)
	    alpha = desired maximum altitude as a fraction of Earth's radius
	    
	    Returns:
	    phi = launch angle from vertical
	"""
	phi = (1 + alpha) * (numpy.sqrt(1-((alpha/(1+alpha))*(ve_v0)**2)))
	return phi

x = 2
y = 0.25
z = launch_angle(x,y)
print(z)