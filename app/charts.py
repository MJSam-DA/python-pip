# La libreria matplotlib se debe instalar para poder ser utilizada
import matplotlib.pyplot as plt


def generate_bar_chart(name, labels, values):
  fig, ax = plt.subplots() #coordenadas
  ax.bar(labels, values) #se indica que tipo de gráfica se quiere usar
  plt.savefig(f'./imgs/{name}.png')
  plt.close()

def generate_pie_chart(labels, values):
  fig, ax = plt.subplots()
  ax.pie(values, labels=labels)
  ax.axis('equal')
  plt.savefig('pie.png')
  plt.close()


  # Vamos a ejecutar el código como script
if __name__ == '__main__':
  labels = ['a', 'b', 'c'] #nombres de columnas
  values = [10, 40, 800] #valores de las columnas
  #generate_bar_chart() #llamado de función
  generate_pie_chart(labels, values)