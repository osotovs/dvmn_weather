import requests

url ='http://www.wttr.in/'
payload= {'nTqm': '', 
          'lang': 'ru'}

cities= ['Лондон',
        'Шереметьево',
        'Череповец',]

for city in cities:  
  response= requests.get (f'{url}{city}', params= payload)
  response.raise_for_status()  
  print(response.text)