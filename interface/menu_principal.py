import tkinter as tk
from interface.cadastro_cliente import abrir_cadastro_cliente
from interface.cadastro_produto import abrir_cadastro_produto
from interface.cadastro_venda import abrir_cadastro_venda

def abrir_menu_principal():
    janela = tk.Tk()
    janela.title("Sistema de Vendas")

    tk.Label(janela, text="Menu Principal", font=("Arial", 16)).pack(pady=10)

    tk.Button(janela, text="Cadastrar Cliente", width=25, command=abrir_cadastro_cliente).pack(pady=5)
    tk.Button(janela, text="Cadastrar Produto", width=25, command=abrir_cadastro_produto).pack(pady=5)
    tk.Button(janela, text="Registrar Venda", width=25, command=abrir_cadastro_venda).pack(pady=5)

    janela.mainloop()
