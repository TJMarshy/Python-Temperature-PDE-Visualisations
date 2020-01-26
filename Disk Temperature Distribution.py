from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 unused import

import matplotlib.pyplot as plt
import numpy as np
'''
Temperature Distribution of Flat disk of one half at T0 and other at -T0 at r = a

'''

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

a = 3
T_0 = 1
# Create the mesh in polar coordinates and compute corresponding Z.
r = np.linspace(0, a, 20)
p = np.linspace(0, 2*np.pi, 20)
R, P = np.meshgrid(r, p)
Z = 0
for n in range(100):
    Z += ((4*T_0)/(((a**(2*n+1))*(2*n+1)*np.pi)))*np.sin((2*n + 1)*P)*R**(2*n+1)
Z += 1

# Express the mesh in the cartesian system.
X, Y = R*np.cos(P), R*np.sin(P)

# Plot the surface.
ax.plot_surface(X, Y, Z, cmap='viridis')
#ax.plot_wireframe(X, Y, Z, rcount = 20, ccount = 20)
#ax.plot(X,Y,1)

# Tweak the limits and add latex math labels.

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('Temperature Distribution Of a Disk')

for angle in np.linspace(0,360,360):
    ax.view_init(30,angle)
    plt.draw()
    plt.pause(0.001)