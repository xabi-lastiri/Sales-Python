from src.messages.error_messages import error_invalid_format
from src.modules.module_db_connection import select_record


# Check whether the item exists in the database or not.
def check_item_exists(query, parameter1, parameter2):
    result = select_record(query, 1, parameter1, parameter2)
    return False if result is None else True


def check_price_format(price):
    try: return float(price)
    except ValueError: print(error_invalid_format)


def check_int_format(value):
    try: return int(value)
    except ValueError: return False