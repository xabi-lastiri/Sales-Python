from src.modules.module_administration import module_administration
from src.modules.module_clients import module_clients
from src.modules.module_finances import module_finances
from src.modules.module_products import module_products
from src.modules.module_purchases import module_purchases
from src.modules.modules_sales import module_sales
from src.functions.generic_functions import introduce_module
from src.modules.module_login import module_login


def main():
    user_id = module_login()
    while True:
        introduce_module("main menu", None)
        modules = [
            "1. Clients",
            "2. Products",
            "3. Sales",
            "4. Purchases",
            "5. Finances",
            "6. Administration"
        ]
        print("0. Exit")
        for module in modules: print(module)
        select = input("\n> ")
        match select:
            case "0": break
            case "1": module_clients()
            case "2": module_products()
            case "3": module_sales(user_id)
            case "4": module_purchases(user_id)
            case "5": module_finances()
            case "6": module_administration()


if __name__=='__main__':
    main()