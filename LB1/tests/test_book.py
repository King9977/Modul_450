import pytest
import sqlite3
from app.book import BookService

@pytest.fixture
def db_connection():
    connection = sqlite3.connect(":memory:")
    connection.execute("CREATE TABLE Author (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, birth_date TEXT)")
    connection.execute("CREATE TABLE Genre (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL UNIQUE)")
    connection.execute("CREATE TABLE Book (id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT NOT NULL, author_id INTEGER, genre_id INTEGER, publication_date TEXT, FOREIGN KEY (author_id) REFERENCES Author(id), FOREIGN KEY (genre_id) REFERENCES Genre(id))")
    yield connection
    connection.close()

def test_add_book(db_connection):
    db_connection.execute("INSERT INTO Author (name, birth_date) VALUES ('Max Mustermann', '1990-01-01')")
    db_connection.execute("INSERT INTO Genre (name) VALUES ('Fiktion')")
    service = BookService(db_connection)
    service.add_book("Cyber Solutions", 1, 1, "2023-10-01")

    book = db_connection.execute("SELECT * FROM Book WHERE title = 'Cyber Solutions'").fetchone()  # Titel geändert
    assert book is not None
    assert book[1] == "Cyber Solutions"
