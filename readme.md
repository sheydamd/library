# Library Database Data Models & SQLite Data Adapters

This project provides a set of Python classes representing entities in a library management system—such as Authors, Translators, Publishers, Genres, and more—along with Data Adapter classes that interact with an SQLite database.
The goal is to offer a simple object-oriented structure for storing and retrieving information about books and their related metadata.

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



### Data Adapter Classes

Each provides methods for database interaction:

AuthorsDataAdapter

TranslatorsDataAdapter

Esrb_ratingsDataAdapter

PublishersDataAdapter

ResourcesDataAdapter

GenresDataAdapter

LanguagesDataAdapter


Typical functionality includes:

get_all() — Fetch all records from a table

insert() — Insert a new entity

delete(id) — Delete a record (with basic dependency checks)

### Notes

Some constructors use init instead of the standard init.
Python will not automatically call init, so you must call it manually.

Some SQL statements may contain errors or mismatched field names depending on your database schema.

Several classes return inconsistent field mappings (e.g., wrong table columns).

Many database paths are inconsistent (books.db, bookss.db, data1.db).
Ensure these files exist or update the paths.