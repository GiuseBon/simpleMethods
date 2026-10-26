import math
import numpy
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm

#we want to plot a vector field. goal of project to plot a vector field and see the trajectory of a particle under those forces
#do we want to do it by hand?
import numpy as np
import matplotlib.pyplot as plt

# 1. Define a grid of points
x = np.linspace(-2, 2, 50)
y = np.linspace(-2, 2, 50)
X, Y = np.meshgrid(x, y)

# 2. Define the vector components (U = dx/dt, V = dy/dt)
G = 1 #gravitational constant
m1 = 1 #mass 1
m2 = 1 #mass 2
R = np.sqrt(X**2 + Y**2)#Radius
R[R == 0] = np.nan
U = -X/(R**3) #put small nudge for non 1/0 error
V = -Y/(R**3) #put small nudge for non 1/0 error
# when plotting 
# 3. Calculate magnitude for coloring
magnitude = np.sqrt(U**2 + V**2)
U_norm = U/magnitude
V_norm = V/magnitude
# 4. Create the vector field plot
plt.figure(figsize=(8, 6))
Q = plt.quiver(X, Y, U_norm, V_norm, magnitude, cmap='inferno',norm=LogNorm(vmin=np.nanmin(magnitude), vmax=np.nanmax(magnitude)),pivot='middle')
plt.plot(0, 0, 'wo', markersize=10, markeredgecolor='black', label='Mass $M$')

# Add labels, title, and colorbar
plt.colorbar(Q, label='Vector Magnitude')
plt.title('2D Vector Field: $\mathbf{V}(x, y) = (-x/r^3, -y/r^3)$')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid(True)
plt.axis('equal')

plt.show()