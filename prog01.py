import sqlite3 
import os

connection_string = os.path.join(os.getcwd(), 'db.sqlite3')

conexao = sqlite3.connect(connection_string)

if __name__ == '__main__':
    # Comando para excluir a tabela tb_estados caso ela já exista.
    comando = 'DROP TABLE IF EXISTS tb_estados'
    # Criando um cursor que é necessário para executar comandos SQL.
    cursor = conexao.cursor()
    # Executando comando.
    cursor.execute(comando)

    # Criando tabela:

    # 1 - Definindo comando para criação.
    # CREATE TABLE nome_da_tabela = Cria a tabela.
    comando = '''
    CREATE TABLE tb_estados(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        sigla TEXT NOT NULL
    )'''
    cursor.execute(comando)

    lista_estados = [
        {"nome": "Acre", "sigla": "AC"},
        {"nome": "Alagoas", "sigla": "AL"},
        {"nome": "Amapá", "sigla": "AP"},
        {"nome": "Amazonas", "sigla": "AM"},
        {"nome": "Bahia", "sigla": "BA"},
        {"nome": "Ceará", "sigla": "CE"},
        {"nome": "Distrito Federal", "sigla": "DF"},
        {"nome": "Espírito Santo", "sigla": "ES"},
        {"nome": "Goiás", "sigla": "GO"},
        {"nome": "Maranhão", "sigla": "MA"},
        {"nome": "Mato Grosso", "sigla": "MT"},
        {"nome": "Mato Grosso do Sul", "sigla": "MS"},
        {"nome": "Minas Gerais", "sigla": "MG"},
        {"nome": "Pará", "sigla": "PA"},
        {"nome": "Paraíba", "sigla": "PB"},
        {"nome": "Paraná", "sigla": "PR"},
        {"nome": "Pernambuco", "sigla": "PE"},
        {"nome": "Piauí", "sigla": "PI"},
        {"nome": "Rio de Janeiro", "sigla": "RJ"},
        {"nome": "Rio Grande do Norte", "sigla": "RN"},
        {"nome": "Rio Grande do Sul", "sigla": "RS"},
        {"nome": "Rondônia", "sigla": "RO"},
        {"nome": "Roraima", "sigla": "RR"},
        {"nome": "Santa Catarina", "sigla": "SC"},
        {"nome": "São Paulo", "sigla": "SP"},
        {"nome": "Sergipe", "sigla": "SE"},
        {"nome": "Tocantins", "sigla": "TO"}
    ]
    for estado in lista_estados:
        nome = estado.get('nome')
        sigla = estado.get('sigla')
        comando = f"INSERT INTO tb_estados(nome, sigla) VALUES ('{nome}', '{sigla}');"
        cursor.execute(comando)
        print(f'Estado {nome} inserido com sucesso!')
    conexao.commit()

    print('-'*15, 'CONSULTA DE DADOS', '-'*15)
    # Visualizando os dados da tabela com o comando de consulta SELECT
    comando = 'SELECT * FROM tb_estados'

    resultado = cursor.execute(comando)

    # Métodos para trazer os dados:
    # 1 - Método fetchone, que traz apenas o primeiro resultado.
    print('Método fetchone: ', resultado.fetchone())
    
    # 2 - Método fetchmany(número), que traz a quantidade de registros de acordo com o número passado em (número).
    print('Método fetchmany: ', resultado.fetchmany(10))
    
    # 3 - Método fetchall, que traz todos os outros resultados.
    print('Método fetchall: ', resultado.fetchall())

    resultado = cursor.execute(comando)

    estados = resultado.fetchall()

    for estado in estados:
        saida = f'''Estado: {estado[1]}
Sigla: {estado[2]}
--------------------'''
        print(saida)

    cursor.close()
    conexao.close()
