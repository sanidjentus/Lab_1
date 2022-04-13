from numpy import arange
from scipy.integrate import solve_ivp
from sympy import *

def Сauchy(t, z, E, q):
   x0, x1 = z
   q = q.subs(value, t)
   return [x1, E * x1 + q * x0]

E = -1
value = Symbol('value')
q = sin(value)
print(q)
step = 0.1
t_eval = arange(-0.5, 0.5+step, step)
print(t_eval)
t_span = (-0.5, 0.5)
y0 = [1.0, 2.0]
x = []
for eps in range(0, 10):
    eps *= step
    sol = solve_ivp(Сauchy, t_span=t_span, y0=y0, t_eval=t_eval, args=(eps, q), method='RK45')
    x.append(sol.y)
print("Res X:")
n = 0.0
temp = 0
M = []
for i in x:
    print('X(',n,') = ',i[0])
    n = n + step
    m = 0
    for j in i[0]:
        temp = temp + j
        m = m + 1
    M.append(temp/m)
print("Res M:")
for i in M:
    print(i)