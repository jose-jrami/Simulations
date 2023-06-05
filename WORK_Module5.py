
import math as m
import numpy as np
import scipy.integrate as integrate
import matplotlib.pyplot as plt

# Constants and integram upper and lower limits
k = 9*10**9 # proportinality constant k
a = 1*10**-12 # Upperlimit distance a
b = 7*10**-12 # Lower limit distance b
Q1 = 1.6*10**-19 # Charge value

# Define work eqaution
X = lambda x: (k*Q1**2)/(x**2)

# Calcualte answer trough integral of the weok eqaution
ans = integrate.quad(X, a, b)

# Print the answer to the terminal
print("Work = ", ans[0])
