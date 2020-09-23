import requests

url ='http://www.wttr.in/'
payload= {'n':'','lang':'ru'}
cities_name= {'Лондон':'Лондон',
              'Шереметьево': 'Шереметьево',
              'Череповец':'Череповец',
              }

for city_name in cities_name:  

  response= requests.get(url +city_name, params= payload)
  response.raise_for_status()
  response.url
  print(response.text)