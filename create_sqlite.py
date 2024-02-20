import csv
import sqlite3

DATA_PATH = 'bases_mail/segundo_emaill.csv'


# Função para criar o banco de dados e a tabela
def criar_banco_dados():
    conn = sqlite3.connect('dados.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS usuarios
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                 nome TEXT,
                 segundo_email TEXT)''')
    conn.commit()
    conn.close()


# Função para inserir dados do CSV no banco de dados
def inserir_dados_csv():
    conn = sqlite3.connect('dados.db')
    c = conn.cursor()

    with open(DATA_PATH, 'r', encoding='utf-8') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            nome = row['nome']
            segundo_email = row['segundo_email']
            c.execute('''INSERT INTO usuarios (nome, segundo_email)
                         VALUES (?, ?)''', (nome, segundo_email))
    
    conn.commit()
    conn.close()


# Executar as funções para criar o banco de dados e inserir os dados do CSV
criar_banco_dados()
inserir_dados_csv()
