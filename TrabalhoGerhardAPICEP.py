import requests

def consulta_cep(cep):
    # URL da API do ViaCEP
    url = f'https://viacep.com.br/ws/{cep}/json/'

    # Fazendo a requisição GET para a API
    response = requests.get(url)

    # Verificando se a resposta da API foi bem-sucedida
    if response.status_code == 200:
        data = response.json()
        if 'erro' not in data:
            print(f'CEP: {data["cep"]}')
            print(f'Logradouro: {data["logradouro"]}')
            print(f'Complemento: {data.get("complemento", "")}')
            print(f'Bairro: {data["bairro"]}')
            print(f'Cidade: {data["localidade"]}')
            print(f'Estado: {data["uf"]}')
        else:
            print('CEP não encontrado.')
    else:
        print('Erro ao consultar o CEP.')

if __name__ == '__main__':
    cep = input('Digite o CEP a ser consultado: ')
    consulta_cep(cep)