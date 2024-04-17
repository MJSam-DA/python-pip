# Módulo para filtrar solo al país que nos interesa de todo el archivo 

def general_country_info(data, country):
  result = list(filter(lambda item : item['Country/Territory'] == country, data))
  return result


def population_by_country(data, country):
  population = {}
  pais = list(filter(lambda item : item['Country/Territory'] == country, data))
  years = ['2022 Population', '2020 Population', '2015 Population', '2010 Population', '2000 Population', '1990 Population', '1980 Population', '1970 Population']
  years_population = pais[0]
  for year in years:
    population[year[0:4]] = int(years_population[year])
    #print(f'{year[0:4]} : {years_population[year]}')

  labels = population.keys()
  values = population.values()
  return labels, values


def world_population_percentage(data):
  info = {}
  for pais in data:
    info[pais['CCA3']] = float(pais['World Population Percentage'])

  labels = info.keys()
  values = info.values()
  return labels, values