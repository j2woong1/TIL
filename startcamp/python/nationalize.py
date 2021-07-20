import requests

name = 'woong'
url = f'https://api.nationalize.io/?name={name}'
response = requests.get(url).json()

print(response)