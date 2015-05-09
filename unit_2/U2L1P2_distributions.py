# Link: https://courses.thinkful.com/data-001v2/assignment/2.1.2
# Following along with the course examples, no feedback needed

import matplotlib.pyplot as plt
import numpy as np
import matplotlib.mlab as mlab

mean = 1  # where the hill is centered
variance = 100
sigma = np.sqrt(variance)
x = np.linspace(-4,5,1000) #left and right max values, number of points to plot
plt.plot(x, mlab.normpdf(x,mean,sigma))

plt.show()