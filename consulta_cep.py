def consulta(cep):
    import requests

    url = 'http://viacep.com.br/ws/%s/json/' % cep
    response = requests.get(url)
    response_json = response.json()
    return response_json