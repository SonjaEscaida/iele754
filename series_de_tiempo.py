#Ejercicio 1: Cargar los datos

import pandas as pd

data_url = "_____" # Completa con la URL del archivo CSV que deseas cargar
df = pd.read_csv(data_url)


#Ejercicio 2: Inspeccionar los datos

# Muestra las primeras filas del dataframe
df._____


#Ejercicio 3: Manejar valores faltantes

# Verifica si hay valores faltantes
valores_faltantes = df._____

# Maneja los valores faltantes
df_limpio = df._____


#Ejercicio 4: Convertir tipos de datos

# Convierte una columna a datetime
df_limpio['columna_fecha'] = pd._____(df_limpio['columna_fecha'])



#Ejercicio 5: Calcular estadísticas básicas

# Calcula la media de una columna
valor_medio = df_limpio['nombre_columna']._____




#Ejercicio 6: Crear un histograma

import matplotlib.pyplot as plt

# Dibuja un histograma de una columna
plt._____(df_limpio['nombre_columna'])
plt.show()



#Ejercicio 7: Calcular correlaciones

# Calcula la correlación entre dos columnas
correlacion = df_limpio['columna1']._____(df_limpio['columna2'])



#Ejercicio 8: Dibujar datos de series temporales

# Dibuja una columna como una serie temporal
df_limpio.plot(x='columna_fecha', y='nombre_columna')
plt.show()



#Ejercicio 9: Descomponer la serie temporal

from statsmodels.tsa.seasonal import seasonal_decompose

# Descompone una columna de series temporales
descomposicion = seasonal_decompose(df_limpio['nombre_columna'],
                                    model='additive', period=1)
descomposicion.plot()
plt.show()



#Ejercicio 10: Crear modelo ARIMA

from statsmodels.tsa.arima.model import ARIMA

# Crea y ajusta un modelo ARIMA
modelo = ARIMA(df_limpio['nombre_columna'], order=(5,1,0))
modelo_ajustado = modelo._____ 
