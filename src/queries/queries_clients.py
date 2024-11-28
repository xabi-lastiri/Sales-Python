query_select_client = \
    ("SELECT client.client_name, client.client_surname "
    "FROM db_sales.client "
    "WHERE client.client_name = (%s) AND client.client_surname = (%s);")


query_select_client_id = \
    ("SELECT client.client_id "
     "FROM db_sales.client "
     "WHERE client.client_id = %s;")


query_select_clients = \
    ("SELECT client.client_id, client.client_name, client.client_surname "
     "FROM db_sales.client;")


query_insert_client = \
    "INSERT INTO db_sales.client (client_name, client_surname) VALUES (%s, %s);"


query_delete_client = \
    "DELETE FROM db_sales.client WHERE client_id = %s;"