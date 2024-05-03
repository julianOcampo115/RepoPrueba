CREATE DATABASE myflaskapp;
use myflaskapp;

CREATE TABLE users (
    id int NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name varchar(255),
    email varchar(255),
    username varchar(255),
    password varchar(255)
);
#drop table products;

CREATE TABLE products (
    code int NOT NULL AUTO_INCREMENT PRIMARY KEY,
    product varchar(255),
    price varchar(255),
    amount varchar(255),
    bag varchar(255)
);

INSERT INTO users VALUES(null, "juan", "juan@gmail.com", "juan", "123"),
    (null, "maria", "maria@gmail.com", "maria", "456");

INSERT INTO products VALUES(null, "Tomates", "500", "4", "yes"),
    (null, "Piñas", "2000", "7", "yes");
