from tkinter import Tk, Frame, Label, Entry, Button, messagebox
from tkinter import ttk

# Cores
co0 = "#f0f3f5"  # preta
co1 = "#feffff"  # branca
co2 = "#3fb5a3"  # verde
co4 = "#403d3d"  # letra

# Credenciais de exemplo (substitua pelo seu próprio sistema de autenticação)
credenciais = {"admin": "admin", "usuario1": "senha1", "usuario2": "senha2"}

# Função para verificar as credenciais
def verificar_senha():
    nome = e_nome.get()
    senha = e_pass.get()

    if nome in credenciais and senha == credenciais[nome]:
        messagebox.showinfo('Login', f'Bem vindo, {nome}!')
        # Chama a função para criar a nova janela aqui
        nova_janela()
    else:
        messagebox.showwarning('Erro', 'Verifique seus dados e tente novamente')

# Função para criar a nova janela após o login bem-sucedido
def nova_janela():
    # Destruir todos os widgets nos frames
    for widget in frame_cima.winfo_children():
        widget.destroy()
    
    for widget in frame_baixo.winfo_children():
        widget.destroy()

    # Configurar widgets para a nova janela
    l_nome_nova = Label(frame_cima, text=f"Bem vindo, {e_nome.get()}!", height=1, anchor="ne", font=("Arial 25"), bg=co1, fg=co4)
    l_nome_nova.place(x=5, y=5)

    l_linha_nova = Label(frame_cima, width=275, text="", height=1, anchor="nw", font=("Arial 1"), bg=co2)
    l_linha_nova.place(x=10, y=45)

    l_nome_baixo = Label(frame_baixo, text=f"Seja bem vindo, {e_nome.get()}", height=1, anchor="nw", font=("Arial 15"), bg=co1, fg=co4)
    l_nome_baixo.place(x=5, y=105)

# Criando janela principal
janela = Tk()
janela.title("Login")
from tkinter import NW, RAISED, RIDGE

janela.geometry("300x300")
janela.configure(background=co1)
janela.resizable(width=False, height=False)

# Criando Frames
frame_cima = Frame(janela, width=300, height=50, bg=co1, relief="flat")
frame_cima.grid(row=0, column=0, pady=1, padx=0, sticky="nsew")
frame_baixo = Frame(janela, width=300, height=250, bg=co1, relief="flat")
frame_baixo.grid(row=1, column=0, pady=1, padx=0, sticky="nsew")

# Configurando widgets para o frame_cima
l_nome = Label(frame_cima, text="Login", height=1, anchor="ne", font=("Arial 25"), bg=co1, fg=co4)
l_nome.place(x=5, y=5)

l_linha = Label(frame_cima, width=275, text="", height=1, anchor=NW, font=("Arial 1"), bg=co2)
l_linha.place(x=10, y=45)

# Configurando widgets para o frame_baixo
l_nome = Label(frame_baixo, text="Nome *", height=1, anchor=NW, font=("Arial 10 bold"), bg=co1, fg=co4)
l_nome.place(x=10, y=20)
e_nome = Entry(frame_baixo, width=25, justify='left', font=("", 15), highlightthickness=1, relief="solid")
e_nome.place(x=14, y=50)

l_pass = Label(frame_baixo, text="Password *", height=1, anchor=NW, font=("Arial 10 bold"), bg=co1, fg=co4)
l_pass.place(x=10, y=95)
e_pass = Entry(frame_baixo, show='*', width=25, justify='left', font=("", 15), highlightthickness=1, relief="solid")
e_pass.place(x=14, y=125)

botao_confirmar = Button(frame_baixo, command=verificar_senha, text="Entrar", width=39, height=2, bg=co2, fg=co1, font=("Arial 8 bold"), relief=RAISED, overrelief=RIDGE)
botao_confirmar.place(x=15, y=180)

janela.mainloop()
