import tkinter
from tkinter import *
from tkinter import ttk, messagebox

# ----- cores ----- #

co0 = "#FFFFFF"  # branca / white
co1 = "#333333"  # preta pesado / dark black
co2 = "#fcc058"  # laranja / orange
co3 = "#38576b"  # valor / value
co4 = "#3297a8"  # azul / blue
co5 = "#fff873"  # amarela / yellow
co6 = "#fcc058"  # laranja / orange
co7 = "#e85151"  # vermelha / red
co8 = co4        # +verde
co10 ="#fcfbf7"  # Branco
fundo = "#3b3b3b" #black

# ----- Criando janela principal ----- #

janela = Tk()
janela.title("Jogo da Velha")
janela.geometry("260x370")
janela.configure(bg=fundo)

# ----- Criando Frames ----- #

frameCima = Frame(janela, width=240, height=100, bg=co1, relief=RAISED)
frameCima.grid(row=0, column=0, sticky=NW, padx=10, pady=10)

frameBaixo = Frame(janela, width=240, height=300, bg=fundo, relief=FLAT)
frameBaixo.grid(row=1, column=0, sticky=NW)

# ----- Criando Labels para frames ----- #

labelX = Label(frameCima, text="X",height=1, relief=FLAT, anchor=CENTER, font=('Ivy, 40 bold'), bg=co1, fg=co7)
labelX.place(x=25, y=10)
labelX = Label(frameCima, text="Jogador 1",height=1, relief=FLAT, anchor=CENTER, font=('Ivy, 7 bold'), bg=co1, fg=co0)
labelX.place(x=17, y=70)
labelXPontos = Label(frameCima, text="0",height=1, relief=FLAT, anchor=CENTER, font=('Ivy, 30 bold'), bg=co1, fg=co0)
labelXPontos.place(x=80, y=20)

labelSeparador = Label(frameCima, text=":",height=1, relief=FLAT, anchor=CENTER, font=('Ivy, 30 bold'), bg=co1, fg=co0)
labelSeparador.place(x=110, y=15)

label0 = Label(frameCima, text="O",height=1, relief=FLAT, anchor=CENTER, font=('Ivy, 40 bold'), bg=co1, fg=co4)
label0.place(x=170, y=10)
label0 = Label(frameCima, text="Jogador 2",height=1, relief=FLAT, anchor=CENTER, font=('Ivy, 7 bold'), bg=co1, fg=co0)
label0.place(x=165, y=70)
labelXPontos0 = Label(frameCima, text="0",height=1, relief=FLAT, anchor=CENTER, font=('Ivy, 30 bold'), bg=co1, fg=co0)
labelXPontos0.place(x=130, y=20)

# ----- Criando Frame baixo ----- #

# Linhas Verticais

linha1 = Label(frameBaixo, text="",height=23, pady=5, relief=FLAT, anchor=CENTER, font=('Ivy, 5 bold'), bg=co0, fg=co7)
linha1.place(x=90, y=15)

linha2 = Label(frameBaixo, text="",height=23, pady=5, relief=FLAT, anchor=CENTER, font=('Ivy, 5 bold'), bg=co0, fg=co7)
linha2.place(x=174, y=15)

# Linhas Horizontais

linha3 = Label(frameBaixo, text="", width=200, padx=2, relief=FLAT, anchor=CENTER, font=('Ivy, 5 bold'), bg=co0, fg=co7)
linha3.place(x=30, y=63)

linha4 = Label(frameBaixo, text="", width=200, padx=2, relief=FLAT, anchor=CENTER, font=('Ivy, 1 bold'), bg=co0, fg=co7)
linha4.place(x=30, y=130)

# ----- Criando Botões ----- #

# Linha 0

btn0 = Button(frameBaixo, text="", width=3, height=1, relief=FLAT, font=('Ivy, 20 bold'), overrelief=RIDGE, bg=fundo, fg=co7)
btn0.place(x=30, y=15)

btn1 = Button(frameBaixo, text="", width=4, height=1, relief=FLAT, font=('Ivy, 20 bold'), overrelief=RIDGE, bg=fundo, fg=co7)
btn1.place(x=96, y=15)

btn2 = Button(frameBaixo, text="", width=3, height=1, relief=FLAT, font=('Ivy, 20 bold'), overrelief=RIDGE, bg=fundo, fg=co7)
btn2.place(x=180, y=15)

# Linha 1

btn3 = Button(frameBaixo, text="", width=3, height=1, relief=FLAT, font=('Ivy, 20 bold'), overrelief=RIDGE, bg=fundo, fg=co7)
btn3.place(x=30, y=75)

btn4 = Button(frameBaixo, text="", width=4, height=1, relief=FLAT, font=('Ivy, 20 bold'), overrelief=RIDGE, bg=fundo, fg=co7)
btn4.place(x=96, y=75)

btn5 = Button(frameBaixo, text="", width=3, height=1, relief=FLAT, font=('Ivy, 20 bold'), overrelief=RIDGE, bg=fundo, fg=co7)
btn5.place(x=180, y=75)

# Linha 2

btn6 = Button(frameBaixo, text="", width=3, height=1, relief=FLAT, font=('Ivy, 20 bold'), overrelief=RIDGE, bg=fundo, fg=co7)
btn6.place(x=30, y=135)

btn7 = Button(frameBaixo, text="", width=4, height=1, relief=FLAT, font=('Ivy, 20 bold'), overrelief=RIDGE, bg=fundo, fg=co7)
btn7.place(x=96, y=135)

btn8 = Button(frameBaixo, text="", width=3, height=1, relief=FLAT, font=('Ivy, 20 bold'), overrelief=RIDGE, bg=fundo, fg=co7)
btn8.place(x=180, y=135)

janela.mainloop()