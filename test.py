import sqlite3

con = sqlite3.connect('bookss.db')
cur = con.cursor()

sql = """
SELECT
    books.id, 
    books.title, 
    publishers.name AS publisher_name, 
    authors.name  || ' ' ||  authors.last_name AS author_name
FROM books
INNER JOIN publishers ON books.publisher_id = publishers.id
INNER JOIN book_author ON books.id = book_author.book_id
INNER JOIN authors ON book_author.author_id = authors.id;
"""

data = list(cur.execute(sql))  # همه داده‌ها را یک بار بگیر

ids = list(set([row[0] for row in data]))  # کتاب‌های منحصربه‌فرد

for id in ids:
    books = [row for row in data if row[0] == id]
    authors = ", ".join([book[3] for book in books])
    print(books[0][0], books[0][1], books[0][2], authors, sep="\t")

con.close()