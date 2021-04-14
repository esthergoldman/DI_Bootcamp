
CREATE TABLE items(

 item_id SERIAL PRIMARY KEY,

 product VARCHAR (50) NOT NULL,

 price  MONEY NOT NULL

)





INSERT INTO items (product, price)

VALUES

('Small Desk', 100),

('Large desk', 300),

('Fan', 80);



SELECT * FROM items WHERE price >= 80;

SELECT * FROM items WHERE price <= 300;

















___________________________________________
CREATE TABLE customers(

 customer_id SERIAL PRIMARY KEY,

 first_name VARCHAR (50) NOT NULL,

 last_name VARCHAR (100) NOT NULL,

)



INSERT INTO customers (first_name, last_name)

VALUES

('Greg','Jones'),

('Sandra','Jones'),

('Scott','Scott'),

('Trevor','Green'),

('Melanie','Johnson');



SELECT * FROM customers;



SELECT * FROM customers WHERE last_name = 'Smith';    (Will you get a result ? NO)

SELECT * FROM customers WHERE last_name = 'Jones';

SELECT * FROM customers WHERE last_name != 'Scott';