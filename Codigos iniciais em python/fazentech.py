from time import sleep

# LISTA PARA ARMAZENAR OS CÓDIGOS DAS VACAS
lista = []

# FUNÇÃO MENU PRINCIPAL DO SISTEMA
def menu():
    sleep(0.5)
    print("=" * 70)
    print(' ' * 25, "SEJA BEM VINDO", ' ' * 25)
    print("=" * 70)
    sleep(1)
    print("""
    \033[1;32mMENU PRINCIPAL:\033[m

    Selecione uma opção abaixo:

    1) Digite zero para adicionar uma vaca leiteira nova [0]
    2) Digite um para ver quais vacas leiteiras já foram adicionadas [1]
    3) Digite dois, caso deseja buscar por uma vaca [2]
    4) Digite três, caso deseje excluir uma vaca de sua lista [3]
    5) Digite quatro para sair [4]
    """)

    print("=" * 70)
    lista.sort()
    n = leia_int('Digite: ')

    # Adicionar código de vaca
    if n == 0:
        adicionar()

    # Ver vacas adicionadas
    if n == 1:
        quantidade()

    # Buscar código de vacas por sequência binária
    if n == 2:
        num = leia_int2('Digite um código de vaca: ')
        busc = busca_binaria(lista, num)

        if busc:
            sleep(1)
            print(f"A vaca com o código {num} foi encontrada")
            sleep(2)
            print('\033[1;32mVoltando ao menu Principal\033[m')
            sleep(2)
            menu()
        else:
            print(f"Não foi encontrada vaca com o código {num}")
            while True:
                resp = resposta(f'Deseja adicionar esta vaca com códgio {num} [S/N]')
                if resp:
                    if num not in lista:
                        lista.append(num)
                        sleep(1)
                        print('Código da vaca adicionado com sucesso...')
                        sleep(1)
                        print('\033[1;32mVoltando ao menu Principal\033[m')
                        sleep(2)
                        menu()
                        break

    if n == 3:
        excluir()

    if n == 4:
        print("Saindo do programa...")
        sleep(2)
        exit()


# FUNÇÃO DE VALIDAÇÃO DO MENU
def leia_int(msg):
    while True:
        n1 = input(msg)
        if n1.isnumeric():
            valor = int(n1)
            if valor in [0, 1, 2, 3, 4]:
                return valor
            else:
                print('\033[0;31mERRO, escolha uma opção válida, entre 0 e 4\033[m')
        else:
            print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')


# VALIDAÇÃO FUNÇÃO ADICIONAR[0]
def leia_int2(msg):
    while True:
        n1 = input(msg)
        if n1.isnumeric():
            return int(n1)
        else:
            print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')


# CASO O USUÁRIO NÃO DIGITE S OU N, MOSTRA ERRO
def resposta(msg):
    while True:
        p = input(msg).upper()
        if p == 'S' or p == 'N':
            if p == 'S':
                return True
            else:
                return False
            menu()
            break
        else:
            print('\033[0;31mERRO: Digite S para Sim e N para Não\033[m')


# FUNÇÃO PARA ADICIONAR UMA VACA LEITEIRA [0]
def adicionar():
    while True:
        add = leia_int2('Digite o código da vaca que deseja adicionar: ')
        if add < 1:
            print('Error! O código da vaca não pode ser zero')
        elif add not in lista:
            lista.append(add)
            print('Código da vaca adicionado com sucesso...')
        else:
            print('\033[0;31mERRO! O código desta vaca já foi adicionado\033[m')
        resp = resposta('Deseja adicionar outro código de vaca? [S/N]')
        if not resp:
            break


# FUNÇÃO PARA SABER QUAIS VACAS LEITEIRAS JÁ FORAM ADICIONADAS [1]
def quantidade():
    for i in lista:
        sleep(0.01)
        print(f'{i}', end=" -- ")
        sleep(1)
    print(f'\nForam adicionados {len(lista)} códigos de vacas')
    resposta('Digite S para fechar o programa ou N para voltar ao menu [S/N]: ')


# FUNÇÃO PARA BUSCAR UMA VACA EM BINÁRIO [2]
def busca_binaria(lists, item):
    prim = 0
    ult = len(lists) - 1
    found = False
    while prim <= ult and not found:
        meio = (prim + ult) // 2
        if lists[meio] == item:
            found = True
        else:
            if item < lists[meio]:
                ult = meio - 1
            else:
                prim = meio + 1
    return found


# FUNÇÃO PARA EXCLUIR UMA VACA DO SISTEMA [3]
def excluir():
    number = leia_int2('Digite o código da vaca que deseja remover: ')
    while number != 0:
        if number in lista:
            lista.remove(number)
            print('Código da vaca removido com sucesso')
            sleep(2)
            print('\033[1;32mVoltando ao menu Principal\033[m')
            sleep(2)
            menu()
            break
        else:
            print('\033[1;31mERROR! NÃO FOI POSSÍVEL REMOVER! \nCódigo da vaca não encontrado\033[m')
            sleep(1)
            number = leia_int2("\033[1;33mDigite 0 para voltar ao menu principal ou\033[m\nDigite outro código de vaca que deseje excluir: ")
            menu()


# EXECUÇÃO DO PROGRAMA
lista = [2009, 1530, 1670, 1790, 2001]
menu()
print("=" * 70)
print('Finalizando Programa...')
sleep(3)

