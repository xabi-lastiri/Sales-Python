from src.functions.select_items import select_product_designation, select_product_price, select_product_quantity, \
    select_product_id, select_family_name, select_family_id
from src.messages.error_messages import error_no_items_found
from src.messages.instructions import instruction_return_menu
from src.modules.module_db_connection import select_record, manipulate_record
from src.queries.queries_products import \
    query_insert_product, query_insert_family, query_delete_product, query_delete_family, \
    query_select_products_by_family
from src.functions.generic_functions import introduce_module, confirm, wait_for_return_menu


def module_products():
    while True:
        introduce_module("menu > products", instruction_return_menu)
        modules = [
        "1. Add a product",
        "2. Delete a product",
        "3. Add a family",
        "4. Delete a family",
        "5. List all products"
        ]
        for module in modules: print(module)
        select = input("\n> ")
        match select:
            case "m": break
            case "1": add_product()
            case "2": delete_product()
            case "3": add_family()
            case "4": delete_family()
            case "5": list_products()


def add_product():
    introduce_module("menu > products > add product", None)
    product_designation = select_product_designation()
    product_price = select_product_price()
    product_stock = select_product_quantity()
    product_family = select_family_id()
    if confirm():
        manipulate_record(query_insert_product, product_designation, product_price, product_stock, product_family)
        wait_for_return_menu()


def delete_product():
    introduce_module("menu > products > delete product", None)
    product_id = select_product_id()
    if confirm():
        manipulate_record(query_delete_product, product_id, None, None, None)
        wait_for_return_menu()


def add_family():
    introduce_module("menu > products > add family", None)
    family_name = select_family_name()
    if confirm():
        manipulate_record(query_insert_family, family_name, None, None, None)
        wait_for_return_menu()


def delete_family():
    introduce_module("menu > products > delete family", None)
    family_id = select_family_id()
    if confirm():
        manipulate_record(query_delete_family, family_id, None, None, None)
        wait_for_return_menu()


def list_products():
    introduce_module("menu > products > list products", None)
    family_id = select_family_id()
    products = select_record(query_select_products_by_family, "n", family_id, None)
    if products is None:
        print(error_no_items_found)
    else:
        for product in products:
            print(f"{product[0]} : {product[1]}, {product[2]} €, {product[3]} unit(s) in stock.")
    wait_for_return_menu()
