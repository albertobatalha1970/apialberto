import requests
import json

url = "https://raw.githubusercontent.com/albertobatalha1970/apialberto/main/api.json"
responses = requests.get(url)
responses = responses.json()
aluno = "O aluno tem "
print(f'{aluno}', responses["Aluno"]["idade"], ' anos de idade!')