import matplotlib.pyplot as plt
def runge_kutta_e(y, x, h, f,e_n=0):
    """ y is the initial value for y
        x is the initial value for x
        dx is the time step in x
        f is derivative of function y(t)
    """
    k1 = h * f(y, x,e_n=0)
    k2 = h * f(y + 0.5 * k1, x + 0.5 * h,e_n=0)
    k3 = h * f(y + 0.5 * k2, x + 0.5 * h,e_n=0)
    k4 = h * f(y + k3, x + h,e_n=0)
    return y + (k1 + 2 * k2 + 2 * k3 + k4) / 6

def runge_kutta_s(y, x, h, f,e_n=0):
    """ y is the initial value for y
        x is the initial value for x
        dx is the time step in x
        f is derivative of function y(t)
    """
    k1 = h * f(y, x,e_n=0)
    k2 = h * f(y + 0.5 * k1, x + 0.5 * h,e_n=0)
    k3 = h * f(y + 0.5 * k2, x + 0.5 * h,e_n=0)
    k4 = h * f(y + k3, x + h,e_n=0)
    return y - (k1 + 2 * k2 + 2 * k3 + k4) / 6

def initial_function_E(y_0=1,x_0=0,e_n=0):
    y_1 = 750 - 1750 * y_0 #y_1=(600+100)*(1-y)-100*10*y  Cs=Cs0
    return y_1

def function_E(y_n,x_n,e_n):#the real parameter is s_n
    y_n_1 = 750 * (1-y_n) - 100 * e_n * y_n
    return y_n_1
def function_S(y_n,x_n,e_n):
    y_n_1 = 600 * (1 - e_n) - 100 * e_n * y_n
    return y_n_1
def funciton_P(E):
    P=[]
    for e in E:
        p = (1 - e)*150
        P.append(p)
    return P
def funciton_ES(E,S):
    ES=[]
    for i in range(167):
        es = E[i] * S[i] - (1-E[i])*750
        ES.append(es)
    return ES
E,S,YE,YS=[1],[10],[],[]
e_1=runge_kutta_e(1,0,0.0001,initial_function_E)
y_e=initial_function_E(1,0)
s_1=runge_kutta_s(10,0,0.0001,function_S,e_1)
y_s=function_S(10,0,e_1)
YE.append(y_e)
YS.append(y_s)
E.append(e_1)
S.append(s_1)

while(s_1 > 0):
    e_next=runge_kutta_e(e_1,0,0.0001,function_E,s_1)
    # y_e = function_E(e_1, 0,s_1)
    s_next=runge_kutta_s(s_1,0,0.0001,function_S,e_next)
    # y_s=function_S(s_1,0,e_next)
    # YE.append(y_e)
    # YS.append(y_s)
    E.append(e_next)
    S.append(s_next)
    e_1 = e_next
    s_1 = s_next
E.pop(-1)
S.pop(-1)

ES=funciton_ES(E,S)
P=funciton_P(E)
print(YE)
print(YS)

plt.figure(20)
plt.subplot(221)
plt.plot(YE)
plt.title('YE')
plt.subplot(222)
plt.plot(YS)
plt.title('YS')
plt.show()

# plt.figure(20)
# plt.subplot(221)
# plt.plot(E)
# plt.title('CE')
# plt.subplot(222)
# plt.plot(S)
# plt.title('CS')
# plt.show()


