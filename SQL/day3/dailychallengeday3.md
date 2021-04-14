ONE TO ONE

CREATE TABLE songs (
  song_id SERIAL,
  song_title VARCHAR(45) NOT NULL,
  released_date date NOT NULL,
  PRIMARY KEY (song_id)
);

/*
 one to one: a song has one genre
*/

CREATE TABLE genre (
  pk_song_id INTEGER NOT NULL,
  song_lyric TEXT NOT NULL,
  PRIMARY KEY (pk_song_id),
  CONSTRAINT fk_song_id FOREIGN KEY (pk_song_id) REFERENCES songs (song_id)
);


INSERT into songs(song_title, released_date) VALUES 
('Baby One More Time', '1997-12-02'),
('Toxic', '2015-09-11');


INSERT into genre(pk_song_id, song_lyric) 
VALUES 
((SELECT song_id FROM songs where song_title = 'Baby One More Time'),
'Oh, baby, baby
Oh, baby, baby'),

((SELECT song_id FROM songs where song_title = 'Toxic'),
'Too high
Can’t come down
Losing my head
Spinning ‘round and ‘round
Do you feel me now?');


SELECT songs.song_title, songs.released_date, genre.song_lyric as genre
FROM songs
FULL OUTER JOIN genre
ON songs.song_id = genre.pk_song_id;


------
ONE TO MANY

CREATE TABLE singers (
  singer_id SERIAL,
  first_name VARCHAR(30) NOT NULL,
  last_name VARCHAR(30) NOT NULL,
  PRIMARY KEY (singer_id)
);

/*
 one to many: A singer sings many songs :)
*/

CREATE TABLE newsongs (
  song_id SERIAL,
  song_title VARCHAR(45) NOT NULL,
  released_date date NOT NULL,
  fk_singer_id INTEGER NOT NULL,
  PRIMARY KEY (song_id),
  FOREIGN KEY (fk_singer_id) REFERENCES singers(singer_id) ON DELETE CASCADE
);

INSERT into singers(first_name, last_name) VALUES 
('Britney', 'Spears'),
('Lady', 'Gaga');

INSERT into newsongs(fk_singer_id,song_title, released_date) VALUES 
(1,'Toxy', '2008-01-01'),
(2,'Poker Face', '2010-03-05');

SELECT singers.first_name, singers.last_name, newsongs.song_title
FROM singers
INNER JOIN newsongs
ON singers.singer_id = newsongs.fk_singer_id;

SELECT singers.first_name, singers.last_name, newsongs.song_title
FROM singers
RIGHT OUTER JOIN newsongs
ON singers.singer_id = newsongs.fk_singer_id;


SELECT singers.first_name, singers.last_name, newsongs.song_title
FROM singers
FULL OUTER JOIN newsongs
ON singers.singer_id = newsongs.fk_singer_id;


SELECT singers.first_name, singers.last_name, newsongs.song_title
FROM singers
LEFT OUTER JOIN newsongs
ON singers.singer_id = newsongs.fk_singer_id;


------------
MANY TO MANY

CREATE TABLE singers_songs (
  singer_id INTEGER NOT NULL,
  song_id INTEGER NOT NULL,
  singer_albums VARCHAR (50) NOT NULL,
  PRIMARY KEY (singer_id, song_id),
  FOREIGN KEY (singer_id) REFERENCES singers(singer_id) ON UPDATE CASCADE,
  FOREIGN KEY (song_id) REFERENCES songs(song_id) ON UPDATE CASCADE
);

INSERT into singers_songs(singer_id, song_id,singer_albums) VALUES 
((SELECT singer_id FROM singers where first_name = 'Britney' AND last_name = 'Spears' ), 
(SELECT song_id FROM songs where song_title = 'Toxic'),'in the zone' );

((SELECT singer_id FROM singers where first_name = 'Lady' AND last_name = 'Gaga' ), 
(SELECT song_id FROM songs where song_title = 'Bad Romance'),'The Fame Monster' );

INSERT into singers_songs(singer_id, song_id,singer_albums) VALUES 
((SELECT singer_id FROM singers where first_name = 'Petite' AND last_name = 'Miller' ), 
(SELECT song_id FROM songs where song_title = 'Baby Love'),'Lil Empire' );



SELECT singers.first_name, singers.last_name, singers_songs.singer_albums
FROM singers
LEFT OUTER JOIN singers_songs
ON singers.singer_id = singers_songs.singer_id;


SELECT singers.first_name, singers.last_name, singers_songs.singer_albums
FROM singers
FULL OUTER JOIN singers_songs
ON singers.singer_id = singers_songs.singer_id;


SELECT singers.first_name, singers.last_name, singers_songs.singer_albums
FROM singers
RIGHT OUTER JOIN singers_songs
ON singers.singer_id = singers_songs.singer_id;


SELECT singers.first_name, singers.last_name, singers_songs.singer_albums
FROM singers
INNER JOIN singers_songs
ON singers.singer_id = singers_songs.singer_id;