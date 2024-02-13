import requests
import json

url = "https://raw.githubusercontent.com/albertobatalha1970/apialberto/main/eletronicos.json"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    
    
    
    
    # Faça o que precisar com os dados da API JSON
else:
    print("Erro ao acessar a API:", response.status_code)


response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(data)
    
    
    
    # Faça o que precisar com os dados da API JSON
else:
    print("Erro ao acessar a API:", response.status_code)