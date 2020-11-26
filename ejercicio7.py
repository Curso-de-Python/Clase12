'''
-----------------------------
 EJERCICIO N°7
 Gráficas en 3D
-----------------------------
'''
from mpl_toolkits.mplot3d import Axes3D
import numpy as np   # Cómputos científicos en Python
import matplotlib
import matplotlib.pyplot as plt
'''
fig = plt.figure()
ax = Axes3D(fig)

x = [6,3,6,9,12,24]
y = [3,5,78,12,23,56]

# ---------------------------
# EJEMPLO 1
ax.plot(x, y, zs=0, zdir='x', label='zs=0, zdir=z')
ax.set_xlabel('Eje X')  # Si cambias zdir las etiquetas no se actualizan
ax.set_ylabel('Eje Y')
ax.set_zlabel('Eje Z')
plt.show()


# ---------------------------
# EJEMPLO 2
# Se colocan 0's en el eje y, y el eje y se pasa al ejex
ax.plot(xs=x, ys=[0]*len(x), zs=y, zdir='z', label='ys=0, zdir=z')
plt.show()

# ---------------------------
# EJEMPLO 3
N = 100
r0 = 0.6
x = 0.9 * np.random.rand(N)
y = 0.9 * np.random.rand(N)
area = (20 * np.random.rand(N))**2 
c = np.sqrt(area)
r = np.sqrt(x ** 2 + y ** 2)
area1 = np.ma.masked_where(r < r0, area)
area2 = np.ma.masked_where(r >= r0, area)
plt.scatter(x, y, s=area1, marker='^', c=c)
plt.scatter(x, y, s=area2, marker='o', c=c)

# Muestra el límte entre las regiones:
theta = np.arange(0, np.pi / 2, 0.01)
plt.plot(r0 * np.cos(theta), r0 * np.sin(theta))

plt.show()
'''
# ---------------------------
# EJEMPLO 4
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
from matplotlib import cm

fig = plt.figure()
ax = fig.gca(projection='3d')
X, Y, Z = axes3d.get_test_data(0.05)

# Grafica la superficie 3D
ax.plot_surface(X, Y, Z, rstride=8, cstride=8, alpha=0.3)

# Grafica las proyecciones de los contornos para cada dimensión
# Si se elige como offset los límites de los ejes, las
# proyecciones aparecerán "sobre las paredes" de la gráfica
cset = ax.contourf(X, Y, Z, zdir='z', offset=-100, cmap=cm.coolwarm)
cset = ax.contourf(X, Y, Z, zdir='x', offset=-40, cmap=cm.coolwarm)
cset = ax.contourf(X, Y, Z, zdir='y', offset=40, cmap=cm.coolwarm)

ax.set_xlim(-40, 40)
ax.set_ylim(-40, 40)
ax.set_zlim(-100, 100)

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.show()
