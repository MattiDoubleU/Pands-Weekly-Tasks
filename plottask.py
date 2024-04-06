# plottask.py
# Author: Matthias Wiedemann
# As per weekly task 8 this is a program that displays a histogram of a normal distribution of a 1000 values with a mean of 5 and standard deviation of 2, 
# and a plot of the function  h(x)=x3 in the range 0 to 10, on the one set of axes.

# First of all plot libraries numpy and matplotlib.pyplot have to be imported.

import numpy as np
import matplotlib.pyplot as plt

# Second, we need 1000 random values (or an array of 1000 random numbers from a normal Gaussian distribution) 
# with mean of 5 and standard deviation of 2 in normal distribution.
# My research brought to the very Numpy.org documentation:
# https://numpy.org/doc/stable/reference/random/generated/numpy.random.normal.html
# random.normal(loc=0.0, scale=1.0, size=None). The code at the bottom of the page helped me to figure out what value
# goes where in the code parameter.

random = np.random.normal(5, 2, 1000)

# Plot histogram: I looked the code up on: https://www.geeksforgeeks.org/plotting-histogram-in-python-using-matplotlib/
# I used this code initially:
'''
plt.hist(random)  
'''
# Then tried the code as proposed in above link, the result looks much nicer: 

plt.hist(random, bins=30, color='skyblue', edgecolor='black')

# Adding labels and title (I still need to understand the context of the labels)
plt.xlabel('Values')
plt.ylabel('Frequency')
plt.title('Basic Histogram')

# Display the plot
plt.show()

# Plot of the function  h(x)=x3 in the range 0 to 10, on the one set of axes: I am currently doing a bit of research on this.



