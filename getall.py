import sqlite3
con= sqlite3.connect('bookss.db')
cur= con.cursor()
class Authors :
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
    
class AuthorsDataAdapter:
    @staticmethod
    def get_all()-> list[Authors]:
        authors=[]
        cn=sqlite3.connect("bookss.db")
        cur=cn.cursor()
        auths=cur.execute("SELECT * FROM Authors")
        for au in auths:
            a1=Authors(au[0],au[1],au[2])
            authors.append(a1)
        for author in authors:
            print(author)
    def insert(author: Authors)-> Authors:
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
    
class Translators :
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
    
class TranslatorsDataAdapter:
    @staticmethod
    def get_all()-> list[Translators]:
        translators=[]
        cn=sqlite3.connect("bookss.db")
        cur=cn.cursor()
        tran=cur.execute("SELECT * FROM Translators")
        for tr in tran:
            t1=Translators(tr[0],tr[1],tr[2])
            translators.append(t1)
        for translator in translators:
            print(translator)
    def insert(tranlator: Translators)-> Translators:
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
    
class Esrb_ratings :
    id : int =0
    esrb_name: str =""
    def __init__(self,id,esrb_name):
        self.id=id
        self.esrb_name=esrb_name

    def __str__(self)-> str:
        return f"id: {self.id},esrb_name:{self.esrb_name}"
    
class Esrb_ratingsDataAdapter:
    @staticmethod
    def get_all()-> list[Esrb_ratings]:
        esrb_ratings=[]
        cn=sqlite3.connect("bookss.db")
        cur=cn.cursor()
        esrb=cur.execute("SELECT * FROM esrb_ratings")
        for es in esrb:
            e1=Esrb_ratings(es[0],es[1],es[2])
            esrb_ratings.append(e1)
        for esrbr in esrb_ratings:
            print(esrb)

    def insert(esrb: Esrb_ratings)-> Esrb_ratings:
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

class Publishers :
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
    
class PublishersDataAdapter:
    @staticmethod
    def get_all()-> list[Publishers]:
        publishers=[]
        cn=sqlite3.connect("bookss.db")
        cur=cn.cursor()
        pubs=cur.execute("SELECT * FROM Publishers")
        for pu in pubs:
            t1=Publishers(pu[0],pu[1],pu[2])
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

class Resources :
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
    
class ResourcesDataAdapter:
    @staticmethod
    def get_all()-> list[Resources]:
        resources=[]
        cn=sqlite3.connect("bookss.db")
        cur=cn.cursor()
        res=cur.execute("SELECT * FROM resources")
        for rs in res:
            r1=Resources(rs[0],rs[1],rs[2])
            resources.append(r1)
        for resource in resources :
            print(resource)

    def insert(resource: Resources)-> Resources:
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
    
class Genres :
    id : int =0
    name: str =""
    def __init__(self,id,name):
        self.id=id
        self.name=name
    def __str__(self)-> str:
        return f"id: {self.id},name:{self.name}"
    
class GenresDataAdapter:
    @staticmethod
    def get_all()-> list[Genres]:
        genres=[]
        cn=sqlite3.connect("bookss.db")
        cur=cn.cursor()
        gens=cur.execute("SELECT * FROM genres")
        for gen in gens:
            g1=Resources(gen[0],gen[1],gen[2])
            genres.append(g1)
        for genre in genres :
            print(genre)

    def insert(genre: Genres)-> Genres:
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
    
class Languages :
    id : int =0
    name: str =""
    def __init__(self,id,name):
        self.id=id
        self.name=name
    def __str__(self)-> str:
        return f"id: {self.id},name:{self.name}"
    
class LanguagesDataAdapter:
    @staticmethod
    def get_all()-> list[Languages]:
        languages=[]
        cn=sqlite3.connect("bookss.db")
        cur=cn.cursor()
        lan=cur.execute("SELECT * FROM languages")
        for ln in lan:
            r1=Resources(ln[0],ln[1],ln[2])
            languages.append(r1)
        for language in languages :
            print(language)
    def insert(lang: Languages)-> Languages:
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

class Books :
    id :int = 0
    name: str =""
    title: str =""
    description : str =""
    esrb_rating : Esrb_ratings =None
    publisher: Publishers =None
    book_language:list[Book_language]=[]
    book_author:list[Book_author]=[]
    book_translator:list[Book_translator]=[]
    book_resource:list[Book_resource]=[]
    book_genre:list[Book_genre]=[]
    class LanguagesDataAdapter:
        @staticmethod
        def get_all()-> list[Languages]:
            books=[]
            cn=sqlite3.connect("bookss.db")
            cur=cn.cursor()
            boks=cur.execute("SELECT * FROM books")
            for bk in boks:
                r1=Books(bk[0],bk[1],bk[2])
                books.append(r1)
            for bok in books :
                print(bok)
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

