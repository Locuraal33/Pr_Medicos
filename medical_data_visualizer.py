import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sn

#Importamos los datos
dm = pd.read_csv("Datos.csv")
dm.info()
dm.head()