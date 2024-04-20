import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Importamos los datos
df = pd.read_csv("medical_examination.csv")

# Añadir la columna overweight
df['overweight'] = np.where((df['weight'] / ((df['height']/100)**2)) > 25, 1, 0)
print(df.head())

# Normalizar gluc y cholesterol

df['gluc'] = np.where((df['gluc']) > 1, 1, 0)
df['cholesterol'] = np.where((df['cholesterol']) > 1, 1, 0)
print(df.head(50))