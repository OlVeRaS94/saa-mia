import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler, OneHotEncoder

# Carregar el dataset
df = pd.read_csv('/home/aluvesprada/Documentos/saa/Exercicis.sobre.preprocessament/Stars.csv')

# 1. Anàlisi de les dades
print("Nombre de files i columnes:", df.shape)
print("Nuls per columna:\n", df.isnull().sum())
print("Tipus de dades:\n", df.dtypes)
print("Nombre de files per cada tipus d'estrela:\n", df['Type'].value_counts())

# 2. Tractament de nuls
# Comprovar els valors nuls per files i columnes
nuls_per_fila = df.isnull().sum(axis=1)
nuls_per_columna = df.isnull().sum()

# Eliminar les files amb més de dos nuls
df = df[nuls_per_fila <= 2]

# Completar els valors nuls amb la mitja per a columnes numèriques
for col in df.select_dtypes(include=[np.number]).columns:
    df[col] = df[col].fillna(df[col].mean())

# Completar els valors nuls amb la moda per a columnes de text
for col in df.select_dtypes(include=[object]).columns:
    df[col] = df[col].fillna(df[col].mode()[0])

# 3. Escalament de les dades
# Escalament de les dades numèriques amb MinMaxScaler
scaler = MinMaxScaler()
df[df.select_dtypes(include=[np.number]).columns] = scaler.fit_transform(df.select_dtypes(include=[np.number]))

# Codificació de les dades de text amb OneHotEncoder
encoder = OneHotEncoder(sparse_output=False)
encoded_cols = encoder.fit_transform(df.select_dtypes(include=[object]))
encoded_df = pd.DataFrame(encoded_cols, columns=encoder.get_feature_names_out(df.select_dtypes(include=[object]).columns))

# Unir les dades escalades i codificades en un nou DataFrame
df_processed = pd.concat([df.select_dtypes(include=[np.number]), encoded_df], axis=1)

# Mostrar el nou DataFrame processat
print(df_processed.head())
