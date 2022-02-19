import csv

with open('[direccion del archivo]') as csv_file:
  resultado = csv.reader(csv_file, delimiter=',')
  line_count = 0
  for row in resultado:
    if line_count == 0:
      print(f'Column names are {", ".join(row)}')
    
    line_count += 1
    print(f'A {row[0]} le gusta la pelicula de {row[4]}')