query_select_products_by_family = \
    ("SELECT product.product_id, product_name, product_price, product_stock "
    "FROM db_sales.product "
    "WHERE product.family_id = %s;")


query_select_families = \
    ("SELECT family.family_id, family.family_designation "
     "FROM db_sales.family")


query_select_family = \
    ("SELECT family.family_id "
     "FROM db_sales.family "
     "WHERE family.family_designation = %s;")


query_select_family_id = \
    ("SELECT family.family_id "
     "FROM db_sales.family "
     "WHERE family.family_id = %s;")


query_select_product = \
    ("SELECT product.product_name "
     "FROM db_sales.product "
     "WHERE product.product_name = %s;")


query_select_product_id = \
    ("SELECT product.product_id "
     "FROM db_sales.product "
     "WHERE product.product_id = %s;")


query_select_product_price = \
    ("SELECT product.product_price "
     "FROM db_sales.product "
     "WHERE product.product_id = %s;")


query_select_product_stock = \
    ("SELECT product.product_stock "
     "FROM db_sales.product "
     "WHERE product.product_id = %s;")


query_select_products = \
    ("SELECT product.product_id, product.product_name, product_price, product_stock, family_designation "
    "FROM db_sales.product "
     "JOIN db_sales.family ON product.family_id = family.family_id;")


query_insert_product = \
    "INSERT INTO db_sales.product (product_name, product_price, product_stock, family_id) VALUES (%s, %s, %s, %s);"


query_insert_family = \
    "INSERT INTO db_sales.family (family_designation) VALUES (%s);"


query_delete_product = \
    "DELETE FROM db_sales.product WHERE product_id = %s;"


query_delete_family = \
    "DELETE FROM db_sales.family WHERE family_id = %s;"


query_update_stock = \
    ("UPDATE db_sales.product "
     "SET product.product_stock = %s "
     "WHERE product.product_id = %s;")
