import pytest
import sqlite3
from app.genre import GenreService

@pytest.fixture
def db_connection():
    connection = sqlite3.connect(":memory:")
    connection.execute("CREATE TABLE Genre (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL UNIQUE)")
    yield connection
    connection.close()

def test_add_genre(db_connection):
    service = GenreService(db_connection)
    service.add_genre("Fiktion")

    genre = db_connection.execute("SELECT * FROM Genre WHERE name = 'Fiktion'").fetchone()
    assert genre is not None
    assert genre[1] == "Fiktion"
