import tkinter as tk
from models import adicionar_cliente

def abrir_cadastro_cliente():
    janela = tk.Tk()
    janela.title("Cadastrar Cliente")

    tk.Label(janela, text="Nome").pack()
    nome = tk.Entry(janela)
    nome.pack()

    tk.Label(janela, text="Email").pack()
    email = tk.Entry(janela)
    email.pack()

    def cadastrar():
        adicionar_cliente(nome.get(), email.get())
        tk.Label(janela, text="Cliente cadastrado com sucesso!").pack()

    tk.Button(janela, text="Cadastrar", command=cadastrar).pack()
    janela.mainloop()
