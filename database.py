import sqlite3
from models import Agendamento

BANCO_DADOS = "agendaflow.db"

def conectar():
    """Abre a conexão com o banco SQLite e garante que a tabela exista"""
    conexao = sqlite3.connect(BANCO_DADOS)
    cursor = conexao.cursor()


    cursor.execute("""
    CREATE TABLE IF NOT EXISTS agendamentos (
        id INTEGER PRIMARY KEY,
        nome TEXT NOT NULL,
        servico TEXT NOT NULL,
        preco REAL NOT NULL,
        data TEXT NOT NULL,
        hora TEXT NOT NULL,
        status TEXT NOT NULL
    )
    """)

    conexao.commit()
    return conexao


def carregar_agendamentos():
    """Busca todas as linhas da tabela e transforma em objetos Agendamento."""
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute('SELECT id, nome, servico, preco, data, hora, status FROM agendamentos')
    linhas = cursor.fetchall()
    conexao.close()

    agendamentos = []
    for l in linhas:
        agendamento = Agendamento(
            id=l[0],
            nome=l[1],
            servico=l[2],
            preco=l[3],
            data=l[4],
            hora=l[5],
            status=l[6]
        )
        agendamentos.append(agendamento)

    return agendamentos


def salvar_agendamentos(agendamentos):
    """Salva ou atualiza os objetos Agendamento no banco de dados."""
    conexao = conectar()
    cursor = conexao.cursor()

    for a in agendamentos:
        cursor.execute("""
        INSERT OR REPLACE INTO agendamentos (id, nome, servico, preco, data, hora, status)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (a.id, a.nome, a.servico, a.preco, a.data, a.hora, a.status))

    conexao.commit()
    conexao.close()


