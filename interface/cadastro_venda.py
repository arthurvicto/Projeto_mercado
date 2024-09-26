import tkinter as tk
from tkinter import ttk
from models import adicionar_venda, buscar_cliente_por_nome, buscar_produto_por_nome

def abrir_cadastro_venda():
    janela = tk.Tk()
    janela.title("Registrar Venda")

    tk.Label(janela, text="Nome do Cliente").pack()
    nome_cliente = tk.Entry(janela)
    nome_cliente.pack()

    lista_clientes = ttk.Combobox(janela)
    lista_clientes.pack()

    def buscar_clientes():
        nome = nome_cliente.get()
        clientes = buscar_cliente_por_nome(nome)
        lista_clientes['values'] = [f"{cliente[0]} - {cliente[1]}" for cliente in clientes]

    tk.Button(janela, text="Buscar Clientes", command=buscar_clientes).pack()

    tk.Label(janela, text="Nome do Produto").pack()
    nome_produto = tk.Entry(janela)
    nome_produto.pack()

    lista_produtos = ttk.Combobox(janela)
    lista_produtos.pack()

    def buscar_produtos():
        nome = nome_produto.get()
        produtos = buscar_produto_por_nome(nome)
        lista_produtos['values'] = [f"{produto[0]} - {produto[1]}" for produto in produtos]

    tk.Button(janela, text="Buscar Produtos", command=buscar_produtos).pack()

    tk.Label(janela, text="Quantidade").pack()
    quantidade = tk.Entry(janela)
    quantidade.pack()

    tk.Label(janela, text="Data da Venda (AAAA-MM-DD)").pack()
    data_venda = tk.Entry(janela)
    data_venda.pack()

    def registrar_venda():
        try:
            id_cliente = int(lista_clientes.get().split(" - ")[0])
            id_produto = int(lista_produtos.get().split(" - ")[0])
            qtd = int(quantidade.get())
            data = data_venda.get()
            adicionar_venda(id_cliente, id_produto, qtd, data)
            tk.Label(janela, text="Venda registrada com sucesso!").pack()
        except IndexError:
            tk.Label(janela, text="Selecione um cliente e um produto válidos!").pack()

    tk.Button(janela, text="Registrar Venda", command=registrar_venda).pack()
    janela.mainloop()
