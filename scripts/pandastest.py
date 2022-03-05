import pandas as pd

# cargar el csv como dataframe de pandas
dfcsv = pd.read_csv('./notebooks/Familia.csv')

# sumar el total de las edades de la familia
valorTotalEdades = dfcsv['Edad'].sum()
personaMenor = dfcsv['Edad'].min()
personaMayor = dfcsv['Edad'].max()

resultado = dfcsv[dfcsv['Edad'] == dfcsv['Edad'].max()]

print(resultado)