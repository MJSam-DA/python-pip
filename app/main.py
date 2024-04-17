# Se indica que país es del que queremos la información

import charts
import read_csv
import utils

data = read_csv.data
#print(data)

def run():
  country = input('Menciona el país: ').title()
  #result = utils.general_country_info(data, country)

  labels, values = utils.population_by_country(data, country)
  #print(population)
  charts.generate_bar_chart(country, labels, values)



def wpp():
  #Opcional filtrar por continentes para una mejor visualización en la gráfica
  data = read_csv.data
  data = list(filter(lambda item : item['Continent'] == 'North America', data))
  labels, values = utils.world_population_percentage(data)
  charts.generate_pie_chart(labels, values)


if __name__ == '__main__':
  run()
  #wpp()