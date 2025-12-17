import sqlite3
con= sqlite3.connect('bookss.db')
cur= con.cursor()

class Author :
    id : int =0
    national_code :int = 0
    Name: str =""
    last_name: str =""
    birthday : str =""
    grade: str = ""

    def __init__(self,id,name,last_name,birthday,grade,national_code):
        self.id=id
        self.name=name
        self.national_code=national_code
        self.last_name=last_name
        self.birthday=birthday
        self.grade=grade
    def __str__(self)-> str:
        return f"id: {self.id},name:{self.name},last_name:{self.last_name}"
    def __eq__(self,other):
        return isinstance(other.Aathor) and self.id==other.id
    
class AuthorDataAdapter:
    @staticmethod
    def get_all()-> list[Author]:
        authors=[]
        cn=sqlite3.connect("bookss.db")
        cur=cn.cursor()
        auths=cur.execute("SELECT * FROM Authors")
        for au in auths:
            a1=Author(au[0],au[1],au[2])
            authors.append(a1)
        for author in authors:
            print(author)
    def insert(author: Author)-> Author:
        cn=sqlite3.connect("bookss.db")
        cur=cn.cursor()
        sql=f"INSERT INTO authors (id,name,last_name,birthday,grade,national_code) VALUES({author.id}, '{author.name}', '{author.last_name}', '{author.birthday}', '{author.grade}','{author.national_code}'))"
        cur.execute(sql)
        cn.commit()
        lid=cur.lastrowid
        author.id=lid
        return author
    
    @staticmethod
    def delete(id: int) -> bool:
        cn = sqlite3.connect("books.db")
        cur = cn.cursor()
        sql = "SELECT author_id FROM books"
        if id in [row[0] for row in cur.execute(sql)]:
            return False
        cur.execute(f"DELETE FROM authors WHERE id={id}")
        cn.commit()
        return True
    
class Translator :
    id : int =0
    national_code :int = 0
    Name: str =""
    last_name: str =""
    birthday : str =""
    grade: str = ""
    def __init__(self,id,name,last_name,birthday,grade,national_code):
        self.id=id
        self.name=name
        self.national_code=national_code
        self.last_name=last_name
        self.birthday=birthday
        self.grade=grade
    def __str__(self)-> str:
        return f"id: {self.id},name:{self.name},last_name:{self.last_name}"
    def __eq__(self,other):
        return isinstance(other.Translators) and self.id==other.id
class TranslatorDataAdapter:
    @staticmethod
    def get_all()-> list[Translator]:
        translators=[]
        cn=sqlite3.connect("bookss.db")
        cur=cn.cursor()
        tran=cur.execute("SELECT * FROM Translators")
        for tr in tran:
            t1=Translator(tr[0],tr[1],tr[2])
            translators.append(t1)
        for translator in translators:
            print(translator)
    def insert(tranlator: Translator)-> Translator:
        cn=sqlite3.connect("bookss.db")
        cur=cn.cursor()
        sql=f"INSERT INTO translators (id,name,last_name,birthday,grade,national_code) VALUES({tranlator.id}, '{tranlator.name}', '{tranlator.last_name}', '{tranlator.birthday}', '{tranlator.grade}','{tranlator.national_code}'))"
        cur.execute(sql)
        cn.commit()
        lid=cur.lastrowid
        tranlator.id=lid
        return tranlator
    @staticmethod
    def delete(id: int) -> bool:
        cn = sqlite3.connect("books.db")
        cur = cn.cursor()
        sql = "SELECT translator_id FROM books"
        if id in [row[0] for row in cur.execute(sql)]:
            return False
        cur.execute(f"DELETE FROM translators WHERE id={id}")
        cn.commit()
        return True
    
class Esrb_rating :
    id : int =0
    esrb_name: str =""
    def __init__(self,id,esrb_name):
        self.id=id
        self.esrb_name=esrb_name

    def __str__(self)-> str:
        return f"id: {self.id},esrb_name:{self.esrb_name}"
    
    def __eq__(self,other):
        return isinstance(other.Esrb_rating) and self.id==other.id
    
class Esrb_ratingDataAdapter:
    @staticmethod
    def get_all()-> list[Esrb_rating]:
        esrb_ratings=[]
        cn=sqlite3.connect("bookss.db")
        cur=cn.cursor()
        esrb=cur.execute("SELECT * FROM esrb_ratings")
        for es in esrb:
            e1=Esrb_rating(es[0],es[1],es[2])
            esrb_ratings.append(e1)
        for esrbr in esrb_ratings:
            print(esrb)

    def insert(esrb: Esrb_rating)-> Esrb_rating:
        cn=sqlite3.connect("data1.db")
        cur=cn.cursor()
        sql=f"INSERT INTO esrb_ratings (id, name) VALUES( {esrb.id} ,'{esrb.name}')"
        cur.execute(sql)
        cn.commit()
        lid=cur.lastrowid
        esrb.id=lid
        return esrb
    
    @staticmethod
    def delete(id:int)-> bool:
        cn=sqlite3.connect("data1.db")
        cur=cn.cursor()
        sql1="select esrb_rating_id from books"
        book=cur.execute(sql1)
        if id not in book:
            sql2="delete from esrb_ratings where id={id}"
            cur.execute(sql2)
            cn.commit()
        else:
            return False

class Publisher :
    id : int =0
    address:str=""
    establish_date :str = ""
    name: str =""
    email: str =""
    birthday : int =0
    fax_number: str = ""
    phone_number: str = ""
    def __init__(self,id,name,birthday):
        self.id=id
        self.name=name
        self.birthday=birthday
    def __str__(self)-> str:
        return f"id: {self.id},name:{self.name},birthday:{self.birthday}"
    
    def __eq__(self,other):
        return isinstance(other.Publisher) and self.id==other.id
    
class PublisherDataAdapter:
    @staticmethod
    def get_all()-> list[Publisher]:
        publishers=[]
        cn=sqlite3.connect("bookss.db")
        cur=cn.cursor()
        pubs=cur.execute("SELECT * FROM Publishers")
        for pu in pubs:
            t1=Publisher(pu[0],pu[1],pu[2])
            publishers.append(t1)
        for publisher in publishers:
            print(publisher)

    @staticmethod
    def delete(id:int)-> bool:
        cn=sqlite3.connect("data1.db")
        cur=cn.cursor()
        sql1="select publidher_id from books"
        book=cur.execute(sql1)
        if id not in book:
            sql2="delete from publishers where id={id}"
            cur.execute(sql2)
            cn.commit()
        else:
            return False

class Resource :
    id : int =0
    title :str = 0
    type: str =""
    establish_date: str =""
    def __init__(self,id,title,type,establish_date):
        self.id=id
        self.title=title
        self.type=tuple
        self.establish_date=establish_date
    def __str__(self)-> str:
        return f"id: {self.id},title:{self.title},establish_date:{self.establish_date}"
    def __eq__(self,other):
        return isinstance(other.Resource) and self.id==other.id
    
class ResourceDataAdapter:
    @staticmethod
    def get_all()-> list[Resource]:
        resources=[]
        cn=sqlite3.connect("bookss.db")
        cur=cn.cursor()
        res=cur.execute("SELECT * FROM resources")
        for rs in res:
            r1=Resource(rs[0],rs[1],rs[2])
            resources.append(r1)
        for resource in resources :
            print(resource)

    def insert(resource: Resource)-> Resource:
        cn=sqlite3.connect("data1.db")
        cur=cn.cursor()
        sql=f"INSERT INTO resources (id, title, type, establish_date) VALUES( {resource.id} ,'{resource.title}','{resource.type}','{resource.establish_date}')"
        cur.execute(sql)
        cn.commit()
        lid=cur.lastrowid
        resource.id=lid
        return resource
    
    @staticmethod
    def delete(id: int) -> bool:
        cn = sqlite3.connect("books.db")
        cur = cn.cursor()
        sql = "SELECT resource_id FROM books"
        if id in [row[0] for row in cur.execute(sql)]:
            return False
        cur.execute(f"DELETE FROM resources WHERE id={id}")
        cn.commit()
        return True
    
class Genre :
    id : int =0
    name: str =""
    def __init__(self,id,name):
        self.id=id
        self.name=name
    def __str__(self)-> str:
        return f"id: {self.id},name:{self.name}"
    def __eq__(self,other):
        return isinstance(other.Gunre) and self.id==other.id
class GenreDataAdapter:
    @staticmethod
    def get_all()-> list[Genre]:
        genres=[]
        cn=sqlite3.connect("bookss.db")
        cur=cn.cursor()
        gens=cur.execute("SELECT * FROM genres")
        for gen in gens:
            g1=Resource(gen[0],gen[1],gen[2])
            genres.append(g1)
        for genre in genres :
            print(genre)

    def insert(genre: Genre)-> Genre:
        cn=sqlite3.connect("data1.db")
        cur=cn.cursor()
        sql=f"INSERT INTO genres (id, esrb_name) VALUES( {genre.id} ,'{genre.name}')"
        cur.execute(sql)
        cn.commit()
        lid=cur.lastrowid
        genre.id=lid
        return genre
    
    @staticmethod
    def delete(id: int) -> bool:
        cn = sqlite3.connect("books.db")
        cur = cn.cursor()
        sql = "SELECT genre_id FROM books"
        if id in [row[0] for row in cur.execute(sql)]:
            return False
        cur.execute(f"DELETE FROM genres WHERE id={id}")
        cn.commit()
        return True
    
class Language :
    id : int =0
    name: str =""
    def __init__(self,id,name):
        self.id=id
        self.name=name
    def __str__(self)-> str:
        return f"id: {self.id},name:{self.name}"
    def __eq__(self,other):
        return isinstance(other.Language) and self.id==other.id
class LanguageDataAdapter:
    @staticmethod
    def get_all()-> list[Language]:
        languages=[]
        cn=sqlite3.connect("bookss.db")
        cur=cn.cursor()
        lan=cur.execute("SELECT * FROM languages")
        for ln in lan:
            r1=Resource(ln[0],ln[1],ln[2])
            languages.append(r1)
        for language in languages :
            print(language)
    def insert(lang: Language)-> Language:
        cn=sqlite3.connect("data1.db")
        cur=cn.cursor()
        sql=f"INSERT INTO languages (id, esrb_name) VALUES( {lang.id} ,'{lang.name}')"
        cur.execute(sql)
        cn.commit()
        lid=cur.lastrowid
        lang.id=lid
        return lang
    
    @staticmethod
    def delete(id: int) -> bool:
        cn = sqlite3.connect("books.db")
        cur = cn.cursor()
        sql = "SELECT language_id FROM books"
        if id in [row[0] for row in cur.execute(sql)]:
            return False
        cur.execute(f"DELETE FROM languages WHERE id={id}")
        cn.commit()
        return True
    
#multiple
class Book_author:
    book:str=""
    author:str=""
class Book_translator:
    book:str=""
    translator:str=""

class Book_resource:
    book:str=""
    resource:str=""

class Book_genre:
    book:str=""
    genre:str=""

class Book_language:
    book:str=""
    language:str=""

class Book :
    id :int = 0
    name: str =""
    title: str =""
    description : str =""
    esrb_rating : Esrb_rating =None
    publisher: Publisher =None
    book_language:list[Book_language]=[]
    book_author:list[Book_author]=[]
    book_translator:list[Book_translator]=[]
    book_resource:list[Book_resource]=[]
    book_genre:list[Book_genre]=[]
    def __init__(self,id,name,title,description):
        self.id=id
        self.name=name
        self.title=title
        self.description=description
        self.description
        self.esrb_rating = None
        self.publisher = None
        self.book_language = []
        self.book_author = []
        self.book_translator = []
        self.book_resource = []
        self.book_genre = []
        self.publisher=None
    def __str__(self)-> str:
        return f"id: {self.id},name:{self.name},title:{self.title},description:{self.description}"
    
class BookDataAdapter:
    @staticmethod
    def get_books_only():
        import sqlite3
        cn = sqlite3.connect("bookss.db")
        cur = cn.cursor()

        books = []
        for row in cur.execute("SELECT id, name, title, description FROM books"):
            books.append(Book(row[0], row[1], row[2], row[3]))

        cn.close()
        return books

    @staticmethod
    def get_all():
        books = BookDataAdapter.get_books_only()
        books_map = {book.id: book for book in books}

        for ba in AuthorDataAdapter.get_all():
            if ba.book_id in books_map:
                if ba.author not in books_map[ba.book_id].book_author:
                    books_map[ba.book_id].book_author.append(ba.author)

        for bg in GenreDataAdapter.get_all():
            if bg.book_id in books_map:
                if bg.genre not in books_map[bg.book_id].book_genre:
                    books_map[bg.book_id].book_genre.append(bg.genre)

        for bl in LanguageDataAdapter.get_all():
            if bl.book_id in books_map:
                if bl.language not in books_map[bl.book_id].book_language:
                    books_map[bl.book_id].book_language.append(bl.language)

        return list(books_map.values())
    @staticmethod
    def delete(id:int)-> bool:
            cn = sqlite3.connect("books.db")
            cur = cn.cursor()
            sql=cur.execute("SELECT id FROM books WHERE id = {id}")
            if id in [row[0] for row in cur.execute(sql)]:
                return False
            cur.execute("DELETE FROM book_author WHERE book_id = {book_id}")
            cur.execute("DELETE FROM book_translator WHERE book_id = {book_id}")
            cur.execute("DELETE FROM book_resource WHERE book_id = {book_id}")
            cur.execute("DELETE FROM book_genre WHERE book_id = {book_id}")
            cur.execute("DELETE FROM book_language WHERE book_id = {book_id}")
            cur.execute("DELETE FROM books WHERE id = {book_id}")
            cn.commit()
            return True

books=BookDataAdapter.get_all()
for book in books:
    print(book)