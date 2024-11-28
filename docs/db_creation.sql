CREATE DATABASE IF NOT EXISTS db_sales;

USE db_sales;

CREATE TABLE IF NOT EXISTS client (
    client_id INT NOT NULL AUTO_INCREMENT,
    client_name VARCHAR(70) NOT NULL,
    client_surname VARCHAR(70) NOT NULL,
    CONSTRAINT PRIMARY KEY (client_id)
);

CREATE TABLE IF NOT EXISTS administrator (
    admin_id INT NOT NULL AUTO_INCREMENT,
    admin_login VARCHAR(45) NOT NULL,
    admin_password VARCHAR(45) NOT NULL,
    CONSTRAINT PRIMARY KEY (admin_id)
);

CREATE TABLE IF NOT EXISTS family (
    family_id INT NOT NULL AUTO_INCREMENT,
    family_designation VARCHAR(70) NOT NULL,
    CONSTRAINT PRIMARY KEY (family_id)
);

CREATE TABLE IF NOT EXISTS product (
    product_id INT NOT NULL AUTO_INCREMENT,
    product_name VARCHAR(70) NOT NULL,
    product_price FLOAT NOT NULL,
    product_stock INT NOT NULL,
    family_id INT NOT NULL,
    CONSTRAINT PRIMARY KEY (product_id),
    CONSTRAINT FOREIGN KEY (family_id) REFERENCES family(family_id)
);

CREATE TABLE IF NOT EXISTS sale (
    sale_id INT NOT NULL AUTO_INCREMENT,
    sale_date DATE NOT NULL,
    client_id INT NOT NULL,
    admin_id INT NOT NULL,
    CONSTRAINT PRIMARY KEY (sale_id),
    CONSTRAINT FOREIGN KEY (admin_id) REFERENCES administrator(admin_id),
    CONSTRAINT FOREIGN KEY (client_id) REFERENCES client(client_id)
);

CREATE TABLE IF NOT EXISTS selling (
    sale_id INT NOT NULL,
    product_id INT NOT NULL,
    sale_quantity INT NOT NULL,
    CONSTRAINT PRIMARY KEY (sale_id, product_id),
    CONSTRAINT FOREIGN KEY (sale_id) REFERENCES sale(sale_id),
    CONSTRAINT FOREIGN KEY (product_id) REFERENCES product(product_id)
);

CREATE TABLE IF NOT EXISTS purchase (
    purchase_id INT NOT NULL AUTO_INCREMENT,
    purchase_date DATE NOT NULL,
    admin_id INT NOT NULL,
    CONSTRAINT PRIMARY KEY (purchase_id),
    CONSTRAINT FOREIGN KEY (admin_id) REFERENCES administrator(admin_id)
);

CREATE TABLE IF NOT EXISTS purchasing (
    purchase_id INT NOT NULL,
    product_id INT NOT NULL,
    purchase_price FLOAT NOT NULL,
    purchase_quantity INT NOT NULL,
    CONSTRAINT PRIMARY KEY (purchase_id, product_id),
    CONSTRAINT FOREIGN KEY (purchase_id) REFERENCES purchase(purchase_id),
    CONSTRAINT FOREIGN KEY (product_id) REFERENCES product(product_id)
);

# Optional:

INSERT INTO client (client_id, client_name, client_surname) VALUES (1, 'LASTIRI','Xabi');
INSERT INTO administrator (admin_id, admin_login, admin_password) VALUES (1, 'admin', 'admin');
INSERT INTO family (family_id, family_designation) VALUES (1, 'Fruits et légumes');
INSERT INTO product(product_id, product_name, product_price, product_stock, family_id) VALUES (1, 'pomme', 1, 100, 1);
INSERT INTO sale(sale_id, sale_date, client_id, admin_id) VALUES (1, '2024-11-22', 1, 1);
INSERT INTO selling(sale_id, product_id, sale_quantity) VALUES (1, 1, 50);
INSERT INTO purchase(purchase_id, purchase_date, admin_id) VALUES (1, '2024-11-22', 1);
INSERT INTO purchasing(purchase_id, product_id, purchasing.purchase_price, purchase_quantity) VALUES (1, 1, 0.5, 100);