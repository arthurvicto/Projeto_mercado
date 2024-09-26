from db import conectar

def adicionar_cliente(nome, email):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("INSERT INTO clientes (nome, email) VALUES (%s, %s)", (nome, email))
    conexao.commit()
    cursor.close()
    conexao.close()

def adicionar_produto(nome, preco, quantidade):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("INSERT INTO produtos (nome, preco, quantidade) VALUES (%s, %s, %s)", (nome, preco, quantidade))
    conexao.commit()
    cursor.close()
    conexao.close()

def adicionar_venda(id_cliente, id_produto, quantidade, data_venda):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("INSERT INTO vendas (id_cliente, id_produto, quantidade, data_venda) VALUES (%s, %s, %s, %s)", 
                   (id_cliente, id_produto, quantidade, data_venda))
    conexao.commit()
    cursor.close()
    conexao.close()

def buscar_cliente_por_nome(nome):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("SELECT id, nome FROM clientes WHERE nome LIKE %s", (f'%{nome}%',))
    resultados = cursor.fetchall()
    cursor.close()
    conexao.close()
    return resultados

def buscar_produto_por_nome(nome):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("SELECT id, nome FROM produtos WHERE nome LIKE %s", (f'%{nome}%',))
    resultados = cursor.fetchall()
    cursor.close()
    conexao.close()
    return resultados
