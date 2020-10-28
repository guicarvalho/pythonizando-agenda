def show_menu_options():
    """Show menu options.

    Returns:
        Menu option the user has chosen.
    """
    return int(
        input(
            """
MENU
1 - Cadastrar
2 - Listar
3 - Remover
0 - Sair
=> """
        )
    )
