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
    print("12 - Potenciação")
    print("13 - Fatorial")
    print("14 - Combinação")
    print("15 - Permutação")
    print("16 - Arredonda")

def soma():
    nums = input("Digite os números separados por vírgula: ")
    lista = nums.split(",")
    resultado = sum([float(x) for x in lista])
    print("O resultado da soma é:", resultado)

def subtracao():
    nums = input("Digite os números separados por vírgula: ")
    lista = nums.split(",")
    resultado = float(lista[0])
    for i in range(1, len(lista)):
        resultado -= float(lista[i])
    print("O resultado da subtração é:", resultado)

def multiplicacao():
    nums = input("Digite os números separados por vírgula: ")
    lista = nums.split(",")
    resultado = 1
    for i in lista:
        resultado *= float(i)
    print("O resultado da multiplicação é:", resultado)

def divisao():
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    resultado = num1 / num2
    print("O resultado da divisão é:", resultado)

def raiz_quadrada():
    num = float(input("Digite o número: "))
    resultado = math.sqrt(num)
    print("O resultado da raiz quadrada é:", resultado)

def seno():
    num = float(input("Digite o número em radianos: "))
    resultado = math.sin(num)
    print("O resultado do seno é:", resultado)

def cosseno():
    num = float(input("Digite o número em radianos: "))
    resultado = math.cos(num)
    print("O resultado do cosseno é:", resultado)

def tangente():
    num = float(input("Digite o número em radianos: "))
    resultado = math.tan(num)
    print("O resultado da tangente é:", resultado)

def logaritmo():
    num = float(input("Digite o número: "))
    base = float(input("Digite a base: "))
    resultado = math.log(num, base)
    print("O resultado do logaritmo é:", resultado)

def logaritmo_base10():
    num = float(input("Digite o número: "))
    resultado = math.log10(num)
    print("O resultado do logaritmo base 10 é:", resultado)

def logaritmo_basee():
    num = float(input("Digite o número: "))
    resultado = math.log(num)
    print("O resultado do logaritmo base e é:", resultado)

def potenciacao():
    num1 = float(input("Digite a base: "))
    num2 = float(input("Digite o expoente: "))
    resultado = num1 ** num2
    print("O resultado da potenciação é:", resultado)

def fatorial():
    x = int(input("Digite um número: "))
    resultado = math.factorial(x)
    print("O resultado do fatorial é:", resultado)

def combinacao():
    n = int(input("Digite o valor de n: "))
    k = int(input("Digite o valor de k: "))
    resultado = math.comb(n, k)
    print("O resultado da combinação é:", resultado)

def permutacao():
    n = int(input("Digite o valor de n: "))
    k = int(input("Digite o valor de k: "))
    resultado = math.perm(n, k)
    print("O resultado da permutação é:", resultado)

def arredonda():
    x = float(input("Digite um número: "))
    d = int(input("Digite a quantidade de casas decimais: "))
    resultado = round(x, d)
    print("O resultado do arredondamento é:", resultado)

while True:
    print_menu()
    escolha = input("Digite a sua escolha (1/2/3/4/5/6/7/8/9/10/11/12/13/14/15/16): ")

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
        exponencial()
    elif escolha == '7':
        seno()
    elif escolha == '8':
        cosseno()
    elif escolha == '9':
        tangente()
    elif escolha == '10':
        logaritmo()
    elif escolha == '11':
        logaritmo_base10()
    elif escolha == '12':
        logaritmo_basee()
    elif escolha == '13':
        fatorial()
    elif escolha == '14':
        combinacao()
    elif escolha == '15':
        permutacao()
    elif escolha == '16':
        arredonda()
    else:
        print("Opção inválida")

    novamente = input("Deseja realizar outra operação? (s/n): ")
    if novamente.lower() != 's':
        break

