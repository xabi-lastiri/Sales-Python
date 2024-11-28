from src.functions.select_items import select_product_price, select_product_quantity, select_product_id
from src.modules.module_db_connection import select_record, manipulate_record
from src.queries.queries_purchases import query_insert_purchase, query_select_last_purchase_id, query_insert_purchasing
from src.functions.generic_functions import introduce_module, \
    confirm, wait_for_return_menu
from src.queries.queries_products import query_select_product_stock, query_update_stock
import datetime


def module_purchases(user_id):
    introduce_module("menu > purchases", None)
    product_id = select_product_id()
    purchase_price = select_product_price()
    purchase_quantity = select_product_quantity()
    total_due = float(purchase_price) * int(purchase_quantity)
    print(f"\nTotal due {round(total_due)} €")
    if confirm():
        date = datetime.date.today()
        # Step 1: create the record in purchase table.
        manipulate_record(query_insert_purchase, date, user_id, None, None)
        # Step 2: get the purchase_id newly created.
        purchase_id = select_record(query_select_last_purchase_id, 1, None, None)[0]
        # Step 3: create the record in purchasing table.
        manipulate_record(query_insert_purchasing, purchase_id, product_id, purchase_price, purchase_quantity)
        # Step 4: calculate the new stock for the purchased product.
        current_stock = select_record(query_select_product_stock, 1, product_id, None)[0]
        new_stock = int(current_stock) + int(purchase_quantity)
        # Step 5: update the stock in product table.
        manipulate_record(query_update_stock, new_stock, product_id, None, None)
        wait_for_return_menu()