from tkinter import *
from tkinter import ttk

# Importando Pillow

from PIL import Image, ImageTk

# Cores

co0 = "#444466"  # Preto
co1 = "#feffff"  # Branco
co2 = "#6f9fbd"  # Azul
co3 = "#38576b"  # Valor
co4 = "#403d3d"  # Letra
co5 = "#ef5350"  # Vermelho
co6 = "#f7ff08"  #amarelo

# Criando janelas

janela = Tk()
janela.title('')
janela.geometry('550x510')
janela.configure(bg=co1)

ttk.Separator(janela, orient=HORIZONTAL).grid(row=0, columnspan=1, ipadx=272)

estilo = ttk.Style(janela)
estilo.theme_use("clam")

# Criando frame Pokemon
framePokemon = Frame(janela, width=550, height=290, relief='flat')
framePokemon.grid(row=1, column=0)
# framePokemon.configure(bg=co0)

# Criando label

# Nome
pokeNome = Label(framePokemon, text='Pikachu', relief='flat', anchor=CENTER, font=('Fixedsys 20'), bg=co1, fg=co4)
pokeNome.place(x=12, y=15)
pokeNome.configure(bg=co6)

# Categoria
pokeTipo = Label(framePokemon, text='Eletrico', relief='flat', anchor=CENTER, font=('Ivy 10 bold'), bg=co1, fg=co0)
pokeTipo.place(x=12, y=50)

# Id
pokeId = Label(framePokemon, text='#025', relief='flat', anchor=CENTER, font=('Ivy 10 bold'), bg=co1, fg=co0)
pokeId.place(x=12, y=75)

# Imagem do pokemon

imagemPokemon = Image.open("C:\Projetos pessoais\Python\Pokedex\images\pikachu.png")
imagemPokemon = imagemPokemon.resize((238, 238))
imagemPokemon = ImageTk.PhotoImage(imagemPokemon)

pokeImagem = Label(framePokemon, image=imagemPokemon, relief='flat', bg=co1, fg=co0)
pokeImagem.place(x=12, y=75)

pokeTipo.lift()
pokeId.lift()

# Status

pokeStatus = Label(janela, text='Status', relief='flat', anchor=CENTER, font=('Verdana 20'), bg=co1, fg=co0)
pokeStatus.place(x=15, y=310)

# Hp

pokeHp = Label(janela, text='HP: 300', relief='flat', anchor=CENTER, font=('Verdana 10'), bg=co1, fg=co4)
pokeHp.place(x=15, y=360)

# Ataque
pokeAtack = Label(janela, text='Ataque: 600', relief='flat', anchor=CENTER, font=('Verdana 10'), bg=co1, fg=co4)
pokeAtack.place(x=15, y=385)

# Defesa
pokeDef = Label(janela, text='Defesa: 500', relief='flat', anchor=CENTER, font=('Verdana 10'), bg=co1, fg=co4)
pokeDef.place(x=15, y=410)

# Velocidade
pokeVel = Label(janela, text='Velocidade: 200', relief='flat', anchor=CENTER, font=('Verdana 10'), bg=co1, fg=co4)
pokeVel.place(x=15, y=435)

# Total
pokeTotal = Label(janela, text='Total: 1600', relief='flat', anchor=CENTER, font=('Verdana 10'), bg=co1, fg=co4)
pokeTotal.place(x=15, y=460)

# Habilidades

pokeHab = Label(janela, text='Habilidades', relief='flat', anchor=CENTER, font=('Verdana 20'), bg=co1, fg=co0)
pokeHab.place(x=180, y=310)

# Habilidade 1

pokeHab1 = Label(janela, text='Choque do trovão', relief='flat', anchor=CENTER, font=('Verdana 10'), bg=co1, fg=co4)
pokeHab1.place(x=195, y=360)

# Habilidade 2
pokeHab2 = Label(janela, text='Calda de Ferro', relief='flat', anchor=CENTER, font=('Verdana 10'), bg=co1, fg=co4)
pokeHab2.place(x=195, y=385)

# Habilidade 3
pokeHab3 = Label(janela, text='Bola Eletrica', relief='flat', anchor=CENTER, font=('Verdana 10'), bg=co1, fg=co4)
pokeHab3.place(x=195, y=410)

# Habilidade 4
pokeHab4 = Label(janela, text='Ataque Rapido', relief='flat', anchor=CENTER, font=('Verdana 10'), bg=co1, fg=co4)
pokeHab4.place(x=195, y=435)

# Criando botões de navegação

# Imagem do pokemon

imagemPokemon1 = Image.open("C:\Projetos pessoais\Python\Pokedex\images\cabeca-pikachu.png")
imagemPokemon1 = imagemPokemon1.resize((40, 40))
imagemPokemon1 = ImageTk.PhotoImage(imagemPokemon1)

btnPokeImagem1 = Button(framePokemon, image=imagemPokemon1, relief='flat', overrelief=RIDGE, compound=LEFT, anchor=NW, padx=5, font=('Verdana 12'), bg=co1, fg=co0)
btnPokeImagem1.place(x=260, y=75)

janela.mainloop()
