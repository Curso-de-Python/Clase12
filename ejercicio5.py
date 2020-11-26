'''
-----------------------------
 EJERCICIO N°5
 Diagramas circulares
-----------------------------
'''
import matplotlib.pyplot as plt

partes = [7,2,8,5]
actividades = ['dormir','comer','trabajar','jugar']
cols = ['c','y','r','b']

# ---------------------------
# EJEMPLO 1
plt.title('Diagrama circular de actividades en la semana')
plt.xlabel = ('x')
plt.ylabel = ('y')
plt.pie(partes, colors = cols, labels = actividades)
plt.legend()
plt.show()

'''
# ---------------------------
# EJEMPLO 2
plt.pie(partes, colors = cols, labels = actividades, startangle = 90, shadow = True, explode = (0,0,0.1,0))
plt.legend()
plt.show()

# ---------------------------
# EJEMPLO 3
plt.pie(
        partes, 
        colors = cols, 
        labels = actividades, 
        startangle = 90, 
        shadow = True, 
        explode = (0.2,0.2,0.2,-0.1),
        autopct = ('%1.1f%%')
       )
plt.legend()
plt.show()
'''
