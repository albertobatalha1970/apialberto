import requests
import json

url = "https://raw.githubusercontent.com/albertobatalha1970/apialberto/main/api.json"
responses = requests.get(url)
responses = responses.json()
print("O preço do Tablet é: ")
print(responses['Aluno']['nome'])