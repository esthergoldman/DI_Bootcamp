CREATE TABLE students(

 auto_incremented SERIAL PRIMARY KEY,

 first_name VARCHAR (50) NOT NULL,

 last_name VARCHAR (100) NOT NULL,

 birth_date DATE NOT NULL

)



DATE FORMAT MONTH’DAY’YEAR



INSERT INTO students (first_name, last_name, birth_date)

VALUES

('Marc','Benichou', DATE '02.11.1998'),

('Yoan','Cohen', DATE '03.12.2010'),

('Amelia','Dux', DATE '07.04.1996'),

('David','Grez', DATE '06.14.2003'),

('Omer','Simpson', DATE '03.10.1980'),

('Esther','Gold', DATE '10.29.1990');





SELECT * FROM students;



SELECT  first_name, last_name FROM students;



SELECT auto_incremented

FROM students

WHERE

auto_incremented = 2;



SELECT 

first_name,

last_name

FROM students

WHERE

first_name = 'Marc'

AND

last_name = 'Benichou';







SELECT 

first_name,

last_name

FROM students

WHERE

first_name = 'Marc'

OR

last_name = 'Benichou';



SELECT 

first_name,

last_name

FROM students

WHERE

first_name like '%a%';



 SELECT 

first_name,

last_name

FROM students

WHERE

first_name like 'A%'



SELECT 

first_name,

last_name

FROM students

WHERE

first_name like '%a'



SELECT 

first_name,

last_name

FROM students

WHERE

first_name like '%ea'



SELECT auto_incremented

FROM students

WHERE

auto_incremented = 1 

or 

auto_incremented = 3;



SELECT 

*

FROM students

WHERE

birth_date >=  '1/01/2000'