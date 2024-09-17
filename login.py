# Importando as bibliotecas necessárias
import tkinter as tk  
from tkinter import messagebox 

# Função para verificar o login do usuário
def verificar_login():
    usuario = entry_usuario.get()
    senha = entry_senha.get()
 
    # Verifica se o usuário e senha são validos 
    if usuario == "admin" and senha == "1234":
        messagebox.showinfo("Informação de Login", "Efetuado com sucesso!")
        abrir_tela_principal()
    else:
        # Se as credenciais estão incorretas, exibe uma mensagem de erro
        messagebox.showerror("Erro", "Usuário ou senha inválidos!")
 
# Função para abrir a tela principal da aplicação
def abrir_tela_principal():
    tela_login.destroy()
    
    # Cria uma nova janela para a tela principal
    tela_principal = tk.Tk()
    # Define o título da janela
    tela_principal.title("Tela Principal")
    # Define o tamanho da janela 
    tela_principal.geometry("800x400")
    
    # Cria uma mensagem de boas-vindas e o adiciona à janela
    label_bem_vindo = tk.Label(tela_principal, text="Bem-vindo à Tela Principal!", font=("Arial", 16))
    label_bem_vindo.pack(pady=20)  # Adiciona um espaçamento vertical ao redor do rótulo
    
    # Cria um botão "Sair" que fecha a janela quando clicado
    botao_sair = tk.Button(tela_principal, text="Sair", command=tela_principal.quit)
    botao_sair.pack(pady=10)  # Adiciona um espaçamento vertical ao redor do botão
    
    # Inicia o loop principal da interface gráfica, exibindo a janela
    tela_principal.mainloop()
 
# Cria a janela da tela de login
tela_login = tk.Tk()
# Define o título da janela
tela_login.title("Tela de Login")
# Define o tamanho da janela 
tela_login.geometry("250x180")
 
# Cria um rótulo para o campo de entrada de usuário e o adiciona à janela
label_usuario = tk.Label(tela_login, text="Usuário:")
label_usuario.pack(pady=(20, 5))  

#  usuário inserir seu nome de usuário
entry_usuario = tk.Entry(tela_login)
entry_usuario.pack(pady=(0, 10))  
 
# Cria um rótulo para o campo de entrada de senha e o adiciona à janela
label_senha = tk.Label(tela_login, text="Senha:")
label_senha.pack(pady=(0, 5))

# usuário inserir sua senha, com os caracteres ocultos
entry_senha = tk.Entry(tela_login, show="*")
entry_senha.pack(pady=(0, 20))
 
# Cria um botão de login 
botao_login = tk.Button(tela_login, text="Login", command=verificar_login)
botao_login.pack()  # Adiciona o botão

# Inicia o loop principal 
tela_login.mainloop()
