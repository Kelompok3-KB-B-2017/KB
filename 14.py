from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np


fig = plt.figure()
ax = fig.gca(projection='3d')

# Make data.
X = np.arange(-2,2 , 0.01)
Y = np.arange(-2,2, 0.01)
X, Y = np.meshgrid(X, Y)
#https://en.wikipedia.org/wiki/Rosenbrock_function
Z =(1+(x+y+1)**2 *(19-14*x + 3*x**2-14*y+6*x*y+3*y**2)) *
    (30+(2*x-3*y)**2 * (18-32*x+12*x**2+48*y-36*x*y+27*y**2))
# Plot the surface.
surf = ax.plot_surface(X, Y, Z, cmap=cm.gist_stern,
                       linewidth=0, antialiased=False)

# Customize the z axis.
#ax.set_zlim(-1.01, 1.01)
ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

# Add a color bar which maps values to colors.
fig.colorbar(surf, shrink=0.5, aspect=5)

plt.show()


