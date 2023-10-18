import random

# Lista de palavras possíveis
palavras = ["faculdade", "programacao", "linguagem", "repeticao", "jogador", "fortaleza", "alimento", "software", "desenvolvimento"]

# Escolhe uma palavra aleatória da lista
palavra_escolhida = random.choice(palavras)

# Inicializa as variáveis
tentativas_restantes = 6
letras_corretas = []

# Função para mostrar a palavra com letras corretas reveladas
def mostrar_palavra():
    palavra_mostrada = ""
    for letra in palavra_escolhida:
        if letra in letras_corretas:
            palavra_mostrada += letra
        else:
            palavra_mostrada += "_"
    return palavra_mostrada

# Loop principal do jogo
while True:
    # Mostra a palavra com letras corretas reveladas
    print(mostrar_palavra())

    # Pede ao jogador para fornecer uma letra
    letra = input("Digite uma letra: ").lower()

    # Verifica se a letra já foi tentada
    if letra in letras_corretas:
        print("Você já tentou esta letra.")
        continue

    # Verifica se a letra está na palavra
    if letra in palavra_escolhida:
        letras_corretas.append(letra)
        print("Letra correta!")
    else:
        print("Letra incorreta.")
        tentativas_restantes -= 1

    # Verifica se o jogador ganhou
    if all(letra in letras_corretas for letra in palavra_escolhida):
        print("Parabéns! Você ganhou. A palavra era:", palavra_escolhida)
        break

    # Verifica se o jogador perdeu
    if tentativas_restantes == 0:
        print("Você perdeu. A palavra era:", palavra_escolhida)
        break

    # Mostra o número de tentativas restantes
    print("Tentativas restantes:", tentativas_restantes)