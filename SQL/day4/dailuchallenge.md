CREATE TABLE orders (
  order_id SERIAL,
  first_name VARCHAR(30) NOT NULL,
  last_name VARCHAR(30) NOT NULL,
  PRIMARY KEY (order_id)
);


CREATE TABLE items (
  item_id SERIAL,
  item_name VARCHAR(45) NOT NULL,
  item_price INTEGER NOT NULL,
  fk_order_id INTEGER NOT NULL,
  PRIMARY KEY (item_id),
  FOREIGN KEY (fk_order_id) REFERENCES orders(order_id) ON DELETE CASCADE
);

INSERT into items(item_name, item_price) 
VALUES 
('dress', 100),
('jacket', 200),
('skirt', 120),
('short', 50);

INSERT into orders(order_id, first_name, last_name) 
VALUES 
(1, 'louise', 'cohen'),
(2, 'luna', 'lucas'),
(3, 'david','hermann')


SELECT * FROM 
items WHERE fk_order_id =1;

CREATE TABLE users (
  user_id SERIAL,
  first_name VARCHAR(45) NOT NULL,
  last_naem VARCHAR (45) NOT NULL,
  fk_order_id INTEGER NOT NULL,
  PRIMARY KEY (user_id),
  FOREIGN KEY (fk_order_id) REFERENCES orders(order_id) ON DELETE CASCADE
);

