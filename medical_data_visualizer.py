import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Importamos los datos
df = pd.read_csv("medical_examination.csv")

# Añadir la columna overweight
df['overweight'] = np.where((df['weight'] / ((df['height']/100)**2)) > 25, 1, 0)

# Normalizar gluc y cholesterol

df['gluc'] = np.where((df['gluc']) > 1, 1, 0)
df['cholesterol'] = np.where((df['cholesterol']) > 1, 1, 0)

# Crear el grafico 

def draw_cat_plot():

    # Preparación de los datos
    df_cat = pd.melt(df, id_vars=['cardio'], value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])
    
    # Graficar con seaborn
    fig = sns.catplot(
        x='variable', 
        y='total', 
        hue='value', 
        col='cardio',
        kind='bar',
        data=df_cat.groupby(['cardio', 'variable', 'value']).size().reset_index(name='total')
    )
    
    # Guardar la figura
    fig.savefig('catplot.png')
    
    return fig

df_cat = pd.melt(df, id_vars=['cardio'], value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])
    
print(df_cat)
df_cat.info()
print(df_cat.tail(10))