
import math as m
import numpy as np
import scipy.integrate as integrate
import matplotlib.pyplot as plt


# delta = 50ms
d = 50

# Define HIC function.
# Reference: https://www.intmath.com/applications-integration/hic-part2.php
X = lambda x, a: (1/a)*(22000/((x - 74)**2 + 500))

# Define empty list for HIC50 and count
HIC50 = []
count = []

# Loop to evaluate integral according to the delta (d) from 0ms - 160ms
# function appends the list HIC50 to generate curve which is used to extract HIC value
for i in range(0,160):
    ans = integrate.quad(X, i, i + d, args=(d,))
    HIC50.append(ans[0])
    count.append(i)

# Raise each value in the list HIC to the 2.5 Power and multiply times the delta d in milliseconds
# https://www.intmath.com/applications-integration/hic-part2.php
Y = ((np.array(HIC50))**2.5)*d*10**-3


# Plot the curve and print the maximum value on the terminal and show HIC Value on Plot
max = np.max(Y)
display = "HIC Value =" + str(max)
print(display)
plt.plot(count, Y)
plt.xlabel("Time (ms)")
plt.ylabel("HIC50")
plt.ylim(0, 800)
plt.legend([display])
plt.show()
