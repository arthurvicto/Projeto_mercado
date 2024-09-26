import tkinter as tk
from tkinter import messagebox
from models import adicionar_produto

def abrir_cadastro_produto():
    janela = tk.Tk()
    janela.title("Cadastro de Produto")

    tk.Label(janela, text="Nome do Produto").pack()
    nome = tk.Entry(janela)
    nome.pack()

    tk.Label(janela, text="Preço").pack()
    preco = tk.Entry(janela)
    preco.pack()

    tk.Label(janela, text="Quantidade").pack()
    quantidade = tk.Entry(janela)
    quantidade.pack()

    def salvar_produto():
        try:
            nome_produto = nome.get()
            preco_produto = float(preco.get())
            quantidade_produto = int(quantidade.get())
            
            if nome_produto and preco_produto and quantidade_produto >= 0:
                adicionar_produto(nome_produto, preco_produto, quantidade_produto)
                messagebox.showinfo("Sucesso", "Produto cadastrado com sucesso!")
            else:
                messagebox.showerror("Erro", "Preencha todos os campos corretamente!")
        except ValueError:
            messagebox.showerror("Erro", "Por favor, insira valores válidos!")

    tk.Button(janela, text="Salvar", command=salvar_produto).pack()

    janela.mainloop()
