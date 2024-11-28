import datetime
from src.functions.select_items import select_sale_quantity, select_client_id, select_product_id
from src.messages.error_messages import error_no_items_found
from src.messages.instructions import instruction_return_menu
from src.modules.module_db_connection import select_record, manipulate_record
from src.queries.queries_products import query_select_product_price, \
    query_select_product_stock, query_update_stock
from src.queries.queries_sales import query_insert_sale, query_select_last_sale_id, query_insert_selling, \
    query_select_sales_per_product, query_select_sales_per_client, query_select_sales_by_user
from src.functions.generic_functions import introduce_module, confirm, wait_for_return_menu


def module_sales(user_id):
    while True:
        introduce_module("menu > sales", instruction_return_menu)
        modules = [
            "1. Sell",
            "2. Statistics"
        ]
        for module in modules:
            print(f"{module}")
        select = input("\n> ")
        match select:
            case "m": break
            case "1": sell(user_id)
            case "2": statistics()


def sell(user_id):
    introduce_module("menu > sales > sell", None)
    client_id = select_client_id()
    product_id = select_product_id()
    sale_quantity = select_sale_quantity(product_id)
    product_price = select_record(query_select_product_price, 1, product_id, None)[0]
    total = round(float(product_price) * int(sale_quantity))
    print(f"\nTotal due: {total} €")
    if confirm():
        date = datetime.date.today()
        # Step 1: create the record in sale table.
        manipulate_record(query_insert_sale, date, client_id, user_id, None)
        # Step 2: get the sale_id newly created.
        sale_id = select_record(query_select_last_sale_id, 1, None, None)[0]
        # Step 3: create the record in selling table.
        manipulate_record(query_insert_selling, sale_id, product_id, sale_quantity, None)
        # Step 4: calculate the new stock for the sold product.
        current_stock = select_record(query_select_product_stock, 1, product_id, None)[0]
        new_stock = int(current_stock) - int(sale_quantity)
        # Step 5: update the stock in product table.
        manipulate_record(query_update_stock, new_stock, product_id, None, None)
        wait_for_return_menu()


def statistics():
    while True:
        introduce_module("menu > sales > statistics", instruction_return_menu)
        modules = [
            "1. Show sales by product",
            "2. Show sales by client",
            "3. Show sales by user"
        ]
        for module in modules: print(module)
        select = input("\n> ")
        match select:
            case "m": break
            case "1": show_sales_by_product()
            case "2": show_sales_by_client()
            case "3": show_sales_by_user()


def show_sales_by_product():
    introduce_module("menu > sales > statistics > sales by product", None)
    result = select_record(query_select_sales_per_product, "n",None, None)
    if result is None:
        print(error_no_items_found)
    else:
        for product in result:
            print(
                f"{product[0]} : {product[1]}, {product[2]} sale(s), {product[3]} unit(s) sold, {round(product[4])} € turnover")
    wait_for_return_menu()


def show_sales_by_client():
    introduce_module("menu > sales > statistics > sales by client", None)
    result = select_record(query_select_sales_per_client, "n",None, None)
    if result is None:
        print(error_no_items_found)
    else:
        for client in result:
            print(
                f"{client[0]} : {client[1]} {client[2]},  {client[3]} sale(s), {round(client[4])} € turnover")
    wait_for_return_menu()


def show_sales_by_user():
    introduce_module("menu > sales > statistics > sales by user", None)
    result = select_record(query_select_sales_by_user, "n", None, None)
    if result is None:
        print(error_no_items_found)
    else:
        for user in result:
            print(
                f"{user[0]} : {user[1]}, {user[2]} sale(s), {round(user[3])} € turnover")
    wait_for_return_menu()
