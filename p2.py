import sqlite3
con= sqlite3.connect('bookss.db')
cur= con.cursor()
sql="""SELECT
    books.id, 
    books.title, 
    publishers.name AS publisher_name, 
    authors.name, authors.last_name
FROM books
INNER JOIN publishers ON books.publisher_id = publishers.id
INNER JOIN book_author ON books.id = book_author.book_id
INNER JOIN authors ON book_author.author_id = authors.id ;
     """

data = list(cur.execute(sql))
ids = list(set([row[0] for row in data]))
for id in ids:
    books=[row for row in data if row[0]==id]
    print(books[0][0],books[0][1],books[0][2], ",".join([book[3]+ " "+ book[4] for book in books]), sep="\t")