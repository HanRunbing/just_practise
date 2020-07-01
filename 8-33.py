# _*_ coding:utf-8 _*_
# 开发人员：兰天
# 开发时间:2020/6/28 19:21
# 文件名称：meicuihua.py
# 开发工具：PyCharm

import numpy as np
import matplotlib.pyplot as plt

print('运行开始')
h = 0.0001   # 步长
E = 1    # E的当前浓度
S = 1000    # S的当前浓度
allE = []   # E的浓度变化数列
allE.append(E)
allS = []
allS.append(S)   # S的浓度变化数列
time = 1

while(S > 1):   # 在有限的时间内，S是无法消耗完全的，故不能为0
    time = time + 1   # 记录迭代次数
    Enow = E     # 暂时存放当前E，后面S计算需要用一下
    k1 = 750 * (1 - E) - 100 * S * E
    k2 = 750 * (1 - (E + k1 * h / 3)) - 100 * S * (E + k1 * h / 3)
    k3 = 750 * (1 - (E + k1 * h / 3 + k2 * h / 3)) - 100 * S * (E + k1 * h / 3 + k2 * h / 3)
    k4 = 750 * (1 - (E + k1 * h / 3 + k2 * h / 3 + k3 * h / 3)) - 100 * S * (E + k1 * h / 3 + k2 * h / 3 + k3 * h / 3)
    E = E + h * (k1 + 2 * k2 + 2 * k3 + k4) / 6   # 更新E
    allE.append(E)

    k1 = 600 * (1 - Enow) - 100 * Enow * S
    k2 = 600 * (1 - Enow) - 100 * Enow * (S + k1 * h / 3)
    k3 = 600 * (1 - Enow) - 100 * Enow * (S + k1 * h / 3 + k2 * h / 3)
    k4 = 600 * (1 - Enow) - 100 * Enow * (S + k1 * h / 3 + k2 * h / 3 + k3 * h / 3)
    S = S + h * (k1 + 2 * k2 + 2 * k3 + k4) / 6   # 更新S
    allS.append(S)

def concentration_P(S,ES):
    P=[]
    for i in range(1786):
        p = 10 - S[i] - ES[i]
        P.append(p)
    return P
def concentration_ES(E):
    ES=[]
    for e in E:
        es = 1 - e
        ES.append(es)
    return ES
def Rate_E(ES,E,S):
    R_E=[]
    for i in range(1786):
        re = ES[i] * 750 - 100 * E[i] * S[i]
        R_E.append(re)
    return R_E
def Rate_S(ES,E,S):
    R_S=[]
    for i in range(1786):
        rs = ES[i] * 600 - 100 * E[i] * S[i]
        R_S.append(rs)
    return R_S
def Rate_ES(ES,E,S):
    R_ES=[]
    for i in range(1786):
        res = E[i] * S[i] * 100 - ES[i] * 750
        R_ES.append(res)
    return R_ES
def Rate_P(ES):
    R_P=[]
    for i in range(1786):
        p = ES[i] * 150
        R_P.append(p)
    return R_P

allES = concentration_ES(allE)
allP = concentration_P(allS,allES)
R_E = Rate_E(allES,allE,allS)
R_S = Rate_S(allES,allE,allS)
R_ES = Rate_ES(allES,allE,allS)
R_P = Rate_P(allES)

plt.figure(1)
plt.title("S")
plt.xlabel("t", size=14)
plt.ylabel("S", size=14)
t = np.array([t for t in range(0,time)])
fitness = np.array(R_E)
plt.plot(t, fitness, color='r', linewidth=3)
plt.show()
