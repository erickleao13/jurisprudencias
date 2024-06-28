import requests

def build_query_url(endpoint, params):
    base_url = "https://datajud.cnj.jus.br/api/v1"
    query_url = f"{base_url}/{endpoint}?{'&'.join([f'{k}={v}' for k, v in params.items()])}"
    return query_url

def send_api_request(endpoint, params):
    url = build_query_url(endpoint, params)
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Erro na requisição à API: {response.status_code}")

def search_jurisprudence(query, court, start_date, end_date):
    endpoint = "jurisprudencia"
    params = {
        "texto": query,
        "tribunal": court, 
        "dataInicial": start_date,
        "dataFinal": end_date
    }
    return send_api_request(endpoint, params)

def get_courts():
    endpoint = "tribunais"
    params = {}
    return send_api_request(endpoint, params)

# Exemplo de uso
results = search_jurisprudence("direito do consumidor", "TJSP", "2020-01-01", "2020-12-31")
print(results)

courts = get_courts()
print(courts)
