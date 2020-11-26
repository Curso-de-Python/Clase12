'''
-----------------------------
 EJERCICIO N°1
 Gráficas lineales
-----------------------------
'''
import matplotlib.pyplot as plt
x = [1,2,3]
y = [5,7,4]

# ---------------------------
# EJEMPLO 1
plt.plot(x,y)
plt.show()

'''
# ---------------------------
# EJEMPLO 2
plt.plot(x,y)
plt.xlabel('Eje X')     # Etiquetas a los ejes
plt.ylabel('Eje Y')
plt.title('Grafica lineal')   # Título

plt.show()

# ---------------------------
# EJEMPLO 3
x2 = [1,2,3]    # Agrego otra gráfica
y2 = [7,5,6]

plt.plot(x1,y1,label='Tipo 1')    # Títulos individuales
plt.plot(x2,y2,label='Tipo 2')

plt.xlabel('Eje X')
plt.ylabel('Eje Y')
plt.title('Grafica lineal')   # Título general
plt.legend()    # Leyenda

plt.show()
'''