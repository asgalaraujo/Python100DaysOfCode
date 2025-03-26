import art
print(art.logo[0])

proximo_apostador = "S"
apostas = {}


while proximo_apostador.upper() == "S":
    nome = input("Digite seu nome: ")
    aposta = int(input("Digite sua aposta: "))
    proximo_apostador = input("Existe um próximo apostador [S/N]? ")
    print("\n"*100)

    apostas[aposta] = nome

# Declaração de dicionario para teste
# apostas = {100: "Adriana", 500: "Miguel", 200: "Matheus", 10: "Alexandre"}

valor_ganhador = sorted(apostas, reverse=True)[0]
ganhador = apostas[valor_ganhador]

print(f"O ganhador foi {ganhador}, com o valor de {valor_ganhador}.")