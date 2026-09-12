
import requests
URL = 'https://dotpro.net'
res = requests.get(URL)
print(res.text)