# Crie um dicionário de produtos e preços
produtos = {
    "tomate": 7.0,
    "alface": 2.0,
    "arroz": 5.0,
    "carne": 40.0
}

# Função para consultar o preço de um produto
def consultar_preco():
    produto = input("Digite o nome do produto (ou 'fim' para encerrar): ").lower()

    if produto == "fim":
        return False

    if produto in produtos:
        preco = produtos[produto]
        print(f"O preço de {produto} é R$ {preco:.2f}")
    else:
        print(f"Não possuímos o item {produto}")

    return True

# Loop para consultar preços até que o usuário digite "fim"
while consultar_preco():
    pass