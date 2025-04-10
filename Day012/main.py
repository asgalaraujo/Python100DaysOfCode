import random

while input("Deseja jogar 'Adivinhe o número'? s/n: ").lower() == "s":
    nivel = input("Deseja nível fácil (f) ou difícil (d)?: ")
    if nivel == "f":
        chances = 10
    else:
        chances = 5

    numero = random.randint(0,100)

    print(f"O número escolhido é {numero}")
    print("\n"*30)
    acertou = False
    for i in range(chances):
        print(f"Você tem {chances - i} chance(s)")
        escolha = int(input("Adivinhe o número entre 0 e 100: "))
        if numero == escolha:
            print("Você adivinhou!")
            acertou = True
            break
        elif escolha > numero:
            print("Muito alto.")
        else:
            print("Muito baixo.")


    if acertou:
        print("Parabéns, você adivinhou o número.")
    else:
        print(f"Tentativas esgotadas. O número era {numero}")



