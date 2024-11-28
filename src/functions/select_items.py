from src.functions.check_values import check_item_exists, check_int_format, check_price_format
from src.functions.display_values import display_all_users, display_all_clients, display_all_families, display_all_products
from src.messages.error_messages import error_invalid_format, error_invalid_option, error_item_already_exists, \
    error_insufficient_stock
from src.modules.module_db_connection import select_record
from src.queries.queries_administration import query_select_administrator, query_select_administrator_id
from src.queries.queries_clients import query_select_client, query_select_client_id
from src.queries.queries_products import query_select_product, query_select_family_id, query_select_product_id, \
    query_select_family, query_select_product_stock


def select_client_id():
    while True:
        display_all_clients()
        client_id = input("\nClient ID: ")
        if not check_int_format(client_id):
            print(error_invalid_format)
        elif not check_item_exists(query_select_client_id, client_id, None):
            print(error_invalid_option)
        else:
            return client_id


def select_client_name():
    while True:
        display_all_clients()
        client_name = input("Client name: ").upper()
        client_surname = input("Client surname: ")
        if check_item_exists(query_select_client, client_name, client_surname):
            print(error_item_already_exists)
        else:
            return client_name, client_surname


def select_product_id():
    while True:
        display_all_products()
        product_id = input("\nProduct ID: ")
        if not check_int_format(product_id):
            print(error_invalid_format)
        elif not check_item_exists(query_select_product_id, product_id, None):
            print(error_invalid_option)
        else:
            return product_id


def select_product_designation():
    while True:
        display_all_products()
        product_designation = input("Product designation: ")
        if check_item_exists(query_select_product, product_designation, None):
            print(error_item_already_exists)
        else:
            return product_designation


def select_product_price():
    while True:
        product_price = input("Product price: ")
        return product_price if check_price_format(product_price) else False


def select_product_quantity():
    while True:
        product_quantity = input("Product quantity: ")
        return product_quantity if check_int_format(product_quantity) else print(error_invalid_format)


def select_sale_quantity(product_id):
    while True:
        sale_quantity = input("Select the quantity: ")
        available_stock = select_record(query_select_product_stock, 1, product_id, None)[0]
        if not check_int_format(sale_quantity):
            print(error_invalid_format)
        elif int(sale_quantity) > int(available_stock):
            print(error_insufficient_stock) and print(f"{available_stock} unit(s) available.")
        else:
            return sale_quantity


def select_family_id():
    while True:
        display_all_families()
        product_family = input("\nFamily ID: ")
        if not check_int_format(product_family):
            print(error_invalid_format)
        elif not check_item_exists(query_select_family_id, product_family, None):
            print(error_invalid_option)
        else:
            return product_family


def select_family_name():
    while True:
        display_all_families()
        family_name = input("Family name: ")
        if check_item_exists(query_select_family, family_name, None):
            print(error_item_already_exists)
        else:
            return family_name


def select_user_login():
    while True:
        display_all_users()
        login = input("\nLogin username: ")
        if check_item_exists(query_select_administrator, login, None):
            print(error_item_already_exists)
        else:
            return login


def select_user_id():
    while True:
        display_all_users()
        user_id = input("\nUser ID: ")
        if not check_int_format(user_id):
            print(error_invalid_format)
        elif not check_item_exists(query_select_administrator_id, user_id, None):
            print(error_invalid_option)
        else:
            return user_id