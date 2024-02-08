import random
import tkinter as tk
from tkinter import messagebox

# definindo as configurações do jogo

NUM_LINHAS = 4
NUM_COLUNAS = 4
CARD_SIZE_W = 10
CARD_SIZE_H = 5
CORES_CARD = ['red', 'green', 'yellow', 'purple', 'orange', 'cyan', 'magenta']
COR_FUNDO = "#343a40"
COR_LETRA = '#ffffff'
FONT_STYLE = ('Arial', 12, 'bold')
MAX_TENTATIVAS = 25


# Criar uma grade aleatoria de cores para os cartas
def create_card_grid():
    cor = CORES_CARD * 2
    random.shuffle(cor)
    grid = []

    for _ in range(NUM_LINHAS):
        linhas = []
        for _ in range(NUM_COLUNAS):
            cor = CORES_CARD.pop()
            linhas.append(cor)
        for _ in range(NUM_COLUNAS):
            cor = CORES_CARD.pop()
            linhas.append(cor)
        grid.append(linhas)
    return grid


# Lidar com clique do jogador em carta

def card_clicked(linhas, coluna):
    card = cartas[linhas][coluna]
    cor = card['bg']
    if cor == 'black':
        card['bg'] = grid[linhas][coluna]
        cartas_reveladas.append(card)
        if len(cartas_reveladas) == 2:
            check_match()


# Verificar se os dois cartas revelados sao iguais

def check_match():
    carta1, carta2 = cartas_reveladas
    if carta1['bg'] == carta2['bg']:
        carta1.after(1000, carta1.destroy)
        carta2.after(1000, carta2.destroy)
        cartas_correspondetes.extend([carta1, carta2])
        check_win()
    else:
        carta1.after(1000, lambda: carta1.config(bg='black'))
        carta2.after(1000, lambda: carta.config(bg='black'))
    cartas_reveladas.clear()
    update_score()


# verificar se o jogador ganhou o jogo

def check_win():
    if len(cartas_correspondetes) == NUM_LINHAS * NUM_COLUNAS:
        messagebox.showinfo('Parabens', 'Você ganhou o jogo!')

    janela.quit()


# Atualizar a pontuacao e verificar se o jogador pedeu

def update_score():
    global numero_tentativas
    numero_tentativas += 1
    label_tentativas.config(text='Tentativas: {}/{}'.format(numero_tentativas, MAX_TENTATIVAS))
    if numero_tentativas >= MAX_TENTATIVAS:
        messagebox.showinfo('fim de jogo', 'você perdeu o jogo!')
        janela.quit()


# Criando interface principal
janela = tk.Tk()
janela.title('Jogo de Memoria')
janela.configure(bg=COR_FUNDO)

# Criando interface principal
janela = tk.Tk()
janela.title('Jogo de Memoria')
janela.configure(bg=COR_FUNDO)

# Criar grade de cartas
grid = create_card_grid()
cartas = []
cartas_reveladas = []
cartas_correspondetes = []
numero_tentativas = 0

for linha in range(NUM_LINHAS):
    linha_de_cartas = []
    for col in range(NUM_COLUNAS):
        carta = tk.Button(janela, command=lambda r=linha, c=col: card_clicked(r, c),
                          width=CARD_SIZE_W, height=CARD_SIZE_H, bg='black', relief=tk.RAISED, bd=3)
        carta.grid(row=linha, column=col, padx=5, pady=5)
        linha_de_cartas.append(carta)
    cartas.append(linha_de_cartas)

# Personalizando o botao

button_style = {'activebackground': '#f8f9fa', 'font': FONT_STYLE, 'fg': COR_LETRA}
janela.option_add('Button', button_style)

# label para numero de tentativas

label_tentativas = tk.Label(janela, text='Tentativas: {}/{}'.format(numero_tentativas, MAX_TENTATIVAS), fg=COR_LETRA,
                            bg=COR_FUNDO,
                            font=FONT_STYLE)
label_tentativas.grid(row=NUM_LINHAS, columnspan=NUM_COLUNAS, padx=10, pady=10)

janela.mainloop()
