import sqlite3

from tasks.menu import exibir_menu
from tasks.crud import salvar, excluir, listar


contatos = []
opcao = 1


while opcao != 0:

    opcao = exibir_menu()

    if opcao == 1:
        print("Cadastrando...")

        nome = input("Informe o nome: ")
        numero = input("Informe o numero: ")

        salvar(nome=nome, numero=numero, contatos=contatos)

    elif opcao == 2:
        print("Listando...")

        with sqlite3.connect("contatos.db") as conn:
            cursor = conn.cursor()

            contatos = listar(cursor=cursor)

        for contato in contatos:
            print("-" * 100)
            print(f"Nome: {contato[0]}\nNúmero: {contato[1]}")

    elif opcao == 3:
        print("Excluindo...")

        nome_excluir = input("Informe o nome do contato que deseja remover: ")

        excluir(contatos=contatos, nome_excluir=nome_excluir)

        print("Contato removido com sucesso!")
