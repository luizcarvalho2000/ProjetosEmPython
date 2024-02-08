import math

def print_menu():
    print("Selecione a operação que deseja realizar:")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("5 - Raiz Quadrada")
    print("6 - Seno")
    print("7 - Cosseno")
    print("8 - Tangente")
    print("9 - Logaritmo")
    print("10 - Logaritmo na base 10")
    print("11 - Logaritmo na base e")

def soma():
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    resultado = num1 + num2
    print("O resultado da soma é:", resultado)

def subtracao():
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    resultado = num1 - num2
    print("O resultado da subtração é:", resultado)

def multiplicacao():
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    resultado = num1 * num2
    print("O resultado da multiplicação é:", resultado)

def divisao():
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    resultado = num1 / num2
    print("O resultado da divisão é:", resultado)

def raiz_quadrada():
    num1 = float(input("Digite um número: "))
    resultado = math.sqrt(num1)
    print("O resultado da raiz quadrada é:", resultado)

def seno():
    num1 = float(input("Digite um ângulo em graus: "))
    resultado = math.sin(math.radians(num1))
    print("O resultado do seno é:", resultado)

def cosseno():
    num1 = float(input("Digite um ângulo em graus: "))
    resultado = math.cos(math.radians(num1))
    print("O resultado do cosseno é:", resultado)

def tangente():
    num1 = float(input("Digite um ângulo em graus: "))
    resultado = math.tan(math.radians(num1))
    print("O resultado da tangente é:", resultado)

def logaritmo():
    num1 = float(input("Digite um número positivo: "))
    resultado = math.log(num1)
    print("O resultado do logaritmo natural é:", resultado)

def logaritmo_base10():
    num1 = float(input("Digite um número positivo: "))
    resultado = math.log10(num1)
    print("O resultado do logaritmo na base 10 é:", resultado)

def logaritmo_basee():
    x = float(input("Digite um número positivo: "))
    resultado = math.log(x)
    print("O resultado do logaritmo na base e é:", resultado)

while True:
    print_menu()
    escolha = input("Digite a sua escolha (1/2/3/4/5/6/7/8/9/10/11): ")

    if escolha == '1':
        soma()
    elif escolha == '2':
        subtracao()
    elif escolha == '3':
        multiplicacao()
    elif escolha == '4':
        divisao()
    elif escolha == '5':
        raiz_quadrada()
    elif escolha == '6':
        seno()
    elif escolha == '7':
        cosseno()
    elif escolha == '8':
        tangente()
    elif escolha == '9':
        logaritmo()
    elif escolha == '10':
        logaritmo_base10()
    elif escolha == '11':
        logaritmo_basee()
    else:
        print("Opção inválida")

    novamente = input("Deseja realizar outra operação? (s/n): ")
    if novamente.lower() != 's':
        break







   