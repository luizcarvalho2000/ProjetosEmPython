from tkinter import *
from tkinter import ttk

##### Cores #####

co0 = "#444466" # Preto
co1 = "#feffff" # Branco
co2 = "#4065a1" # Vermelho

janela = Tk()
janela.title("Calculadora de IMC")
janela.geometry("295x230")
janela.configure(bg=co1)



##### Frames #####

frame_cima = Frame(janela, width=295, height=40, bg=co1, pady=0, padx=0, relief="flat",)
frame_cima.grid(row=0, column=0, sticky=NSEW)

frame_baixo = Frame(janela, width=295, height=200, bg=co1, pady=0, padx=0, relief="flat",)
frame_baixo.grid(row=1, column=0, sticky=NSEW)

style = ttk.Style(janela)
style.theme_use("clam")


# ----------------- Frame cima ----------------- #

app_name = Label(frame_cima, text="Calculadora de IMC", width=23, height=1, padx=0, relief="flat", anchor="center", font=("Ivy 16 bold"), bg=co1, fg=co0)
app_name.place(x=0, y=2)

app_linha = Label(frame_cima, text="", width=400, height=1, relief="flat", anchor="nw", font=("Arial 1"), bg=co2, fg=co1)
app_linha.place(x=0, y=35)

# ----------------- Frame baixo ----------------- #

l_peso = Label(frame_baixo, text="Insira seu peso:", height=1, padx=0, relief="flat", anchor="center", font=('Ivy 10 bold'), bg=co1, fg=co0)
l_peso.grid(row=0, column=0, columnspan=1, sticky=NW, pady=10, padx=3)
e_peso = Entry(frame_baixo, width=5, font=('Ivy 10 bold'), justify="center", relief=SOLID)
e_peso.grid(row=0, column=1, columnspan=1, sticky=NSEW, pady=10, padx=3)

l_altura = Label(frame_baixo, text="Insira sua altura:", height=1, padx=0, relief="flat", anchor="center", font=('Ivy 10 bold'), bg=co1, fg=co0)
l_altura.grid(row=1,column=0, columnspan=1, sticky=NW, pady=10, padx=3)
e_altura = Entry(frame_baixo, width=5, font=('Ivy 10 bold'), justify="center", relief=SOLID)
e_altura.grid(row=1, column=1, columnspan=1, sticky=NSEW, pady=10, padx=3)

l_resultado = Label(frame_baixo, width=5, text="___", height=1, padx=5, pady=12, relief="flat", anchor="center", font=('Ivy 10 bold'), bg=co2, fg=co0)
l_resultado.place(x=175, y=85)

l_resultado_texto = Label(frame_baixo, width=37, text="", height=1, padx=0, pady=12, relief="flat", anchor="center", font=('Ivy 10 bold'), bg=co1, fg=co0)
l_resultado_texto.place(x=0, y=85)

# --------------- Definindo Funções --------------- #




def calcular():
    peso = float(e_peso.get())
    altura = float(e_altura.get())
    resultado = peso / altura

    if resultado < 18.5:
        l_resultado_texto["text"] = "Seu IMC é: {:.2f} - Abaixo do peso".format(resultado)
    elif resultado >= 18.5 and resultado < 24.9:
        l_resultado_texto["text"] = "Seu IMC é: {:.2f} - Peso normal".format(resultado)
    elif resultado >= 25 and resultado < 29.9:
        l_resultado_texto["text"] = "Seu IMC é: {:.2f} - Sobrepeso".format(resultado)
    elif resultado >= 30 and resultado < 34.9:
        l_resultado_texto["text"] = "Seu IMC é: {:.2f} - Obesidade grau 1".format(resultado)
    elif resultado >= 35 and resultado < 39.9:
        l_resultado_texto["text"] = "Seu IMC é: {:.2f} - Obesidade grau 2".format(resultado)
    elif resultado >= 40:
        l_resultado_texto["text"] = "Seu IMC é: {:.2f} - Obesidade grau 3".format(resultado)
    else:
        l_resultado_texto["text"] = "Erro!"

    l_resultado["text"] = "{:.2f}".format(resultado)

# --------------- Botão Calcular --------------- #

b_calcular = Button(frame_baixo, text="Calcular", width=34, height=1, overrelief=SOLID, bg=co2, fg="white", font=('Ivy 10 bold'), anchor="center", relief=RAISED, command=calcular)
b_calcular.place(x=0, y=150)

janela.mainloop()
