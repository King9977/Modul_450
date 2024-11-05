import unittest
from unittest.mock import MagicMock
from app.author import AuthorService

def test_add_author_with_mock():
    mock_connection = MagicMock()
    mock_cursor = mock_connection.cursor.return_value
    service = AuthorService(mock_connection)

    service.add_author("Kaya Senay", "2005-04-06")

    mock_cursor.execute.assert_called_once_with("INSERT INTO Author (name, birth_date) VALUES (?, ?)", ("Kaya Senay", "2005-04-06"))
    mock_connection.commit.assert_called_once()
