import random

# Variáveis globais
saldo_inicial = 2000
saldo_atual = saldo_inicial
baralho = [('A', '♣'), ('2', '♣'), ('3', '♣'), ('4', '♣'), ('5', '♣'), ('6', '♣'), ('7', '♣'), ('8', '♣'), ('9', '♣'), ('10', '♣'), ('J', '♣'), ('Q', '♣'), ('K', '♣'),
           ('A', '♦'), ('2', '♦'), ('3', '♦'), ('4', '♦'), ('5', '♦'), ('6', '♦'), ('7', '♦'), ('8', '♦'), ('9', '♦'), ('10', '♦'), ('J', '♦'), ('Q', '♦'), ('K', '♦'),
           ('A', '♥'), ('2', '♥'), ('3', '♥'), ('4', '♥'), ('5', '♥'), ('6', '♥'), ('7', '♥'), ('8', '♥'), ('9', '♥'), ('10', '♥'), ('J', '♥'), ('Q', '♥'), ('K', '♥'),
           ('A', '♠'), ('2', '♠'), ('3', '♠'), ('4', '♠'), ('5', '♠'), ('6', '♠'), ('7', '♠'), ('8', '♠'), ('9', '♠'), ('10', '♠'), ('J', '♠'), ('Q', '♠'), ('K', '♠')]


# Função para comprar cartas
def hit():
    carta = random.choice(baralho)
    baralho.remove(carta)
    return carta


# Função para mostrar a mão do jogador
def show_hand(mao):
    print("Sua mão:")
    for carta in mao:
        print(f"{carta[0]}{carta[1]}", end=" ")
    print()


# Função para mostrar os pontos do jogador
def show_points(mao):
    pontos = 0
    for carta in mao:
        if carta[0] in ['K', 'Q', 'J']:
            pontos += 10
        elif carta[0] == 'A':
            pontos += 1
        else:
            pontos += int(carta[0])
    return pontos


# Função para render-se e encerrar o jogo
def surrender(mao):
    pontos = show_points(mao)
    print(f"Você se rendeu. Pontuação final: {pontos}")
    encerrar_jogo()


# Função para mostrar o saldo atual
def show_money():
    print(f"Seu saldo atual: R${saldo_atual}")


# Função para realizar uma aposta
def bet():
    global saldo_atual
    print("Fichas disponíveis para compra: 1, 5, 25, 100")
    try:
        aposta = int(input("Digite o valor da aposta: "))
        if aposta not in [1, 5, 25, 100]:
            raise ValueError("Valor de aposta inválido. Escolha entre 1, 5, 25 ou 100.")
        if aposta > saldo_atual:
            raise ValueError("Você não possui saldo suficiente.")
        saldo_atual -= aposta
        return aposta
    except ValueError as ve:
        print(f"Erro: {ve}")
        return bet()


# Função para encerrar o jogo
def encerrar_jogo():
    print("Jogo encerrado.")
    exit()


# Função principal do jogo
def jogar_blackjack():
    global saldo_atual
    print("Bem-vindo ao Blackjack!")
    while True:
        mao_jogador = [hit(), hit()]
        mao_computador = [hit()]

        print("\nNova rodada começou!\n")
        show_hand(mao_jogador)
        show_money()

        aposta = bet()

        while True:
            opcao = input("Escolha uma opção (hit/surrender): ").lower()

            if opcao == "hit":
                mao_jogador.append(hit())
                show_hand(mao_jogador)
                pontos_jogador = show_points(mao_jogador)
                if pontos_jogador == 21:
                    print("Parabéns! Você fez 21 pontos.")
                    saldo_atual += aposta * 2
                    break
                elif pontos_jogador > 21:
                    print("Você estourou! Pontuação acima de 21.")
                    break
            elif opcao == "surrender":
                surrender(mao_jogador)
            else:
                print("Opção inválida. Escolha 'hit' ou 'surrender'.")

        while show_points(mao_computador) < 17:
            mao_computador.append(hit())

        print("\nMão do computador:")
        show_hand(mao_computador)

        pontos_jogador = show_points(mao_jogador)
        pontos_computador = show_points(mao_computador)

        print(f"\nPontuação final - Jogador: {pontos_jogador}, Computador: {pontos_computador}\n")

        if pontos_jogador > pontos_computador or pontos_computador > 21:
            print("Parabéns! Você ganhou esta rodada.")
            saldo_atual += aposta * 2
        elif pontos_jogador == pontos_computador:
            print("Empate!")
            saldo_atual += aposta
        else:
            print("Você perdeu esta rodada.")

        if saldo_atual <= 0:
            print("Você não possui mais saldo. Jogo encerrado.")
            encerrar_jogo()

        continuar = input("Deseja jogar outra rodada? (s/n): ").lower()
        if continuar != 's':
            encerrar_jogo()


if __name__ == "__main__":
    jogar_blackjack()