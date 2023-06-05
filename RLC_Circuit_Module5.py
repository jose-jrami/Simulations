

import math as m
import numpy as np
import scipy.integrate as integrate
import matplotlib.pyplot as plt

# Define RLC Function for Differential equation for the voltage of a cacitor C
def rlc(A, t):
    R = 2
    R2 = 100
    V = 1
    C = 10*10**-6
    L = 1*10**-3
    Vc, x = A
    return [x, 1/(L*C)*V -x*(2*C +L/R2)/(L*C) - Vc*(1 + R/R2)/(L*C)]

# time sample from 0 to 6 milliseconds
tsamp = np.linspace(0, 0.6e-2,1001)

# integrate the function with initial paramteres or conditions of [0, 0]
vc, x = integrate.odeint(rlc, [0, 0], tsamp).T

# Plot the equation
plt.plot(tsamp,vc)
plt.xlabel('t')
plt.ylabel('Vc')
plt.show()
