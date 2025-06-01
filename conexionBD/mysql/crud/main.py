# main.py
from db import create_database_and_tables
from menu.menu import ejecutar_menu

if __name__ == "__main__":
    create_database_and_tables()
    ejecutar_menu()
