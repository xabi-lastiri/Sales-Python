from src.messages.error_messages import error_no_items_found
from src.queries.queries_administration import query_select_administrators
from src.queries.queries_clients import query_select_clients
from src.queries.queries_products import query_select_families, query_select_products
from src.modules.module_db_connection import select_record


def display_all_users():
    query = query_select_administrators
    result = select_record(query, "n", None, None)
    print("Users list:\n")
    for user in result:
        print(f"{user[0]}. {user[1]}")


def display_all_clients():
    query = query_select_clients
    result = select_record(query, "n",None, None)
    if result is None:
        print(error_no_items_found)
    else:
        print("Clients list:\n")
        for client in result:
            print(f"{client[0]} : {client[1]} {client[2]}")


def display_all_families():
    query = query_select_families
    result = select_record(query, "n",None, None)
    if result is None:
        print(error_no_items_found)
    else:
        print("Families list:\n")
        for family in result:
            print(f"{family[0]} : {family[1]}")


def display_all_products():
    query = query_select_products
    result = select_record(query, "n",None, None)
    if result is None:
        print(error_no_items_found)
    else:
        print("Products list:\n")
        for product in result:
            print(f"{product[0]} : {product[1]}, {product[2]} €, {product[3]} unit(s) in stock, {product[4]}")