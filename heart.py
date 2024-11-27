import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler, OneHotEncoder

# Carregar el dataset
df = pd.read_csv('/home/aluvesprada/Documentos/saa/Exercicis.sobre.preprocessament/heart.csv')

# 1. Anàlisi de les dades
print("Nombre de files i columnes:", df.shape)
print("Nuls per columna:\n", df.isnull().sum())
print("Tipus de dades:\n", df.dtypes)

# 2. Tractament de nuls
# Comprovar els valors nuls per files i columnes
nuls_per_fila = df.isnull().sum(axis=1)
nuls_per_columna = df.isnull().sum()

# Eliminar les files amb nuls
df = df.dropna()

# 3. Escalament de les dades
# Escalament de les dades numèriques amb MinMaxScaler
scaler = MinMaxScaler()
df[df.select_dtypes(include=[np.number]).columns] = scaler.fit_transform(df.select_dtypes(include=[np.number]))

# Mostrar els outliers
Q1 = df.quantile(0.25)
Q3 = df.quantile(0.75)
IQR = Q3 - Q1
print("Outliers:")
print(df[(df < (Q1 - 1.5 * IQR)) | (df > (Q3 + 1.5 * IQR))].count())

# Mostrar el DataFrame processat
print(df.head())
