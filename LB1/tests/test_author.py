import pytest
import sqlite3
from app.author import AuthorService

@pytest.fixture
def db_connection():
    connection = sqlite3.connect(":memory:")  # In-Memory-Datenbank für Tests
    connection.execute("CREATE TABLE Author (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, birth_date TEXT)")
    yield connection
    connection.close()

def test_add_author(db_connection):
    service = AuthorService(db_connection)
    service.add_author("Kaya Senay", "2005-04-06")

    author = db_connection.execute("SELECT * FROM Author WHERE name = 'Kaya Senay'").fetchone()
    assert author is not None
    assert author[1] == "Kaya Senay"
