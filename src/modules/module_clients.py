from src.functions.select_items import select_client_name, select_client_id
from src.messages.instructions import instruction_return_menu
from src.modules.module_db_connection import manipulate_record
from src.queries.queries_clients import query_insert_client, \
    query_delete_client
from src.functions.generic_functions import introduce_module, confirm, wait_for_return_menu
from src.functions.display_values import display_all_clients


def module_clients():
    while True:
        introduce_module("menu > clients", instruction_return_menu)
        modules = [
            "1. Add a client",
            "2. Delete a client",
            "3. List all clients"
        ]
        for module in modules: print(module)
        select = input("\n> ")
        match select:
            case "m": break
            case "1": add_client()
            case "2": delete_client()
            case "3": list_clients()


def add_client():
    introduce_module("menu > clients > add a client", None)
    client = select_client_name()
    client_name = client[0]
    client_surname = client[1]
    if confirm():
        manipulate_record(query_insert_client, client_name, client_surname, None, None)
        wait_for_return_menu()


def delete_client():
    introduce_module("menu > clients > delete a client", None)
    client_id = select_client_id()
    if confirm():
        manipulate_record(query_delete_client, client_id, None, None, None)
        wait_for_return_menu()


def list_clients():
    introduce_module("menu > clients > list all clients", None)
    display_all_clients()
    wait_for_return_menu()