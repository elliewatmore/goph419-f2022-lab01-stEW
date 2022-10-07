"""Driver script for Assignment #1."""
def main():
	"""Main entry point function."""
	print("Hello, Assignment #1!")

# import libraries
import numpy as np
import matplotlib.pyplot as plt
# import my launch_angle_range function
from launch_angle_range import launch_angle_range

# set values for velocity ratio and tolerance of alpha to be held at
ve_v0 = 2.0
tol_alpha = 0.04
# create range of alpha values using bounds previously calculated and appropriate spacing
alpha_range = np.arange(0,0.333,0.025)

# create empty array for minimum and maximum launch angles
min_launch_angles = []
max_launch_angles = []

# for loop to calculate minimum and maximum launch angles over alpha range
for alpha in alpha_range:                   
    val = launch_angle_range(ve_v0, alpha, tol_alpha)
    min_launch_angles.append(val[0]) # append value to array for minimum launch angles
    max_launch_angles.append(val[1]) # append value to array for maximum launch angles
    
# plot figure    
plt.figure(1)
plt.plot(alpha_range, min_launch_angles, label = 'minimum launch angles')
plt.plot(alpha_range, max_launch_angles, label = 'maximum launch angles')
plt.legend()
plt.xlabel("desired maximum altitude")
plt.ylabel("launch angle")
plt.title("minimum and maximum launch angles for a range of alpha values")
plt.savefig("Graphs of launch angles for range velocity ratios") # save figure


# create range of velocity ratio values using bounds previously calculated and appropriate spacing
ve_v0_range = np.arange(1.34,2.23,0.025)  
# set values for alpha and its tolerance to be held at
tol_alpha = 0.04
alpha = 0.25

# create empty array for minimum and maximum launch angles
min_launch_angles = []
max_launch_angles = []

# for loop to calculate minimum and maximum launch angles over velocity ratio range
for v in ve_v0_range:                    
    val = launch_angle_range(v, alpha, tol_alpha)
    min_launch_angles.append(val[0]) #  append value to array for minimum launch angles
    max_launch_angles.append(val[1]) #  append value to array for maximum launch angles
    

# plot figure
plt.figure(2)
plt.plot(ve_v0_range, min_launch_angles, label = 'minimum launch angles')
plt.plot(ve_v0_range, max_launch_angles, label = 'maximum launch angles')
plt.legend()
plt.xlabel("ratio of escape velocity to terminal velocity")
plt.ylabel("launch angle")
plt.title("minimum and maximum launch angles for a range of ratios (ve_v0)")
plt.savefig("Graph of launch angles for range of alpha") # save figure




if __name__ == "__main__":
	main()