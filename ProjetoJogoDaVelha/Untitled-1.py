from tkinter import *
from tkinter import messagebox, Scrollbar
import pyodbc

# ---- Criando Funções ----

def mensagem():
    messagebox.showinfo("Mensagem", "Bem-vindo ao meu programa Python!")

def matchCase():
    resultado = messagebox.askyesnocancel("ESTRUTURA DE ESCOLHA", "ESCOLHA SIM, NÃO OU CANCELAR!")
    if resultado is True:
        messagebox.showinfo("RESULTADO", "VOCÊ ESCOLHEU SIM")
    elif resultado is False:
        messagebox.showinfo("RESULTADO", "VOCÊ ESCOLHEU NÃO")
    elif resultado is None:
        messagebox.showinfo("RESULTADO", "VOCÊ ESCOLHEU CANCELAR")
    else:
        messagebox.showinfo("RESULTADO", "VOCÊ ESCOLHEU SAIR")

def DesvioCond():
    if messagebox.askokcancel("DESVIO CONDICIONAL", "ESCOLHA OK OU CANCELAR!"):
        messagebox.showinfo("RESULTADO", "VOCÊ ESCOLHEU SIM")
    else:
        messagebox.showinfo("RESULTADO", "VOCÊ ESCOLHEU CANCELAR!")

    resultadoDoBotoes = messagebox.askyesnocancel("DESVIO CONDICIONAL ENCADEADO/ANINHADO", "ESCOLHA SIM, NÃO OU CANCELAR!")
    if resultadoDoBotoes is True:
        messagebox.showinfo("RESULTADO", "VOCÊ ESCOLHEU SIM")
    elif resultadoDoBotoes is False:
        messagebox.showinfo("RESULTADO", "VOCÊ ESCOLHEU NÃO")
    elif resultadoDoBotoes is None:
        messagebox.showinfo("RESULTADO", "VOCÊ ESCOLHEU CANCELAR")
    else:
        messagebox.showinfo("RESULTADO", "VOCÊ ESCOLHEU SAIR")

def impTxtWhile():
    lstbtxPreferencias.delete(0, END)
    try:
        arqPreferencias = open(r"C:\Curso programar\Python\Preferencias.txt", "r", encoding="utf-8")
        strLinhaLida = arqPreferencias.readline()

        while strLinhaLida != "":
            lstbtxPreferencias.insert(END, strLinhaLida)
            strLinhaLida = arqPreferencias.readline()

        arqPreferencias.close()

    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao importar arquivo: {str(e)}")

def impTxtFor():
    lstbtxPreferencias.delete(0, END)
    try:
        arqPreferencias = open(r"C:\Curso programar\Python\Preferencias.txt", "r", encoding="utf-8")
        arrStrLinhas = arqPreferencias.readlines()

        arqPreferencias.close()
        for item in range(len(arrStrLinhas)):
            item = arrStrLinhas[item]
            lstbtxPreferencias.insert(END, item)

    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao importar arquivo: {str(e)}")

def impTxtForEach():
    lstbtxPreferencias.delete(0, END)
    try:
        with open(r"C:\Curso programar\Python\Preferencias.txt", "r", encoding="utf-8") as arqPreferencias:
            for linha in arqPreferencias:
                lstbtxPreferencias.insert(END, linha)

    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao importar arquivo: {str(e)}")

def impBdConectado():
    try:
        connectionString = (
            'Driver={Microsoft Access Driver (*.mdb, *.accdb)};'
            'DBQ=C:\Curso programar\Python\Preferencias_02_281220231.accdb;'
        )
        objConexao = pyodbc.connect(connectionString)
        objLeitorBd = objConexao.cursor()
        srtSQL = "SELECT * FROM Preferencias_2"
        objLeitorBd.execute(srtSQL)

        preferencias = []
        registro = objLeitorBd.fetchone()

        while registro is not None:
            preferencias.append(registro.Descricao)
            registro = objLeitorBd.fetchone()

        objLeitorBd.close()
        objConexao.close()

        atualizarLista(preferencias)

    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao importar arquivo: {str(e)}")

def atualizarLista(preferencias):
    lstbtxPreferencias.delete(0, END)

    for linha in preferencias:
        lstbtxPreferencias.insert(END, linha)

def limpaTxt():
    lstbtxPreferencias.delete(0, END)

def impBdDesconectado():
    try:
        connectionString = (
            'Driver={Microsoft Access Driver (*.mdb, *.accdb)};'
            'DBQ=C:\Curso programar\Python\Preferencias_02_281220231.accdb;'
        )
        objConexao = pyodbc.connect(connectionString)
        objLeitorBd = objConexao.cursor()
        srtSQL = "SELECT * FROM Preferencias_2"
        objLeitorBd.execute(srtSQL)

        preferencias = []
        registro = objLeitorBd.fetchall()

        for linha in registro:
            preferencias.append(linha[0])

        objLeitorBd.close()
        objConexao.close()

        atualizarLista(preferencias)

    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao importar arquivo: {str(e)}")

# ---- Criando Cores ---- #

co0 = "#000000"  # Preto
co1 = "#feffff"  # Branco
co2 = "#230aff"  # Azul
co3 = "#00b812"  # Verde
co4 = "#c9c9c9"  # Prata
co5 = "#ef5350"  # Vermelho
co6 = "#b839ab"  # Rosa
co7 = "#f7ff00"  # Amarelo
co8 = "#403d3d"  # Marrom Escuro

# ---- Criando Janela Principal---- #

janela = Tk()
janela.title("Importar Banco de Dados")
janela.geometry("350x500")
janela.configure(bg=co2)

# --- Criando Barra de Rolagem --- #

scroll = Scrollbar(janela)
scroll.pack(side=RIGHT, fill=Y)

# ---- Criando Frame Principal ---- #

frameCima = Frame(janela, width=500, height=300, relief=GROOVE)
frameCima.grid(row=1, column=0)
frameCima.configure(bg=co2)

# ---- Criando Label ---- #

lstbtxPreferencias = Listbox(frameCima, relief=GROOVE, width=23, height=20, selectmode="multiple", yscrollcommand=scroll.set)
lstbtxPreferencias.grid(row=0, column=1, rowspan=10, padx=180, pady=5)
lstbtxPreferencias.pack(side=LEFT, fill=BOTH)
scroll.config(command=lstbtxPreferencias.yview)

# --- Criando Largura dos botoes ---- #
btnWidth = 25
btnHeight = 1

# ---- Criando Botões ----

btnMensagem = Button(frameCima, text="Mensagem", relief=RAISED, overrelief=RIDGE, anchor=CENTER, font="Roboto 8 bold", bg=co4, fg=co0,
                     command=mensagem)
btnMensagem.place(x=10, y=10)
btnMensagem.configure(width=btnWidth, height=btnHeight)

btnDesvCond = Button(frameCima, text="Desvio Condicional", relief=RAISED, overrelief=RIDGE, anchor=CENTER, font="Roboto 8 bold", bg=co4, fg=co0,
                        command=DesvioCond)
btnDesvCond.place(x=10, y=40)
btnDesvCond.configure(width=btnWidth, height=btnHeight)

btnMatchCase= Button(frameCima, text="Match Case", relief=RAISED, overrelief=RIDGE, anchor=CENTER, font="Roboto 8 bold", bg=co4, fg=co0,
                     command=matchCase)
btnMatchCase.place(x=10, y=70)
btnMatchCase.configure(width=btnWidth, height=btnHeight)

btnImpTxtWhile = Button(frameCima, text="Importar Txt While", relief=RAISED, overrelief=RIDGE, anchor=CENTER, font="Roboto 8 bold", bg=co4, fg=co0,
                        command=impTxtWhile)
btnImpTxtWhile.place(x=10, y=100)
btnImpTxtWhile.configure(width=btnWidth, height=btnHeight)

btnImpTxtFor = Button(frameCima, text="Importar Txt For", relief=RAISED, overrelief=RIDGE, anchor=CENTER, font="Roboto 8 bold", bg=co4, fg=co0,
                        command=impTxtFor)
btnImpTxtFor.place(x=10, y=130)
btnImpTxtFor.configure(width=btnWidth, height=btnHeight)

btnImpTxtForEach = Button(frameCima, text="Importar Txt For Each", relief=RAISED, overrelief=RIDGE, anchor=CENTER, font="Roboto 8 bold", bg=co4, fg=co0,
                        command=impTxtForEach)
btnImpTxtForEach.place(x=10, y=160)
btnImpTxtForEach.configure(width=btnWidth, height=btnHeight)

btnImpBdConectado= Button(frameCima, text="Importar BD Conectado", relief=RAISED, overrelief=RIDGE, anchor=CENTER, font="Roboto 8 bold", bg=co4, fg=co0,
                        command=impBdConectado)
btnImpBdConectado.place(x=10, y=190)
btnImpBdConectado.configure(width=btnWidth, height=btnHeight)

btnImpBdDesconectado = Button(frameCima, text="Importar BD Desconectado", relief=RAISED, overrelief=RIDGE, anchor=CENTER, font="Roboto 8 bold", bg=co4, fg=co0,
                        command=impBdDesconectado)
btnImpBdDesconectado.place(x=10, y=220)
btnImpBdDesconectado.configure(width=btnWidth, height=btnHeight)

btnLimpaTxt = Button(frameCima, text="Limpar Texto", relief=RAISED, overrelief=RIDGE, anchor=CENTER, font="Roboto 8 bold", bg=co5, fg=co0,
                        command=limpaTxt)
btnLimpaTxt.place(x=10, y=250)
btnLimpaTxt.configure(width=btnWidth, height=btnHeight)

janela.mainloop()
