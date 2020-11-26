'''
-----------------------------
 EJERCICIO N°4
 Diagramas de apilamiento
-----------------------------
'''
import matplotlib.pyplot as plt

# ---------------------------
# EJEMPLO 1
meses= [x for x in range(1,13)]

hipoteca= [700, 700, 700,
           800, 800, 800,
           850, 850, 850,
           850, 850, 850]

servicios= [500, 300, 380,
           200, 600, 550,
           310, 620, 290,
           320, 440, 400]

reparaciones= [100, 120, 100,
          150, 850, 80,
          120, 220, 240,
          50, 60, 150]

plt.plot([],[], color='blue', label='hipoteca')
plt.plot([],[], color='orange', label='servicios')
plt.plot([],[], color='brown', label='reparaciones')

plt.stackplot(meses, hipoteca, servicios, reparaciones, colors=['blue', 'orange', 'brown'])

plt.legend()
plt.title('Gastos de la casa')
plt.xlabel('Meses del año')
plt.ylabel('Costo')

plt.show()

'''
# ---------------------------
# EJEMPLO 2
dias=['dom','lun','mar','mie','jue','vie','sab']

#tiempo empleado en horas:
dormir=[9,6,7,6,7,6,8]
comer=[3,1,1.30,1,1.30,2,3]
trabajar=[2,10,9,8,9,8,0]
jugar=[8,2,3,2,3,2,9]

plt.plot([],[], color='blue', label='dormir')
plt.plot([],[], color='orange', label='comer')
plt.plot([],[], color='brown', label='trabajar')
plt.plot([],[], color='red', label='jugar')

plt.stackplot(dias, dormir, comer, trabajar, jugar)
plt.legend()

plt.title('Apilamiento de actividades en la semana')
plt.xlabel('dias')
plt.ylabel('tiempo en horas')
plt.show()
'''
