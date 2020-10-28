import sqlite3


with sqlite3.connect("contatos.db") as conn:
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS contato (nome TEXT, numero TEXT)")


def salvar(contatos, nome, numero):

    with sqlite3.connect("contatos.db") as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO contato VALUES (?, ?)", (nome, numero))


def listar(cursor):
    cursor.execute("SELECT * FROM contato")

    return cursor.fetchall()


def excluir(contatos, nome_excluir):
    for idx, contato in enumerate(contatos):
        if nome_excluir == contato["nome"]:
            break

    contatos.pop(idx)
