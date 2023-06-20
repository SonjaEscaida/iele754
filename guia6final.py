#!/usr/bin/env python
# coding: utf-8

# # Correlación Lineal y Métodos para detectarlas
# Importamos las librerias que necesitamos

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Leemos el archivo que queremos analizar 

# In[2]:


url= "https://raw.githubusercontent.com/rociochavezmx/Rocio-Chavez-youtube-Files/master/Contaminacion%20Atmosferica.csv"
contamina= pd.read_csv(url)
print(contamina)


# In[3]:


contamina.info()


# In[4]:


contamina.head()


# Creamos el diagrama de dispersión para algunos pares de variables

# In[5]:


plt.scatter(contamina['Velocidad_viento'], contamina['Dias_Lluvia'])
plt.title('Dias_Lluvia y Velocidad_Viento')
plt.xlabel("Velocidad_Viento")
plt.ylabel("Dias_Lluvia")
#Esto es para ver la correlación, la cual no hay porque los puntos estan muy dispersos


# In[6]:


plt.scatter(contamina['Temperatura'], contamina['Contaminacion_SO2'])
plt.title('Contaminacion_SO2 y Temperatura')
plt.xlabel("Temperatura")
plt.ylabel("Contaminacion_SO2")
#A mayor Temperatura, menor Contaminacion-  Correlación Negativa


# In[7]:


plt.scatter(contamina['Habitantes'], contamina['Fabricas'])
plt.title('Fabricas y Habitantes')
plt.xlabel("Habitantes")
plt.ylabel("Fabricas")
#Correlación Positiva


# Creamos una gráfica que muestre los diagramas de dispersión de todas las variables 

# In[8]:


sns.pairplot(contamina)


# # Pruebas de Normalidad

# Probamos normalidad en un conjunto de datos con distribución normal generado aleatoriamente 

# In[9]:


import numpy as np
data_points =np.random.normal(0, 1, 100) #Datos aleatorios solo para demostración 
data_points


# Creamos el histograma con los datos generados aleatoriamente 

# In[10]:


plt.hist(data_points, edgecolor = 'black', linewidth =1)
#Esto nos da una idea de que los datos tienen una distribución normal


# Creamos el gráfico Quantile-Quantile para corroborar normalidad de los datos

# In[11]:


import pylab
import scipy.stats as stats

stats.probplot(data_points, dist= "norm", plot= pylab)
pylab.show()
#Mientras más cercanos esten los puntos a la linea, más cercana será la distribución a la normal


# Otra forma de comprobar los datos es aplicando el Test de Shapiro-Wilks para probar normalidad 

# In[12]:


from scipy.stats import shapiro
estadistico, p_value = shapiro(data_points)
print('Estadístico=%.3f, p_value=%.3f' % (estadistico, p_value))
# %.3f indicamos que queremos 3 decimales
# Cuando es p_value mayor a 0.5, quiere decir que los datos si tienen una dist. normal- Aquí no me cuadra(debería ser 0.8pero no dio)


# Probamos normalidad en alguna de nuestras variables para determinar el tipo de coeficiente a utilizar para calcular la correlación.

# Creamos el histograma con los datos de la variable Velocidad_viento

# In[14]:


plt.hist(contamina['Velocidad_viento'], edgecolor ='black', linewidth=1)


# Creamos el gráfico Quantil-Quantil para Velocidad_viento

# In[17]:


stats.probplot(contamina['Velocidad_viento'], dist= "norm", plot= pylab)
pylab.show()


# Aplicamos la prueba del test Shapiro-Wilks a Velocidad_viento

# In[18]:


estadistico, p_value = shapiro(contamina['Velocidad_viento'])
print('Estadístico=%.3f, p_value=%.3f' % (estadistico, p_value))
#Tiene un p_value mayor a 0.05, por lo tanto tiene una dist normal


# Creamos el histograma con los datos de la variable Conaminación _SO2

# In[19]:


plt.hist(contamina['Contaminacion_SO2'], edgecolor ='black', linewidth=1)


# Obtenemos el gráfico Quantile-Quantile para Contaminación_SO2

# In[21]:


stats.probplot(contamina['Contaminacion_SO2'], dist= "norm", plot= pylab)
pylab.show()
#Se puede ver una clara falta de normalidad en los datos- Alejados de la linea 


# Aplicamos la prueba del test Shapiro-Wilks a Contaminacion_SO2

# In[22]:


estadistico, p_value = shapiro(contamina['Contaminacion_SO2'])
print('Estadístico=%.3f, p_value=%.3f' % (estadistico, p_value))
#Este si arroja un p_value menor a 0.05- Significa que no distribuye normal


# # Calculando la correlación y su significancia

# Obtenemos la correlación de todos los pares de variables

# In[23]:


contamina_corr= contamina.corr(method='spearman')
contamina_corr


# Creamos el mapa de calor con las correlaciones

# In[25]:


sns.heatmap(contamina_corr, 
           xticklabels=contamina_corr.columns,
           yticklabels=contamina_corr.columns,
           cmap='coolwarm'
           )
#Azules= correlaciones negativas, 
#Rojas= correlaciones positivas


# Para obtener adempas la significancia usamos el paquete pingouin

# In[27]:


import pingouin as pg #Debo instalarlo tecleando'pip install pingouin' en Anaconda
corr= pg.pairwise_corr(contamina, method='spearman')

#Ordena los valores de la correlación en base a su significancia y le indicas las columnas a desplehar.
corr.sort_values(by=['p-unc'])[['X','Y','n','r','p-unc']]


# In[ ]:




