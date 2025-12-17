# Library Database Data Models & SQLite Data Adapters

This project contains a set of Python classes and SQLite data adapters designed to form the core of a Library Management Database System.
It provides the fundamental structure needed to store, organize, and manage various types of information in a library—such as:
The goal is to clearly separate database access logic from domain models, while manually mimicking the behavior of ORM systems such as Django ORM or SQLAlchemy.

1. Books

2. Authors

3. Translators

4. Publishers

5. Genres

6. Languages

7. Content ratings

8. Available resources


By offering both data models and database interaction layers, this codebase can serve as the backbone of larger applications.
For example, it can be used when developing:

A library website

A digital catalog

A book borrowing system

A publisher or bookstore management system

Any project that requires structured book-related data


The goal is to provide an organized, object-oriented system that simplifies interaction with an SQLite database, making it easier to build scalable and maintainable software on top of it.

## Features

Object-oriented models for:

- Authors

- Translators

- ESRB Ratings

- Publishers

- Resources

- Genres

- Languages

- Books and their many-to-many relations


Basic CRUD-style database operations (Get all, Insert, Delete)

SQLite database connectivity using Python’s built-in sqlite3 module

Each DataAdapter is responsible for fetching data from its own table.

BooksDataAdapter.get_all():

1. Loads books only (without relations)


2. Loads related data using other adapters


3. Maps related objects to each book using book_id


4. Prevents duplicates using eq


5. Returns a fully populated list of Books

# Project Structure

The file includes the following classes:

Entity Classes

Each represents a record in a table:

Authors

Translators

Esrb_ratings

Publishers

Resources

Genres

Languages

Books

Association models:

Book_author

Book_translator

Book_resource

Book_genre

Book_language

### Equality Handling (eq)

To prevent duplicate related objects, model classes implement the eq method.

Example:

class Author:
    def init(self, id, name):
        self.id = id
        self.name = name

    def eq(self, other):
        return isinstance(other, Author) and self.id == other.id

This allows clean membership checks like:

if author not in book.book_author:


### Data Adapter Classes

Each provides methods for database interaction:

AuthorDataAdapter

TranslatorDataAdapter

Esrb_ratingDataAdapter

PublisherDataAdapter

ResourceDataAdapter

GenreDataAdapter

LanguagesDataAdapter

BookDataAdapter


Typical functionality includes:

get_all() — Fetch all records from a table

insert() — Insert a new entity

delete(id) — Delete a record (with basic dependency checks)


### Notes

Python will not automatically call init, so you must call it manually.

Some SQL statements may contain errors or mismatched field names depending on your database schema.

Several classes return inconsistent field mappings (e.g., wrong table columns).
.