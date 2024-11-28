from src.functions.select_items import select_user_login, select_user_id
from src.messages.instructions import instruction_return_menu
from src.modules.module_db_connection import manipulate_record
from src.queries.queries_administration import \
    query_insert_administrator, query_change_password, query_delete_administrator
from src.functions.generic_functions import introduce_module, confirm, wait_for_return_menu
from src.functions.display_values import display_all_users


def module_administration():
    while True:
        introduce_module("menu > administration", instruction_return_menu)
        modules = [
            "1. Add a user",
            "2. Delete a user",
            "3. Change user's password",
            "4. List all users"
        ]
        for module in modules: print(module)
        select = input("\n> ")
        match select:
            case "m": break
            case "1": add_user()
            case "2": delete_user()
            case "3": change_password()
            case "4": list_users()


def add_user():
    introduce_module("menu > administration > add a user",None)
    login = select_user_login()
    password = input("Password: ")
    if confirm():
        manipulate_record(query_insert_administrator, login, password, None, None)
        wait_for_return_menu()


def delete_user():
    introduce_module("menu > administration > delete a user", None)
    user_id = select_user_id()
    if confirm():
        manipulate_record(query_delete_administrator, user_id, None, None, None)
        wait_for_return_menu()


def change_password():
    introduce_module("menu > administration > change user's password", None)
    user_id = select_user_id()
    new_password = input("New password: ")
    if confirm():
        manipulate_record(query_change_password, new_password, user_id, None, None)
        wait_for_return_menu()


def list_users():
    introduce_module("menu > administration > list all users", None)
    display_all_users()
    wait_for_return_menu()