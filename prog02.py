import sqlite3 
import os
import csv

#  Parte I da atividade
connection_string = os.path.join(os.getcwd(), 'db_atividade.sqlite3')

conexao = sqlite3.connect(connection_string)

arquivo = 'cursos.csv'

if __name__ == '__main__':
    cursor = conexao.cursor()
    cursor.execute('DROP TABLE IF EXISTS tb_cursos')

    # Criando a tabela tb_cursos
    comando = '''
    CREATE TABLE tb_cursos(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        curso TEXT NOT NULL,
        carga_horaria INT NOT NULL,
        preco REAL NOT NULL
    )'''
    cursor.execute(comando)

    # Abrindo o arquivo csv
    with open(arquivo, 'r', newline='', encoding='utf-8') as arquivo_csv:
        leitor_csv = csv.reader(arquivo_csv, delimiter=';')

        next(leitor_csv)

        for linha in leitor_csv:
            curso = linha[0]
            carga_horaria = int(linha[1])
            preco = float(linha[2])
            # Inserindo os dados na tabela SQLite
            cursor.execute("INSERT INTO tb_cursos(curso, carga_horaria, preco) VALUES (?, ?, ?);", (curso, carga_horaria, preco))

    conexao.commit()

# Parte II da atividade
    # Encontrando a quantidade de cursos
    cursor.execute("SELECT COUNT(*) FROM tb_cursos;")
    quantidade_cursos = cursor.fetchone()[0]

    # Encontrando o curso com maior carga horária
    cursor.execute("SELECT curso, carga_horaria FROM tb_cursos ORDER BY carga_horaria DESC LIMIT 1;")
    curso_maior_carga_horaria, carga_horaria_maxima = cursor.fetchone()

    # Enconctrando o curso com maior preço
    cursor.execute("SELECT curso, preco FROM tb_cursos ORDER BY preco DESC LIMIT 1;")
    curso_maior_preco, preco_maximo = cursor.fetchone()

    # Escrevaendo as estatísticas em um arquivo separado
    with open('estatisticas_cursos.txt', 'w') as arquivo_estatisticas:
        arquivo_estatisticas.write("Estatísticas dos cursos\n\n")
        arquivo_estatisticas.write(f"Quantidade de cursos: {quantidade_cursos}\n")
        arquivo_estatisticas.write(f"Curso com a maior carga horária: {curso_maior_carga_horaria} ({carga_horaria_maxima} horas)\n")
        arquivo_estatisticas.write(f"Curso com o maior valor: {curso_maior_preco} (R$ {preco_maximo:.2f})\n")

    print("Estatísticas salvas com sucesso!")
