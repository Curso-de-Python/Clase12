'''
-----------------------------
 EJERCICIO N°2
 Diagramas de barras e histogramas
-----------------------------
'''
import matplotlib.pyplot as plt

x1 = [2,4,6,8,10]
y1 = [3,5,1,7,4]
#x2 = [1,3,5,7,9]
#y2 = [1,3,2,4,9]

# EJEMPLO 1
#plt.bar(x1,y1,label='Barra 1')  # Características

# EJEMPLO 2
plt.bar(x1,y1,label='Barra 1',color='r')  # Cambia el color
#plt.bar(x2,y2,label='Barra 2',color='g')

plt.xlabel('Eje X')
plt.ylabel('Eje Y')
plt.title('Grafica de barras')
plt.legend()

plt.show()

'''
# ---------------------------
# EJEMPLO 3: Histograma
edad_hombres=[2,3,4,5,1,2,4,5,14,25,12,56,34,22,78,65,77,90,5,22,33,55,44,66,22,34,13,5,33,56,88,95,75]
edad_mujeres=[77,66,55,44,33,22,11,22,2,42,21,63,6,99,88,66,13,42,35,38,47,54,34,39,78,27,73,26,3,4,5,1]
edades=[0,10,20,30,40,50,60,70,80,90,100]

plt.hist(edad_hombres,edades,histtype='bar',rwidth=0.8,color='b',label='hombres')
plt.hist(edad_mujeres,edades,histtype='bar',rwidth=0.4,color='r',label='mujeres')

plt.xlabel('Eje X: Edades')
plt.ylabel('Eje Y: Poblacion')
plt.title('Histograma')
plt.legend()

plt.show()
'''