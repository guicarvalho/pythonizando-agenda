"""Applicaiton main module."""

import sqlite3

from database.connection import create_all, get_cursor
from database.dal import delete_by_name, find_all, save
from view.menu import show_menu_options


def init():
    """Initialize program."""
    option = -1

    while option != 0:
        option = show_menu_options()

        if option == 1:
            print("Cadastrando...")

            name = input("Informe o nome: ")
            phone = input("Informe o telefone: ")

            with get_cursor() as cursor:
                save(cursor=cursor, name=name, phone=phone)

        elif option == 2:
            print("Listando...")

            with get_cursor() as cursor:
                contacts = find_all(cursor=cursor)

            for contact in contacts:
                print("-" * 100)
                print(f"Nome: {contact[0]}\nNúmero: {contact[1]}")

        elif option == 3:
            print("Excluindo...")

            name = input("Informe o name do contato que deseja remover: ")

            with get_cursor() as cursor:
                delete_by_name(cursor=cursor, name=name)

            print("Contato removido com sucesso!")


if __name__ == "__main__":
    create_all()
    init()
