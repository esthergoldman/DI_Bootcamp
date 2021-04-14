SELECT language.language_id,language.name
FROM language



SELECT language.name, film.title, film.description
FROM language
FULL OUTER JOIN film
ON language.language_id = film.language_id;


only language 1 in


CREATE TABLE new_film (
  film_id SERIAL,
  title VARCHAR(45) NOT NULL,
  PRIMARY KEY (film_id)
);


INSERT into new_film(title) VALUES 
(' alice in wonderland'),
('harry potter');

CREATE TABLE customer_review(
  review_id SERIAL NOT NULL,
  language_id INTEGER NOT NULL,
  title CHARACTER VARYING NOT NULL,
  score NUMERIC,	
  review_text CHARACTER VARYING NOT NULL,
  last_update TIMESTAMP WITHOUT TIME ZONE,
  fk_film_id INTEGER NOT NULL,
  PRIMARY KEY (review_id),
  FOREIGN KEY (fk_film_id) REFERENCES new_film(film_id) ON DELETE CASCADE
);

INSERT into customer_review(review_text,title) VALUES 
(' good', 'alice in wonderland' ),
('super good', 'harry potter');



DELETE FROM customer_review  where title = 'alice in wonderland';




Exercise 2 : Dvd Rental

UPDATE language 
SET 
    name = 'Spanish'
WHERE
    language_id = 2;


UPDATE language 
SET 
    name = 'Danish'
WHERE
    language_id = 3;


foreign key: fk_film_id, not affect the way we insert

DROP TABLE customer_review;



SELECT * FROM rental

where return_date = null





SELECT max(rental_rate) FROM film

SELECT title FROM film

where rental_rate = 4.99

LIMIT 30



SELECT actor_id, last_name  
FROM actor

WHERE first_name ILIKE 'penelope';


SELECT film_id  
FROM film_actor

WHERE actor_id = 120;




SELECT first_name, customer_id 
FROM customer where last_name = 'Mahan'


SELECT rental.inventory_id,
	customer_id,  rental_date, inventory.film_id 
FROM rental 
join inventory
on inventory.inventory_id = rental.inventory_id

where customer_id= 323


SELECT * FROM 
film WHERE title  ilike ('%boat%');


SELECT * FROM 
film WHERE description  ilike ('%boat%');

