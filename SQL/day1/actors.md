
SELECT COUNT(actor_ID)

FROM actors;



INSERT INTO actors (first_name, last_name, age, number_oscars)

VALUES('jennifer','lawrence','  ', 1);





ERROR:  invalid input syntax for type date: "  "

LINE 2: VALUES('jennifer','lawrence','  ', 1);

                                     ^

SQL state: 22007

Character: 93

 

