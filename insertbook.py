import sqlite3
cn = sqlite3.connect("bookss.db")
cur = cn.cursor()
title=input()
description=input()
for i, n in cur.execute("SELECT id, name FROM publishers"):
    print(i, n)
publishers=int(input())
for i, n in cur.execute("SELECT id, name FROM esrb_ratings"):
    print(i, n)
esrb=int(input())

for i, n, p in cur.execute("SELECT id, name, last_name FROM authors"):
    print(i, n, p)
authors=int(input())
for author in authors.split(","):
    a=author
for i, n, p in cur.execute("SELECT id, name, last_name FROM translators"):
    print(i, n, p)
translators=input()
for translator in translators.split(","):
    a=translator
for i, n, p in cur.execute("SELECT id, title, type FROM resources"):
    print(i, n, p)
resourses=input()
for resource in resourses.split(","):
    a=resource
for i, n, p in cur.execute("SELECT id, name FROM languages"):
    print(i, n)
languages=input()
for language in languages.split(","):
    a=language
for i, n, p in cur.execute("SELECT id, name FROM genres"):
    print(i, n)
genres=input()
for genre in genres.split(","):
    a=genre