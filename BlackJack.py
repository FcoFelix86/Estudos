import random

# Variável global para o saldo inicial
saldo_inicial = 2000
saldo_atual = saldo_inicial

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
def show_hand(mao):
    return ', '.join(mao)

# Função para mostrar os pontos de um jogador
def show_points(mao):
    return calcular_pontos(mao)

# Função para comprar uma carta
def hit(mao):
    carta = baralho.pop(random.randint(0, len(baralho)-1))
    mao.append(carta)
    return carta

# Função para fazer uma aposta
def bet():
    global saldo_atual
    print(f"Saldo atual: R${saldo_atual}")
    
    while True:
        try:
            aposta = int(input("Faça sua aposta: R$"))
            if aposta <= saldo_atual and aposta > 0:
                saldo_atual -= aposta
                return aposta
            else:
                print("Aposta inválida. Tente novamente.")
        except ValueError:
            print("Por favor, insira um valor numérico.")

# Função para render-se e encerrar o jogo
def surrender(mao):
    pontos = calcular_pontos(mao)
    print(f"Você se rendeu! Pontos: {pontos}. Saldo final: R${saldo_atual}")
    exit()

# Função para mostrar o saldo atual
def show_money():
    print(f"Saldo atual: R${saldo_atual}")

# Função principal do jogo
def jogar_blackjack():
    global saldo_atual
    print("Bem-vindo ao Blackjack!")

    while True:
        # Inicializa o jogo
        jogador_mao = [hit(baralho), hit(baralho)]
        computador_mao = [hit(baralho), hit(baralho)]
        aposta = bet()

        # Mostra as mãos iniciais
        print(f"\nSua mão: {show_hand(jogador_mao)}")
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
                print(f"Sua mão: {show_hand(jogador_mao)}")
                pontos = show_points(jogador_mao)
                print(f"Pontos: {pontos}")

                if pontos > 21:
                    print("Estourou 21! Você perdeu.")
                    break

            elif escolha == '2':
                break

            elif escolha == '3':
                surrender(jogador_mao)

            elif escolha == '4':
                show_money()

            else:
                print("Escolha inválida. Tente novamente.")

        # Loop do computador
        while calcular_pontos(computador_mao) < 17:
            carta = hit(computador_mao)
            print(f"\nComputador comprou: {carta}")

        # Mostra as mãos finais
        print("\nMãos finais:")
        print(f"Sua mão: {show_hand(jogador_mao)} - Pontos: {show_points(jogador_mao)}")
        print(f"Computador: {show_hand(computador_mao)} - Pontos: {show_points(computador_mao)}")

        # Determina o vencedor
        pontos_jogador = show_points(jogador_mao)
        pontos_computador = show_points(computador_mao)

        if pontos_jogador > 21 or (pontos_computador <= 21 and pontos_computador >= pontos_jogador):
            saldo_atual -= aposta
            print("Você perdeu a aposta.")
        else:
            saldo_atual += aposta * 2
            print("Você ganhou a aposta!")

        # Pergunta se o jogador quer jogar novamente
        jogar_novamente = input("Deseja jogar novamente? (s/n): ").lower()
        if jogar_novamente != 's':
            print(f"Obrigado por jogar! Seu saldo final: R${saldo_atual}")
            break

if __name__ == "__main__":
    jogar_blackjack()