query_select_last_sale_id = \
    ("SELECT sale.sale_id "
     "FROM db_sales.sale "
     "ORDER BY sale.sale_id DESC "
     "LIMIT 1;")


query_select_sales_per_product = \
    ("SELECT product.product_id, product.product_name, "
     "COALESCE(COUNT(selling.sale_id), 0) AS total_sales_number, "
     "COALESCE(SUM(selling.sale_quantity), 0) AS total_unit_sold, "
     "COALESCE(SUM(product.product_price * selling.sale_quantity), 0) AS total_turnover "
     "FROM db_sales.product "
     "LEFT JOIN db_sales.selling ON product.product_id = selling.product_id "
     "GROUP BY product.product_id, product.product_name "
     "ORDER BY total_unit_sold DESC;")


query_select_sales_per_client = \
    ("SELECT client.client_id, client.client_name, client.client_surname, "
     "COALESCE(COUNT(selling.sale_id), 0) AS total_sales_number, "
     "COALESCE(SUM(product.product_price * selling.sale_quantity), 0) AS total_turnover "
     "FROM db_sales.client "
     "LEFT JOIN db_sales.sale ON client.client_id = sale.client_id "
     "LEFT JOIN db_sales.selling ON sale.sale_id = selling.sale_id "
     "LEFT JOIN db_sales.product ON selling.product_id = product.product_id "
     "GROUP BY client.client_id "
     "ORDER BY total_turnover DESC;")


query_select_sales_by_user = \
    ("SELECT administrator.admin_id, administrator.admin_login, "
     "COALESCE(COUNT(selling.sale_id), 0) AS total_sales_number, "
     "COALESCE(SUM(product.product_price * selling.sale_quantity), 0) AS total_turnover "
     "FROM db_sales.administrator "
     "LEFT JOIN db_sales.sale ON administrator.admin_id = sale.admin_id "
     "LEFT JOIN db_sales.selling ON sale.sale_id = selling.sale_id "
     "LEFT JOIN db_sales.product ON selling.product_id = product.product_id "
     "GROUP BY administrator.admin_id "
     "ORDER BY total_sales_number DESC;")


query_insert_sale = \
 "INSERT INTO db_sales.sale (sale_date, client_id, admin_id) VALUES (%s, %s, %s);"


query_insert_selling = \
 "INSERT INTO db_sales.selling (sale_id, product_id, sale_quantity) VALUES (%s, %s, %s);"