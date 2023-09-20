import requests
# Função consulta_cep, onde fará a consulta ao serviço ViaCEP e Exibe as informações do CEP.
def consulta_cep(cep):

    #URL de consulta para a geração o CEP
    url = f'https://viacep.com.br/ws/{cep}/json/'
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        if 'erro' not in data:
            print("CEP:", data['cep'])
            print("Logradouro:", data['logradouro'])
            print("Complemento:", data.get('complemento', 'N/A'))
            print("Bairro:", data['bairro'])
            print("Cidade:", data['localidade'])
            print("Estado:", data['uf'])
        else:
            print("CEP não encontrado.")
    else:
        print("Erro ao consultar o CEP.")
        
#Caso seja necessário encerrar o programa, será necessário digitar a palavra sim. 
while True:
    print("Consulta de CEP")
    cep = input("Digite o CEP (ou 'sim' para sair): ")
    
    if cep.lower() == 'sim':
        break
    
    consulta_cep(cep)
    input("Pressione Enter para fazer uma nova consulta...")