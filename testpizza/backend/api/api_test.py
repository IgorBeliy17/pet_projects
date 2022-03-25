import requests

response = requests.get('http://127.0.0.1:8000/api/v1/pizza/')
print(response.json())
print(response.status_code)

data = {
    'name': 'из апи',
    'description': 'описание пиццы из апи',
    'toppings': [1, 2],
    'created_by': 1,
    'slug': 'pizzafromapi2'
}
response = requests.post('http://127.0.0.1:8000/api/v1/pizza/', data=data)
print(response.text)
print(response.status_code)