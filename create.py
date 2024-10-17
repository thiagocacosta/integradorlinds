from date.conectar import cursor, conexao

def inserir_sensor(tipo, mac, lat, long, loc, resp, status, obs, unid):
    try:
        inserir_sensor = f"""INSERT INTO api_produto(tituloProduto, preco, descricao, imgProduto, catProduto, classProduto, exibirHome)
        values
        ('{tituloProduto}', '{preco}', '{descricao}', '{imgProduto}', '{catProduto}', '{classProduto}', '{exibirHome}');"""
        cursor.execute(inserir_sensor)
        conexao.commit()
    except:
        print('Erro ao adicionar os sensor...')
    

inserir_sensor("Optico", 0, -22.913075, -22.913075, 'LAB 500', 'Lindomar', 1, 'Sensor de teste', 'x')



import pandas as pd
import os

# Criando dados de exemplo para as ferramentas caseiras
data = {"}

# Criando um DataFrame com os dados
df = pd.DataFrame(data)


caminho_atual = os.getcwd()
c = caminho_atual.replace("\\", "/")

# Salvando o DataFrame em um arquivo CSV
df.to_csv(c+"/date/ferramentas.csv", index=False)
