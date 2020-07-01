# _*_ coding:utf-8 _*_

import numpy as np
import matplotlib.pyplot as plt
#Matplotlib is a Python 2D drawing library
h = 0.0001   # step
E = 1    # E0
S = 1000    # S0
allE = []   # The series of E
allE.append(E)
allS = []
allS.append(S)   # The change in concentration of S
time = 1

while(S > 1):   # In finite time, S cannot be consumed completely, so it cannot be 0
    time = time + 1   # Number of iterations recorded
    Enow = E     # Temporarily store the current E, later S calculation needs to use
    k1 = 750 * (1 - E) - 100 * S * E
    k2 = 750 * (1 - (E + k1 * h / 3)) - 100 * S * (E + k1 * h / 3)
    k3 = 750 * (1 - (E + k1 * h / 3 + k2 * h / 3)) - 100 * S * (E + k1 * h / 3 + k2 * h / 3)
    k4 = 750 * (1 - (E + k1 * h / 3 + k2 * h / 3 + k3 * h / 3)) - 100 * S * (E + k1 * h / 3 + k2 * h / 3 + k3 * h / 3)
    E = E + h * (k1 + 2 * k2 + 2 * k3 + k4) / 6   # undate E
    allE.append(E)

    k1 = 600 * (1 - Enow) - 100 * Enow * S
    k2 = 600 * (1 - Enow) - 100 * Enow * (S + k1 * h / 3)
    k3 = 600 * (1 - Enow) - 100 * Enow * (S + k1 * h / 3 + k2 * h / 3)
    k4 = 600 * (1 - Enow) - 100 * Enow * (S + k1 * h / 3 + k2 * h / 3 + k3 * h / 3)
    S = S + h * (k1 + 2 * k2 + 2 * k3 + k4) / 6   # undate S
    allS.append(S)


def concentration_ES(E):
    # concentration rate of species ES
    ES=[]
    for e in E:
        es = 1 - e
        ES.append(es)
    return ES
def Rate_P(ES):
    # calculate rate of species P
    R_P=[]
    for es in ES:
        p = es * 150
        R_P.append(p)
    return R_P
# result of four rate of change
allES = concentration_ES(allE)
R_P = Rate_P(allES)

#S的图像a
plt.figure(1)
plt.title("S")
plt.xlabel("t", size=14)
plt.ylabel("S", size=14)
t = np.array([t for t in range(0,time)])
fitness = np.array(R_P)
plt.plot(t, fitness, color='r', linewidth=3)
plt.show()