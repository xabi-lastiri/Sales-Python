query_select_last_purchase_id = \
    ("SELECT purchase.purchase_id "
     "FROM db_sales.purchase "
     "ORDER BY purchase.purchase_id DESC "
     "LIMIT 1;")


query_insert_purchase = \
    "INSERT INTO db_sales.purchase (purchase_date, admin_id) VALUES (%s, %s);"


query_insert_purchasing = \
    ("INSERT INTO db_sales.purchasing (purchase_id, product_id, purchase_price, purchase_quantity) "
     "VALUES (%s, %s, %s, %s);")