query_select_administrator = \
    ("SELECT administrator.admin_id, administrator.admin_login, administrator.admin_password "
    "FROM db_sales.administrator "
    "WHERE administrator.admin_login = (%s)")


query_select_administrator_id = \
    ("SELECT administrator.admin_id "
     "FROM db_sales.administrator "
     "WHERE administrator.admin_id = %s;")


query_select_administrators = \
    ("SELECT administrator.admin_id, administrator.admin_login "
     "FROM db_sales.administrator")


query_insert_administrator = \
    "INSERT INTO db_sales.administrator (admin_login, admin_password) VALUES (%s, %s);"


query_delete_administrator = "DELETE FROM db_sales.administrator WHERE administrator.admin_id = %s;"


query_change_password = ("UPDATE db_sales.administrator "
                         "SET administrator.admin_password = %s "
                         "WHERE administrator.admin_id = %s")