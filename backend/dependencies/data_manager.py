import requests

def fetch_energy_data(limit, query):
    url = "https://dadosabertos.aneel.gov.br/pt_BR/api/3/action/datastore_search"
    params = {'resource_id': '3710b245-88f0-4aa6-8cfb-8b1426e9021d', 'limit': limit, 'q': query}
    response = requests.get(url, params=params)
    return response.json()
