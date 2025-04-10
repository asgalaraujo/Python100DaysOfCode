
# TODO : mostrar apenas uma carta do crupiê
# TODO: mostrar ganhador

from art import logo
import random

monte = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def dar_cartas(mao, quantidade_cartas):
    for carta in range(0, quantidade_cartas):
        mao.append(random.choice(monte))
    return mao

def calcular_cartas(mao):
    for carta in mao:
        if sum(mao) > 21 and 11 in mao:
            mao.remove(11)
            mao.append(1)
    return sum(mao)

def jogar():
    mao_crupie = []
    mao_jogador = []

    print(logo[0])
    dar_cartas(mao_crupie, 2)
    dar_cartas(mao_jogador, 2)

    seus_pontos = sum(mao_jogador)

    print(f"Mão crupiê: [{mao_crupie[0]}, X]")
    print(f"Sua mão: {mao_jogador}")
    print(calcular_cartas(mao_jogador))

    estourou = False

    while input("Mais uma carta? s ou n: ").lower() == "s":
        dar_cartas(mao_jogador, 1)
        print(mao_jogador)
        seus_pontos = calcular_cartas(mao_jogador)
        print(seus_pontos)
        if seus_pontos > 21:
            print("Estourou!")
            estourou = True
            break

    if not estourou:
        pontos_crupie = calcular_cartas(mao_crupie)
        while pontos_crupie < 17:
            dar_cartas(mao_crupie, 1)
            pontos_crupie = calcular_cartas(mao_crupie)

        print(f"Mão crupiê: {mao_crupie}")

        if pontos_crupie == seus_pontos:
            print("Empate.")
        elif pontos_crupie > 21 or seus_pontos > pontos_crupie:
            print("Você ganhou.")
        elif pontos_crupie > seus_pontos:
            print("Perdeu.")
        else:
            print("Condição não mapeada. Erro no jogo! É bug!")

while input("Deseja jogar 21? s ou n: ").lower() == "s":
    jogar()