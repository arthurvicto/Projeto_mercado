import mysql.connector

def conectar():
    return mysql.connector.connect(
        host="localhost",
        user="root", 
        password="Tutu777", 
        database="vendas_db"
    )
