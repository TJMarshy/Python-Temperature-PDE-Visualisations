from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
''' Temperature distrobution of Boiling potato'''

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

a=3
temp = 0
T_0 = 20
T_1 = 100

r = np.linspace(0.1,a,100)
t = np.linspace(0,5,100)
R,T = np.meshgrid(r,t)

for n in range(1,100):
    temp += (2*a*(T_0-T_1))/(n*np.pi*R)*(((-1)**n)*np.sin((n*np.pi*R)/a))*np.exp((((n*np.pi)/a)**2)*(-T))
Tem = T_1 - temp
ax.plot_surface(R,T,Tem, cmap=plt.cm.viridis)
#ax.plot_wireframe(R,T,Tem, rcount= 20, ccount =20)
ax.set_xlabel('r')
ax.set_ylabel('time')
ax.set_zlabel('temperature')



plt.show()