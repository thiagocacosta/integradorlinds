import sqlite3

# Conectar ao banco de dados SQLite (db.sqlite3 na mesma pasta)
conexao = sqlite3.connect('db.sqlite3')

# Verificar se a conexão foi bem-sucedida
cursor = conexao.cursor()
cursor.execute('SELECT sqlite_version();')
linha = cursor.fetchone()
print(f'Versão do SQLite => {linha[0]}')

# Executar uma consulta para verificar o banco de dados em uso
cursor.execute('PRAGMA database_list;')
banco = cursor.fetchall()
print(f'Banco de dados => {banco[0][1]}')

# Fechar a conexão
conexao.close()
