import requests
import json

url = "https://raw.githubusercontent.com/albertobatalha1970/apialberto/main/eletronicos.json"
response = requests.get(url)
response = response.json()
print(response)