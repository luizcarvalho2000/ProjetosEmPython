# Definindo a string a ser invertida
string = "Olá, mundo!"

# Criando uma lista vazia para armazenar os caracteres invertidos
inverted = []

# Percorrendo a string de trás para frente e adicionando cada caractere à lista inverted
for i in range(len(string)-1, -1, -1):
    inverted.append(string[i])

# Convertendo a lista de caracteres em uma string novamente
inverted_string = ''.join(inverted)

# Imprimindo a string invertida
print(inverted_string)
