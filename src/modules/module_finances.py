from src.messages.error_messages import error_no_items_found
from src.messages.instructions import instruction_return_menu
from src.modules.module_db_connection import select_record
from src.queries.queries_finances import query_select_revenue_by_month, query_select_revenue_by_year
from src.functions.generic_functions import introduce_module, wait_for_return_menu


def module_finances():
    while True:
        introduce_module("menu > finances", instruction_return_menu)
        modules = [
            "1. Show revenue by month",
            "2. Show revenue by year"
        ]
        for module in modules: print(module)
        select = input("\n> ")
        match select:
            case "m": break
            case "1": show_revenue_by_month()
            case "2": show_revenue_by_year()


def show_revenue_by_month():
    introduce_module("menu > finances > recipes per month", None)
    result = select_record(query_select_revenue_by_month, "n", None, None)
    if result is None:
        print(error_no_items_found)
    else:
        for month in result:
            print(
                f"{month[0]}-{month[1]}: {round(int(month[2]))} € turnover - {round(int(month[3]))} € expenses = {round(int(month[4]))} € recipes")
    wait_for_return_menu()


def show_revenue_by_year():
    introduce_module("menu > finances > recipes per year", None)
    result = select_record(query_select_revenue_by_year, "n", None, None)
    if result is None:
        print(error_no_items_found)
    else:
        for year in result:
            print(
                f"{year[0]}: {round(int(year[1]))} € turnover - {round(int(year[2]))} € expenses = {round(int(year[3]))} € recipes")
    wait_for_return_menu()