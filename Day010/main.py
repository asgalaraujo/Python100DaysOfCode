from art import logo

def calcular(num1, operador, num2):
    """Esta função recebe um operador e dois números e retorna o resultado do cálculo"""
    if operador == "+":
        return num1 + num2
    elif operador == "-":
        return num1 - num2
    elif operador == "*":
        return num1 * num2
    elif operador == "/":
        return num1 / num2
    else:
        print("Operador inválido.")
        return

print(logo)
continua = 'n'

while True:
    if continua == 'n':
        num1 = int(input("Qual é o primeiro número: "))
    elif continua == 's':
        num1 = resultado
    else:
        break
    operador = input("Escolha um operador entre + - * ou / : ")
    num2 = int(input("Qual é o segundo número: "))
    resultado = calcular(num1, operador, num2)

    if resultado != None:
        print(f"{num1} {operador} {num2} = {resultado}")
        continua = input(f"Digite 's' se deseja continuar calculando com o {resultado}, ou digite 'n' para iniciar um novo cálculo: ")
    else:
        continua = 'n'