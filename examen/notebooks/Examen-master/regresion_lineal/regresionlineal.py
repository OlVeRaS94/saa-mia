# Importar librerías necesarias
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Datos
tamaño = np.array([50, 100, 150, 200, 250]).reshape(-1, 1) # Variable independiente (tamaño en m²)
precio = np.array([150000, 300000, 450000, 600000, 750000]) # Variable dependiente (precio en €)

# Crear el modelo de regresión lineal
modelo = LinearRegression()

# Entrenar el modelo
modelo.fit(tamaño, precio)

# Predicción para un tamaño específico
tamaño_nuevo = np.array([[120]]) # Por ejemplo, una casa de 120 m²
prediccion = modelo.predict(tamaño_nuevo)

print(f"El precio estimado para una casa de {tamaño_nuevo[0][0]} m² es de {prediccion[0]:,.2f} €")

# Visualización de los datos y el modelo
plt.scatter(tamaño, precio, color='blue', label='Datos reales')
plt.plot(tamaño, modelo.predict(tamaño), color='red', label='Línea de regresión')
plt.xlabel('Tamaño (m²)')
plt.ylabel('Precio (€)')
plt.title('Regresión Lineal: Precio de una Casa')
plt.legend()
plt.show()