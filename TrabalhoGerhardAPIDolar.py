import requests

def obter_cotacao_dolar():
    # URL da API do Banco Central do Brasil para obter a cotação do dólar
    url = "https://api.bcb.gov.br/dados/serie/bcdata.sgs.10813/dados?formato=json"

    try:
        # Faz a requisição GET para a API
        response = requests.get(url)
        
        # Verifica se a resposta da API foi bem-sucedida
        if response.status_code == 200:
            # Analisa os dados JSON da resposta
            dados = response.json()
            
            # Obtém a cotação mais recente do dólar
            cotacao = dados[-1]['valor']
            
            return cotacao
        else:
            print("Erro ao obter dados da API:", response.status_code)
            return None
    except Exception as e:
        print("Erro na requisição à API:", str(e))
        return None

# Função principal
def main():
    cotacao_dolar = obter_cotacao_dolar()
    
    if cotacao_dolar is not None:
        print(f"A cotação do dólar é R${cotacao_dolar:.2f}")

if __name__ == "__main__":
    main()

