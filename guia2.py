import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

URL = 'https://github.com/MinCiencia/Datos-COVID19/blob/master/output/producto1/Covid-19.csv'

data = pd.read_csv(URL)
print(data)
data.head()

vals = list(data.columns)[5:-1]
ids = list(data.columns)[:5]
df_cases_tidy = pd.melt(data, value_vars=vals, id_vars=ids)

df_cases_tidy.head()
print(df_cases_tidy.info())

#a) Limpiar fechas
df_cases_tidy['variable'] = pd.to_datetime(df_cases_tidy['variable'])

#Fechas de inicio y fin
fi= '2020-03-01'
ff= '2020-06-30'

#Filtrar datos- mantener fechas entre inicio y fin
df_cases_month= df_cases_tidy[(df_cases_tidy['variable'] >= fi) & (df_cases_tidy ['variable'] <= ff) ]

#Mostrar el resultado
print(df_cases_month)
df_cases_month.head()
df_cases_month.info()

#Eliminar datos nulos 
# Es cases o case ?
df_cases_sn =df_cases_month.dropna()
df_cases_sn.head()

df_cases_sn['variable'] =pd.to_datetime(df_cases_sn['variable'])
df_cases_sn['value'] = pd.to_numeric(df_cases_sn['value'])

df =df_cases_sn.sort_values(by='variable')
df.head()


