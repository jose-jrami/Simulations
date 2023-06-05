
import math as m
import numpy as np
import scipy.integrate as integrate
import matplotlib.pyplot as plt

def rlc(P, t):
    a = 2/3     # 3 patients per 2 nurses per hour
    b = 2       # 2 patients per 1 ventilator per hour
    c = 2/10    # 10 patients per 2 rooms per hour if no longer criticall (Monintorting)
    d = 4/2     # 4 patients released per 2 patients still sick per hour (constant)
    e = 3/2     # 3 patients not sick (released at ER unit) per 2 patients critically sick

    N = 13    # Number of nurses available at ICU
    V = 5   # Number of ventilators available at ICU
    R = 4   # NUmber of rooms avialable for condition monitoring


    # ER_IN = constant number of patien flwoing into ER per hour
    # ER_OUT = patient tranfered to the ICU minus not criticall patients released
    # ICU_IN = patients tranfered in from the ER that are crically sick according
    # ICU_OUT = patients released or tranfered to health unit (Outside of ICU) after stablized health
    ER_IN = 50
    ER_OUT = a*(1/N)*P[0] + b*(1/V)*P[0] + e*P[0]
    ICU_IN = a*(1/N)*P[0] + b*(1/V)*P[0]
    ICU_OUT = c*(1/R)*P[1] + d*P[1]

    # dpdt1 = Rate of change in the ER unit (ER_IN - ER_OUT)
    # dPdt2 = Rate of change in the ICU (ICU_IN - ICU_OUT)
    dPdt1 = (ER_IN - ER_OUT)
    dPdt2 = (ICU_IN - ICU_OUT)

    # ER Unit Cqpcity met when ER unit passes 100 patients
    if P[0]>=100 and dPdt1>=0:
        dPdt1 = 0
    # ICU Unit Capacity met when ICU pases 50 patients
    if P[1]>=50 and dPdt2>=0:
        dPdt2 = 0
    # Retrun Differential equations
    return [dPdt1, dPdt2]

# Time input range
tsamp = np.linspace(0, 12, 1000)

# resulting integration according to time input
ans = integrate.odeint(rlc, [0, 0], tsamp).T


plt.plot(tsamp,ans[0], 'b-')
plt.plot(tsamp,ans[1], 'r--')
plt.xlabel('Time (hrs)')
plt.ylabel('Pateints (p)')
plt.legend(['ERU','ICU'])
plt.show()
