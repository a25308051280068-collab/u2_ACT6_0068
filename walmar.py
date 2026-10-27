
# Importar librerías
import matplotlib.pyplot as plt
import numpy as np

# Christian Garcia Jimenez
# Fecha = 27 / octubre / 2026

print("Christian Garcia Jimenez Nc = 0068")

cant_productos = [100, 160, 200, 300, 500]
precio = [4000, 7000, 9000, 10000, 11000]

plt.plot(cant_productos, precio)
plt.show()

# Personalizar productos
plt.plot(
    cant_productos,
    precio,
    color="gold",
    marker="*",
    linestyle="--",
    linewidth=2,
    markersize=12
)
plt.title(" Ventas de walmar 0068 ")
plt.xlabel(" cantidad de producto  ")
plt.ylabel(" Precio ")
plt.show()
