from src.messages.confirmation_messages import message_login_confirmation
from src.messages.error_messages import error_user_not_found, error_incorrect_password
from src.queries.queries_administration import query_select_administrator
from src.functions.generic_functions import cancel
from src.modules.module_db_connection import select_record


def module_login():
    while True:
        username = input("Username: ")
        if cancel(username):
            exit()
        password = input("Password: ")
        login_check = select_record(query_select_administrator, 1, username, None)
        if login_check is None:
            print(error_user_not_found)
        elif password not in login_check[2]:
            print(error_incorrect_password)
        else:
            print(message_login_confirmation)
            return login_check[0]