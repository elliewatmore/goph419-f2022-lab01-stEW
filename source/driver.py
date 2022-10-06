"""Driver script for Assignment #1."""
def main():
	"""Main entry point function."""
	print("Hello, Assignment #1!")

import numpy as np
import matplotlib.pyplot as plt
from launch_angle_range import launch_angle_range

ve_v0 = 2.0
tol_alpha = 0.04
alpha_range = np.arange(0,0.333,0.025)

min_launch_angles = []
max_launch_angles = []


for alpha in alpha_range:                   
    val = launch_angle_range(ve_v0, alpha, tol_alpha)
    min_launch_angles.append(val[0])
    max_launch_angles.append(val[1])
    
    
plt.figure(1)
plt.plot(alpha_range, min_launch_angles, label = 'minimum launch angles')
plt.plot(alpha_range, max_launch_angles, label = 'maximum launch angles')
plt.legend()
plt.xlabel("desired maximum altitude")
plt.ylabel("launch angle")
plt.title("minimum and maximum launch angles for a range of alpha values")
plt.show
plt.savefig("alpha_range.jpg")


ve_v0_range = np.arange(1.8,2.23,0.025)  
tol_alpha = 0.04
alpha = 0.25
print(ve_v0_range)
min_launch_angles = []
max_launch_angles = []


for v in ve_v0_range:                    
    val = launch_angle_range(v, alpha, tol_alpha)
    min_launch_angles.append(val[0])
    max_launch_angles.append(val[1])
    


plt.figure(2)
plt.plot(ve_v0_range, min_launch_angles, label = 'minimum launch angles')
plt.plot(ve_v0_range, max_launch_angles, label = 'maximum launch angles')
plt.legend()
plt.xlabel("ratio of escape velocity to terminal velocity")
plt.ylabel("launch angle")
plt.title("minimum and maximum launch angles for a range of ratios (ve_v0)")
plt.show()
plt.savefig("ve_v0_range.jpg")

if __name__ == "__main__":
	main()