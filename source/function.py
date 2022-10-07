"""function for Assignment #1 to calculate arcsin(x)"""

# import libraries
import numpy as np

# create function for calculating inverse sine

def arcsin(x):
	"""
	calculate inverse sine of an input value
	
	Parameters
	----------
	x : number (value for which arcsine(x) will be calulated)

	Returns
	----------
	val : the value of arcsine(x)

	"""
	# test for if input value is zero
	if x == 0:
		return(0)
	# initialising variables
	n = 1	
	result = 0 
	fact_n = 1
	fact_2n = 2
	eps_s = 0.5*(10**-5) # precision of 5 significant digits required
	eps_a = 1
	
	# while loop to set up iterative processes to calculate values of arcsin(x), stopping criteria set to return value when 5 significant digits of precision reached
	while eps_a > eps_s:
		term = ((2*x)**(2*n)) / ((n**2)*((fact_2n)/((fact_n)**2)))	# formula to calculate inverse of sine
		# changing variables for next iteration if stopping criteria is not met
		result += term
		n += 1
		fact_n *= n 
		fact_2n *= (n*2)*((2*n)-1)
		eps_a = np.abs(term/result)	# eps_a calculated using eps_a = (fn+1 - fn)/fn+1
	val = np.sqrt(0.5*result)
	return(val)
      
# tests to calculate arcsin(x) values over range of values
x = [0,0.1,0.5,0.9,1]
y = []
for i in x:
	val = arcsin(i)
	y.append(val)
print(y)

