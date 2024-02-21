import requests
import json

url = "https://raw.githubusercontent.com/albertobatalha1970/apialberto/main/eletronicos.json"
responses = requests.get(url)
responses = responses.json()
print("O preço do Tablet é: ")
print(responses['Smartphone']['Preço'])