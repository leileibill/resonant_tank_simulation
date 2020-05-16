import numpy as np
from scipy import signal
import matplotlib.pyplot as plt
from scipy.integrate import odeint



L = 20e-6
freq = 10e3

# Inductor
def inductor(iL0, v, dt=1e-6):
    iL = iL0 + v/L * dt
    return iL

dt = 1e-6
t_total = 1e-3
num = int(t_total/dt)

dt_range = [dt] * num
t_range = np.cumsum(dt_range)

y = [0] * num
x = signal.square(t_range * 2 * np.pi * freq)*10

vL = x
for index in range(1, len(dt_range)):
    y[index] = inductor(y[index - 1], vL[index], dt)

iL = y


plt.figure(1)
plt.plot(t_range, x,'r-',linewidth=1,label='ODE Integrator')
plt.plot(t_range, iL,'r-',linewidth=1,label='ODE Integrator')
plt.xlabel('Time')
plt.ylabel('Response (y)')
plt.legend(loc='best')
plt.savefig('2nd_order.png')
plt.show()