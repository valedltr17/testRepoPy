import csv

with open('./notebooks/Familia.csv') as csv_file:
  resultado = csv.reader(csv_file, delimiter=',')
  line_count = 0
  total_edades = 0
  for row in resultado:
    # if line_count == 0:
      # print(f'Column names are {", ".join(row)}')
    
    if line_count > 0:
      print(f'El "mejor amig@" de {row[0]} es {row[4]}')

      # Sumar el total de edades de la familiar
      total_edades += row[3]
    line_count += 1