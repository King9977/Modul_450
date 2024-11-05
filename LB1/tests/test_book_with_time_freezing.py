from datetime import datetime
from unittest.mock import patch
from app.book import BookService
import sqlite3

def test_publication_date_freezing():
    db_connection = sqlite3.connect(":memory:")
    db_connection.execute("CREATE TABLE Book (id INTEGER PRIMARY KEY, title TEXT, author_id INTEGER, genre_id INTEGER, publication_date TEXT)")

    service = BookService(db_connection)

    with patch("datetime.datetime") as mock_datetime:
        mock_datetime.now.return_value = datetime(2024, 1, 1)
        mock_date_str = mock_datetime.now.return_value.strftime("%Y-%m-%d")

        service.add_book("Frozen Date Book", 1, 1, mock_date_str)

        book = db_connection.execute("SELECT * FROM Book WHERE title = 'Frozen Date Book'").fetchone()
        assert book[4] == "2024-01-01"
