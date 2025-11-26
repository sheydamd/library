import sqlite3

cn = sqlite3.connect("bookss.db")
cur = cn.cursor()

title = input("Book title: ")
description = input("Description: ")

for i, n in cur.execute("SELECT id, name FROM publishers"):
    print(i, n)
publisher = int(input("Publisher ID: "))

for i, n in cur.execute("SELECT id, name FROM esrb_ratings"):
    print(i, n)
esrb = int(input("ESRB ID: "))

for i, n, p in cur.execute("SELECT id, name, last_name FROM translators"):
    print(i, n, p)
translator = [int(x) for x in input("Translator IDs (comma-separated): ").split(",")]

for i, n, p in cur.execute("SELECT id, name, last_name FROM authors"):
    print(i, n, p)
author = [int(x) for x in input("Author IDs (comma-separated): ").split(",")]

for i, n in cur.execute("SELECT id, title FROM resources"):
    print(i, n)
resource = [int(x) for x in input("Resource IDs (comma-separated): ").split(",")]

for i, n in cur.execute("SELECT id, name FROM genres"):
    print(i, n)
genre = [int(x) for x in input("Genre IDs (comma-separated): ").split(",")]

for i, n in cur.execute("SELECT id, name FROM languages"):
    print(i, n)
language = [int(x) for x in input("Language IDs (comma-separated): ").split(",")]

cur.execute("""
    INSERT INTO books (title, description, publisher_id, esrb_rating_id)
    VALUES (?, ?, ?, ?)
""", (title, description, publisher, esrb))

book_id = cur.lastrowid

for a in author:
    cur.execute("INSERT INTO book_author (book_id, author_id) VALUES (?, ?)", (book_id, a))

for g in genre:
    cur.execute("INSERT INTO book_genre (book_id, genre_id) VALUES (?, ?)", (book_id, g))

for r in resource:
    cur.execute("INSERT INTO book_resource (book_id, resource_id) VALUES (?, ?)", (book_id, r))

for l in language:
    cur.execute("INSERT INTO book_language (book_id, language_id) VALUES (?, ?)", (book_id, l))

for t in translator:
    cur.execute("INSERT INTO book_translator (book_id, translator_id) VALUES (?, ?)", (book_id, t))

cn.commit()
print("Book and relations inserted successfully.")

cn.close()