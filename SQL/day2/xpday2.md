Part 1



SELECT *

FROM items

ORDER BY price ASC;





SELECT *

FROM items

WHERE price >= 80

ORDER BY price DESC;



SELECT DISTINCT first_name

FROM customers

ORDER BY first_name  ASC

LIMIT 3;



SELECT DISTINCT last_name

FROM customers

ORDER BY last_name  desc;



Exercisexp 1 part 2

———

CREATE TABLE purchase

  AS (SELECT customer_id,item_id

      FROM customers,items);





DELETE FROM purchase







INSERT INTO purchase (customer_id, item_id)

VALUES 

(1, null)



_____

INSERT INTO purchase (customer_id, item_id)

VALUES

(1,1),

(2,2),

(3,3),

(4,4),

(5,0);





PART 3



SELECT *

FROM purchase





SELECT customers.first_name, customers.last_name, purchase.customer_id

FROM customers

INNER JOIN purchase

ON customers.customer_id = purchase.customer_id;



SELECT * FROM purchase WHERE customer_id = 4;







SELECT * FROM purchase

INNER JOIN items ON purchase.item_id = items.item_id 



SELECT * FROM purchase

INNER JOIN items ON purchase.item_id = items.item_id 

WHERE items.product ILIKE 'Small desk' OR 

items.product ILIKE 'Large desk'





INSERT INTO purchase (customer_id, item_id) 

VALUES(3,2);







SELECT items.product,  purchase.item_id

FROM items

INNER JOIN purchase

ON items.item_id = purchase.item_id;





SELECT items.product,  purchase.item_id, customers.first_name, customers.last_name, purchase.customer_id

FROM items INNER JOIN purchase ON items.item_id = purchase.item_id

INNER JOIN customers ON customers.customer_id = purchase.customer_id


____________________

xp day 2 

Dvd rental



SELECT * FROM customer

ORDER BY customer_id ASC 







SELECT (first_name , last_name) as full_name

FROM customer







SELECT COUNT (create_date)

FROM customer







SELECT * FROM customer

ORDER BY first_name DESC 







SELECT film_id, title, description, release_year, rental_rate FROM film

ORDER BY rental_rate ASC 







SELECT address, district, phone FROM address WHERE district ilike 'texas'



SELECT * FROM film

WHERE film_id = 15 OR film_id = 150 ;



SELECT film_id, title, description,"length", rental_rate   FROM film

WHERE title ilike 'harry potter';







SELECT film_id, title, description,"length", rental_rate   FROM film

WHERE title ILIKE 'Ha%';





SELECT MIN(rental_rate) FROM film

SELECT title FROM film

where rental_rate = 0.99

LIMIT 10





SELECT title FROM film

where rental_rate = 0.99

offset 10

FETCH FIRST 10 ROWS ONLY





SELECT payment.amount, payment.payment_date, customer.first_name, customer.last_name, customer.customer_id

FROM payment

INNER JOIN customer 

on payment.customer_id = customer.customer_id

ORDER BY customer_id ASC;





13 no idea

SELECT inventory.inventory_id, inventory.last_update, film.title

FROM inventory

inner JOIN film

ON inventory.film_id = film.film_id

13-







SELECT country.country_id, country.country, city.city

FROM country

inner JOIN city

ON country.country_id = city.country_id





SELECT customer.customer_id, customer.first_name, customer.last_name, customer.store_id, payment.amount, payment.payment_date

FROM customer

inner JOIN payment

ON payment.customer_id = customer.customer_id

order by store_id