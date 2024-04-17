# Se transforma el archivo csv y posteriormente se filtra la información que queremos visualizar del país que se indicó en el main

import csv


# Leer archivo para visualizar en diccionarios:
def read_csv(path):
  with open(path, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    header = next(reader)
    data = []  #lista vacia para guardar cada diccionario
    for row in reader:
      iterable = zip(header, row)
      country_dict = {
        key: value
        for key, value in iterable
      }  # pasamos las tuplas a diccionario
      data.append(country_dict)  #agregar cada diccionario a la lista vacia
      #print(country_dict)
    return data  #para mandar el resultado en la ejecución


data = read_csv('./data.csv')
#print(data[8])
'''
if __name__ == '__main__':
  data = read_csv('./app/data.csv')
  print(data[8]) #para imprimir un resultado
'''
