import sqlite3

# اتصال به دیتابیس (در صورت نبود ایجاد می‌شود)
conn = sqlite3.connect("bookss.db")
cursor = conn.cursor()

data="""DROP TABLE if EXISTS publishers;

CREATE TABLE IF NOT EXISTS publishers(id INTEGER PRIMARY KEY AUTOINCREMENT,
name varchar(50), address varchar(50),
phone_number varchar(20),
fax_number varchar(30), 
email varchar(50), establish_date varchar(30)
);
DROP TABLE if EXISTS translators ;

CREATE TABLE IF NOT EXISTS translators(id INTEGER PRIMARY KEY AUTOINCREMENT,
 name varchar(30),
 last_name varchar(30),
 grade varchar(50),
 national_code varchar(50)
);

DROP TABLE if EXISTS resources ;
CREATE TABLE IF NOT EXISTS resources(id INTEGER PRIMARY KEY AUTOINCREMENT,
 title varchar(50),
 type varchar(50),
 establish_date varchar(30)
);
 
DROP TABLE if EXISTS authors;
CREATE TABLE IF NOT EXISTS authors(
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name varchar(50),
  last_name varchar(50),
  national_code varchar(50),
  birthday varchar(30),
  grade varchar(30)
  );
 
DROP TABLE if EXISTS languages ;
CREATE TABLE IF NOT EXISTS languages(id INTEGER PRIMARY KEY AUTOINCREMENT, name varchar(50)
 );
DROP TABLE if EXISTS esrb_ratings ; 
CREATE TABLE IF NOT EXISTS esrb_ratings(id INTEGER PRIMARY KEY AUTOINCREMENT, name varchar(30)
);

DROP TABLE if EXISTS genres ;
CREATE TABLE IF NOT EXISTS genres(id INTEGER PRIMARY KEY AUTOINCREMENT, name varchar(30));

DROP TABLE if EXISTS books ; 
CREATE TABLE IF NOT EXISTS books(id INTEGER PRIMARY KEY AUTOINCREMENT,
  title varchar(30),
  name varchar(50),
  publisher_id INTEGER,
  esrb_rating_id INTEGER,
  description varchar(50),
  volume integer,
  isbn varchar(30)
);
 
DROP TABLE if EXISTS book_author;
CREATE TABLE if not EXISTS book_author(
id integer PRIMARY KEY AUTOINCREMENT,
book_id varchar(30),
author_id varchar(30)
);
DROP TABLE if EXISTS book_genre;
CREATE TABLE if not EXISTS book_genre(
id integer PRIMARY KEY AUTOINCREMENT,
book_id varchar(30),
genre_id varchar(30)
);
DROP TABLE if EXISTS book_resource;
CREATE TABLE if not EXISTS book_resource(
id integer PRIMARY KEY AUTOINCREMENT,
book_id varchar(30),
resource_id varchar(30)
);
DROP TABLE if EXISTS book_language;
CREATE TABLE if not EXISTS book_language(
id integer PRIMARY KEY AUTOINCREMENT,
book_id varchar(30),
language_id varchar(30)
);
DROP TABLE if EXISTS book_translator;
CREATE TABLE if not EXISTS book_translator(
id integer PRIMARY KEY AUTOINCREMENT,
book_id varchar(30),
translator_id varchar(30)
);

DROP TABLE if EXISTS users ;
CREATE TABLE IF NOT EXISTS users(user_id INTEGER PRIMARY KEY AUTOINCREMENT,
 first_name varchar(30),
 last_name varchar(30),
 phone_number varchar(30),
 email varchar(50),
 membership_date varchar(30),
 national_code varchar(30),
 expiry_date varchar(30),
 image_url varchar(30)
 );
 
DROP TABLE if EXISTS loans ;
CREATE TABLE IF NOT EXISTS loans(loan_ID INTEGER PRIMARY KEY AUTOINCREMENT, user_id integer, book_id integer, loan_date varchar(30),
   return_date varchar(30), status varchar(30)
   );
   
"""
cursor.executescript(data)
