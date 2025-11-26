import sqlite3
cn = sqlite3.connect("bookss.db")
cur = cn.cursor()
title = input()
description = input()
for i, n in cur.execute("SELECT id, name FROM publishers"):
    print(i, n)
publisher = input()

for i, n in cur.execute("SELECT id, name FROM esrb_ratings"):
    print(i, n)
esrb = input()
for i, n, p in cur.execute("SELECT id, name, last_name FROM translators"):
    print(i, n, p)
translator = input()
translator = [x for x in translator.split(",")]

for i, n, p in cur.execute("SELECT id, name, last_name FROM authors"):
    print(i, n, p)
author = input()
author = [x for x in author.split(",")]

for i, n in cur.execute("SELECT id, title FROM resources"):
    print(i, n)
resource = input()
resource = [x for x in resource.split(",")]

for i, n in cur.execute("SELECT id, name FROM genres"):
    print(i, n)
genre = input()
genre = [x for x in genre.split(",")]

for i, n in cur.execute("SELECT id, name FROM languages"):
    print(i, n)
language = input()
language = [x for x in language.split(",")]

sql = """
INSERT INTO books(id, title , name,
  publisher_id, esrb_rating_id,
  description, volume, isbn)
  value();

insert into book_author(id, book_id, author_id) 
    value();

insert into book_genre(book_id, genre_id) 
    value(); 

insert into book_resource(book_id, resource_id) 
    value(); 

insert into  book_language(book_id, language_id) 
    value(); 

insert into  book_translator(book_id,
translator_id) 
    value();    
"""
data = list(cur.execute(sql))
cn.commit()
a=cur.lastrowid
