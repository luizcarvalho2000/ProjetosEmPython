import tkinter as tk
from tkinter import messagebox
import mysql.connector
import requests

# Conectar-se ao banco de dados MySQL
db = mysql.connector.connect(
    host= "localhost",
    user= "root",
    password="Bufallo@2010",
    database="admin_vacas_leiteiras"
)
cursor = db.cursor()

# Função para cadastrar uma vaca
def cadastrar_vaca():
    # Obter os valores dos campos de entrada
    raca = entry_raca.get()
    peso = entry_peso.get()
    idade = entry_idade.get()
    leite = entry_leite.get()
    
    # Inserir os dados no banco de dados
    query = "INSERT INTO vacas (raca, peso, idade, leite) VALUES (%s, %s, %s, %s)"
    values = (raca, peso, idade, leite)
    cursor.execute(query, values)
    db.commit()
    
    # Limpar os campos de entrada após o cadastro
    entry_raca.delete(0, tk.END)
    entry_peso.delete(0, tk.END)
    entry_idade.delete(0, tk.END)
    entry_leite.delete(0, tk.END)
    
    # Exibir mensagem de sucesso
    messagebox.showinfo("Cadastro de Vaca", "Vaca cadastrada com sucesso!")

# Função para cadastrar um funcionário
def cadastrar_funcionario():
    # Obter os valores dos campos de entrada
    nome = entry_nome.get()
    cep = entry_cep.get()
    cpf = entry_cpf.get()
    
    # Pesquisar o endereço com base no CEP
    endereco = pesquisar_endereco_por_cep(cep)
    if endereco == "Endereço não encontrado":
        messagebox.showerror("Cadastro de Funcionário", "Endereço não encontrado")
        return
    
    # Inserir os dados no banco de dados
    query = "INSERT INTO funcionarios (nome, cep, endereco, cpf) VALUES (%s, %s, %s, %s)"
    values = (nome, cep, endereco, cpf)
    cursor.execute(query, values)
    db.commit()
    
    # Limpar os campos de entrada após o cadastro
    entry_nome.delete(0, tk.END)
    entry_cep.delete(0, tk.END)
    entry_cpf.delete(0, tk.END)
    
    # Exibir mensagem de sucesso
    messagebox.showinfo("Cadastro de Funcionário", "Funcionário cadastrado com sucesso!")

# Função para autenticar o login do funcionário
def autenticar_login():
    # Obter os valores dos campos de entrada
    usuario = entry_usuario_login.get()
    senha = entry_senha_login.get()
    
    # Verificar se o usuário e a senha correspondem aos registros do banco de dados
    query = "SELECT * FROM funcionarios WHERE usuario = %s AND senha = %s"
    values = (usuario, senha)
    cursor.execute(query, values)
    result = cursor.fetchone()
    
    if result:
        messagebox.showinfo("Login", "Login realizado com sucesso!")
        # Adicione aqui as funcionalidades adicionais após o login bem-sucedido
    else:
        messagebox.showerror("Login", "Usuário ou senha incorretos.")

# Função para pesquisar o endereço com base no CEP
def pesquisar_endereco_por_cep(cep):
    url = f"https://viacep.com.br/ws/{cep}/json/"
    response = requests.get(url)
    data = response.json()
    if "erro" not in data:
        endereco = data["logradouro"]
        bairro = data["bairro"]
        cidade = data["localidade"]
        uf = data["uf"]
        return f"{endereco}, {bairro}, {cidade} - {uf}"
    else:
        return "Endereço não encontrado"

# Função para consultar todas as vacas cadastradas
def consultar_vacas():
    # Executar a consulta no banco de dados
    query = "SELECT * FROM vacas"
    cursor.execute(query)
    result = cursor.fetchall()
    
    # Exibir os resultados em uma caixa de diálogo
    if result:
        messagebox.showinfo("Consulta de Vacas", "Vacas encontradas:\n\n" + "\n".join(str(row) for row in result))
    else:
        messagebox.showinfo("Consulta de Vacas", "Nenhuma vaca encontrada.")

# Função para atualizar os dados de uma vaca
def atualizar_vaca():
    # Obter o ID da vaca a ser atualizada
    vaca_id = entry_vaca_id.get()
    
    # Verificar se a vaca existe no banco de dados
    query = "SELECT * FROM vacas WHERE id = %s"
    values = (vaca_id,)
    cursor.execute(query, values)
    result = cursor.fetchone()
    
    if result:
        # Obter os novos valores dos campos de entrada
        raca = entry_raca.get()
        peso = entry_peso.get()
        idade = entry_idade.get()
        leite = entry_leite.get()
        
        # Atualizar os dados da vaca no banco de dados
        query = "UPDATE vacas SET raca = %s, peso = %s, idade = %s, leite = %s WHERE id = %s"
        values = (raca, peso, idade, leite, vaca_id)
        cursor.execute(query, values)
        db.commit()
        
        # Limpar os campos de entrada após a atualização
        entry_vaca_id.delete(0, tk.END)
        entry_raca.delete(0, tk.END)
        entry_peso.delete(0, tk.END)
        entry_idade.delete(0, tk.END)
        entry_leite.delete(0, tk.END)
        
        # Exibir mensagem de sucesso
        messagebox.showinfo("Atualização de Vaca", "Vaca atualizada com sucesso!")
    else:
        messagebox.showerror("Atualização de Vaca", "Vaca não encontrada.")

# Função para excluir uma vaca
def excluir_vaca():
    # Obter o ID da vaca a ser excluída
    vaca_id = entry_vaca_id.get()
    
    # Verificar se a vaca existe no banco de dados
    query = "SELECT * FROM vacas WHERE id = %s"
    values = (vaca_id,)
    cursor.execute(query, values)
    result = cursor.fetchone()
    
    if result:
        # Excluir a vaca do banco de dados
        query = "DELETE FROM vacas WHERE id = %s"
        cursor.execute(query, values)
        db.commit()
        
        # Limpar o campo de entrada após a exclusão
        entry_vaca_id.delete(0, tk.END)
        
        # Exibir mensagem de sucesso
        messagebox.showinfo("Exclusão de Vaca", "Vaca excluída com sucesso!")
    else:
        messagebox.showerror("Exclusão de Vaca", "Vaca não encontrada.")

# Função para criar a interface gráfica
def criar_interface():
    # Criar a janela principal
    janela = tk.Tk()
    janela.title("Administração de Vacas Leiteiras")
    
    # Criar rótulos e campos de entrada para os dados da vaca
    label_raca = tk.Label(janela, text="Raça:")
    label_raca.pack()
    entry_raca = tk.Entry(janela)
    entry_raca.pack()
    
    label_peso = tk.Label(janela, text="Peso:")
    label_peso.pack()
    entry_peso = tk.Entry(janela)
    entry_peso.pack()
    
    label_idade = tk.Label(janela, text="Idade:")
    label_idade.pack()
    entry_idade = tk.Entry(janela)
    entry_idade.pack()
    
    label_leite = tk.Label(janela, text="Leite diário:")
    label_leite.pack()
    entry_leite = tk.Entry(janela)
    entry_leite.pack()
    
    # Botão para cadastrar a vaca
    btn_cadastrar_vaca = tk.Button(janela, text="Cadastrar Vaca", command=cadastrar_vaca)
    btn_cadastrar_vaca.pack()
    
    # Criar rótulos e campos de entrada para os dados do funcionário
    label_nome = tk.Label(janela, text="Nome:")
    label_nome.pack()
    entry_nome = tk.Entry(janela)
    entry_nome.pack()
    
    label_cep = tk.Label(janela, text="CEP:")
    label_cep.pack()
    entry_cep = tk.Entry(janela)
    entry_cep.pack()
    
    label_cpf = tk.Label(janela, text="CPF:")
    label_cpf.pack()
    entry_cpf = tk.Entry(janela)
    entry_cpf.pack()
    
    # Botão para cadastrar o funcionário
    btn_cadastrar_funcionario = tk.Button(janela, text="Cadastrar Funcionário", command=cadastrar_funcionario)
    btn_cadastrar_funcionario.pack()
    
    # Criar rótulos e campos de entrada para o login do funcionário
    label_usuario_login = tk.Label(janela, text="Usuário:")
    label_usuario_login.pack()
    entry_usuario_login = tk.Entry(janela)
    entry_usuario_login.pack()
    
    label_senha_login = tk.Label(janela, text="Senha:")
    label_senha_login.pack()
    entry_senha_login = tk.Entry(janela, show="*")
    entry_senha_login.pack()
    
    # Botão para autenticar o login
    btn_login = tk.Button(janela, text="Login", command=autenticar_login)
    btn_login.pack()
    
    # Criar rótulos e campos de entrada para o ID da vaca
    label_vaca_id = tk.Label(janela, text="ID da Vaca:")
    label_vaca_id.pack()
    entry_vaca_id = tk.Entry(janela)
    entry_vaca_id.pack()
    
    # Botão para consultar uma vaca
    btn_consultar_vaca = tk.Button(janela, text="Consultar Vaca", command=consultar_vacas)
    btn_consultar_vaca.pack()
    
    # Botão para atualizar uma vaca
    btn_atualizar_vaca = tk.Button(janela, text="Atualizar Vaca", command=atualizar_vaca)
    btn_atualizar_vaca.pack()
    
    # Botão para excluir uma vaca
    btn_excluir_vaca = tk.Button(janela, text="Excluir Vaca", command=excluir_vaca)
    btn_excluir_vaca.pack()
    
    # Executar a interface gráfica
    janela.mainloop()

# Chamar a função para criar a interface gráfica
criar_interface()
