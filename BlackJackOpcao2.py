import random

# Variáveis globais para os saldos iniciais dos jogadores
saldos_iniciais = [2000, 2000, 2000]
saldos_atuais = list(saldos_iniciais)

# Fichas disponíveis para compra
fichas_disponiveis = [1, 5, 25, 100]

# Baralho com 52 cartas
baralho = [
    'A♣', '2♣', '3♣', '4♣', '5♣', '6♣', '7♣', '8♣', '9♣', '10♣', 'J♣', 'Q♣', 'K♣',
    'A♦', '2♦', '3♦', '4♦', '5♦', '6♦', '7♦', '8♦', '9♦', '10♦', 'J♦', 'Q♦', 'K♦',
    'A♥', '2♥', '3♥', '4♥', '5♥', '6♥', '7♥', '8♥', '9♥', '10♥', 'J♥', 'Q♥', 'K♥',
    'A♠', '2♠', '3♠', '4♠', '5♠', '6♠', '7♠', '8♠', '9♠', '10♠', 'J♠', 'Q♠', 'K♠'
]

# Função para calcular pontos de uma mão
def calcular_pontos(mao):
    pontos = 0
    as_count = 0

    for carta in mao:
        if carta.startswith('A'):
            as_count += 1
            pontos += 1
        elif carta.startswith(('K', 'Q', 'J')):
            pontos += 10
        else:
            pontos += int(carta[:-1])

    # Considera os As como 11 se não estourar 21
    while as_count > 0 and pontos + 10 <= 21:
        pontos += 10
        as_count -= 1

    return pontos

# Função para mostrar a mão de um jogador
def mostra_mao(mao):
    return ', '.join(mao)

# Função para mostrar os pontos de um jogador
def exibir_pontos(mao):
    return calcular_pontos(mao)

# Função para comprar uma carta
def hit(mao):
    carta = baralho.pop(random.randint(0, len(baralho) - 1))
    mao.append(carta)
    return carta

# Função para fazer uma aposta
def bet(saldo_atual):
    print(f"Saldo atual: R${saldo_atual}")

    while True:
        try:
            aposta = int(input("Faça sua aposta: R$  "))
            if aposta <= saldo_atual and aposta > 0:
                saldo_atual -= aposta
                return aposta
            else:
                print("Aposta inválida. Tente novamente.")
        except ValueError:
            print("Por favor, insira um valor numérico.")

# Função para render-se e encerrar o jogo
def surrender(mao, jogador):
    pontos = calcular_pontos(mao)
    print(f"Jogador {jogador}, você se rendeu! Pontos: {pontos}. Saldo final: R$ {saldos_atuais[jogador - 1]}")
    exit()

# Função para mostrar o saldo atual
def mostra_dinheiro(jogador):
    print(f"Saldo do Jogador {jogador}: R${saldos_atuais[jogador - 1]}")

# Função para a jogada do computador
def jogada_computador(mao):
    while calcular_pontos(mao) < 17:
        carta = hit(mao)
        print(f"\nComputador comprou: {carta}")

# Função para comprar fichas
def comprar_fichas(jogador):
    print(f"Saldo atual do Jogador {jogador}: R${saldos_atuais[jogador - 1]}")
    
    while True:
        print("Fichas disponíveis para compra: ", fichas_disponiveis)
        escolha_fichas = int(input("Escolha o valor das fichas que deseja comprar (ou 0 para sair): R$"))
        
        if escolha_fichas == 0:
            break
        
        if escolha_fichas in fichas_disponiveis:
            if escolha_fichas <= saldos_atuais[jogador - 1]:
                saldos_atuais[jogador - 1] -= escolha_fichas
                return escolha_fichas
            else:
                print("Saldo insuficiente. Escolha um valor dentro do seu saldo.")
        else:
            print("Opção de ficha inválida. Escolha um valor disponível.")

# Função principal do jogo


def novo_jogo():
    while True:
        jogar_blackjack()
        continuar = input("Deseja fazer uma nova partida? (s/n): ").lower()
        if continuar != 's':
            break

def jogar_blackjack():
    print("Bem-vindo ao Blackjack!")

    for jogador in range(1, 3):
        print(f"\nJogador {jogador}, é a sua vez!")

        # Comprar fichas
        fichas_compradas = comprar_fichas(jogador)
        print(f"Você comprou fichas no valor de R${fichas_compradas} ")

        # Inicializa o jogo para o jogador
        jogador_mao = [hit(baralho), hit(baralho)]
        computador_mao = [hit(baralho), hit(baralho)]
        aposta = bet(saldos_atuais[jogador - 1])

        # Mostra as mãos iniciais
        print(f"\nSua mão: {mostra_mao(jogador_mao)}")
        print(f"Computador: {computador_mao[0]}, *")

        # Loop do jogador
        while True:
            print("\nEscolha sua ação:")
            print("1. Comprar (Hit)")
            print("2. Parar (Stand)")
            print("3. Desistir (Surrender)")
            print("4. Mostrar dinheiro (Show Money)")

            escolha = input("> ")

            if escolha == '1':
                carta = hit(jogador_mao)
                print(f"Você comprou: {carta}")
                print(f"Sua mão: {mostra_mao(jogador_mao)}")
                pontos = exibir_pontos(jogador_mao)
                print(f"Pontos: {pontos}")

                if pontos > 21:
                    print("Estourou 21! Você perdeu.")
                    break

            elif escolha == '2':
                break

            elif escolha == '3':
                surrender(jogador_mao, jogador)

            elif escolha == '4':
                mostra_dinheiro(jogador)

            else:
                print("Escolha inválida. Tente novamente.")

        # Loop do computador
        while calcular_pontos(computador_mao) < 17:
            carta = hit(computador_mao)
            print(f"\nComputador comprou: {carta}")

        # Mostra as mãos finais
        print("\nMãos finais:")
        print(f"Sua mão: {mostra_mao(jogador_mao)} - Pontos: {exibir_pontos(jogador_mao)}")
        print(f"Computador: {mostra_mao(computador_mao)} - Pontos: {exibir_pontos(computador_mao)}")

        # Determina o vencedor
        pontos_jogador = exibir_pontos(jogador_mao)
        pontos_computador = exibir_pontos(computador_mao)

        if pontos_jogador > 21 or (pontos_computador <= 21 and pontos_computador >= pontos_jogador):
            saldos_atuais[jogador - 1] -= aposta
            print(f"Jogador {jogador}, você perdeu a aposta.")
        else:
            saldos_atuais[jogador - 1] += aposta * 2
            print(f"Jogador {jogador}, você ganhou a aposta!")

        # Mostra os saldos finais de todos os jogadores
        for jogador in range(1, 3):
            print(f"Saldo final do Jogador {jogador}: R${saldos_atuais[jogador - 1]}")

        # Verifica se algum jogador ficou sem saldo
        if any(saldo <= 0 for saldo in saldos_atuais):
            print("Um ou mais jogadores ficaram sem saldo. Fim do jogo.")
            exit()

if __name__ == "__main__":
    novo_jogo()