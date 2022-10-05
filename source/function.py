"""function for Assignment #1 to calculate arcsin(x)"""


import numpy as np

def arcsin(x):
	"""
	"""
	n = 1
	result = 0 
	fact_n = 1
	fact_2n = 2
	eps_s = 0.5*(10**-5)
	eps_a = 1
	while eps_a > eps_s:
		term = ((2*x)**(2*n)) / ((n**2)*((fact_2n)/((fact_n)**2)))
		result += term
		n += 1
		fact_n *= n 
		fact_2n *= (n*2)*((2*n)-1)
		eps_a = np.abs(term/result)
	val = np.sqrt(0.5*result)
	return(val)
      

x = 1
y = arcsin(x)
print(y)

