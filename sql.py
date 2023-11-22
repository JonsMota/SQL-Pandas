import sqlite3
import pandas as pd

funcoes = {
    "0": "criar a variável df_data e carregar o arquivo csv nela",
    "1": "substitui o nome do index para 'index_name'",
    "2": "criar o banco de dados",
    "3": "exportar a variável 'df_data' para o banco de dados criado",
    "4": "cria uma tabela chamada 'products' com Id, NOME e PREÇO ",
    "5": "cria uma tabela chamada 'products' definindo tipagem  do índice, produto e preço",
    "6": "deletar tabela 'products' ou banco ",
    "7": "inserir informações tabela 'products' ou banco ",
    "8": "selecionar a primeira coluna da tabela data e carregar no DF",
    "9": "selecionar todas as colunas da tabela data e carregar no DF",
    "10": "selecionar onde a coluna A for maior que 200 e carregar no DF",
    "11": "selecionar onde a coluna A for maior que 200 e o B maior QUE 250 e carregar no DF",
    "12": "atualizar e definir a tabela 'data' na coluna A e o index_name='b' para o valor de 218",
    "13": "deletar a linha  1",
    "14": "PANDAS selecionar todas as colunas da tabela data",
    "15": "PANDAS selecionar onde a coluna A for maior que 200 e o B maior QUE 250",
    "20": "para SAIR"
}

while True:
    print(funcoes) 
    print("O que deseja fazer?__") 
    op = int(input())

    if op == 0:
        df_data =  pd.read_csv('bd_data.csv', index_col=0)
        print(df_data)
    elif op == 1:
        df_data.index.name = 'index_name'
        print(df_data)
    elif op == 2:
        conn = sqlite3.connect('web.db')
    elif op == 3:
        conn = sqlite3.connect('web.db')
        df_data.to_sql('data', conn, index_label='index_name')
    elif op == 4:
        c = conn.cursor()
        c.execute('CREATE TABLE products (product_id, product_name, price)')
    elif op == 5:
        c = conn.cursor()
        c.execute('CREATE TABLE products ([product_id] INTEGER PRIMARY KEY, [product_name] TEXT, [price] INTEGER)')
    elif op == 6:
        c = conn.cursor()
        c.execute('DROP TABLE products')
    elif op == 7:
        c = conn.cursor()
        c.execute('''INSERT INTO products (product_id, product_name, price) 
            VALUES 
            (1, 'Computer', 800), 
            (2, 'Printer', 200),   
            (3, 'Tablet', 300)    
        ''')
        conn.commit()
    elif op == 8:
        c = conn.cursor()
        c.execute("SELECT * FROM data")
        df = pd.DataFrame(c.fetchone())
        print("----------------------------")
        print(df)
        print("----------------------------")
    elif op == 9:
        c = conn.cursor()
        c.execute("SELECT * FROM data")
        df = pd.DataFrame(c.fetchall())
        print("----------------------------")
        print(df)
        print("----------------------------")
    elif op == 10:
        c = conn.cursor()
        c.execute("SELECT * FROM data WHERE A > 200")
        df = pd.DataFrame(c.fetchall())
        print("----------------------------")
        print(df)
        print("----------------------------")
    elif op == 11:
        c = conn.cursor()
        c.execute("SELECT * FROM data WHERE A > 200 AND B > 250")
        df = pd.DataFrame(c.fetchall())
        print("----------------------------")
        print(df)
        print("----------------------------")
    elif op == 12:
        c = conn.cursor()
        c.execute("UPDATE data SET A=218 WHERE index_name='b'")
        conn.commit()
        df = pd.DataFrame
        print("----------------------------")
        print(df)
        print("----------------------------")
    elif op == 13:
        c = conn.cursor()
        c.execute("DELETE FROM data WHERE index_name=2")
        conn.commit()
        df = pd.DataFrame
        print("----------------------------")
        print(df)
        print("----------------------------")

    elif op == 14:
        query =("SELECT * FROM data")
        df = pd.read_sql(query, con=conn, index_col='index_name')
        print("----------------------------")
        print(df)
        print("----------------------------")

    elif op == 15:
        query =("SELECT * FROM data WHERE A > 200 AND B > 250")
        df = pd.read_sql(query, con=conn)
        print("----------------------------")
        print(df)
        print("----------------------------")
    elif op == 20:
        break