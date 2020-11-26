'''
-----------------------------
 EJERCICIO N°6
 Ploteo de varias gráficas
-----------------------------
'''
import matplotlib.pyplot as plt

data = {'manzana': 10, 'naranjas': 15, 'limones': 5, 'limas': 20}
names = list(data.keys())
values = list(data.values())

fig, axs = plt.subplots(1, 3, figsize=(12, 3), sharey=True)
axs[0].bar(names, values)
axs[1].scatter(names, values)
axs[2].plot(names, values)
fig.suptitle('Categoría de gráficas')

plt.show()
