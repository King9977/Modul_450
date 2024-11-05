# tests/test_author_with_mock.py

import unittest
from unittest.mock import MagicMock
from app.author import AuthorService

def test_add_author_with_mock():
    # Erstelle eine gemockte Verbindung und ein gemocktes Cursor-Objekt
    mock_connection = MagicMock()
    mock_cursor = mock_connection.cursor.return_value
    service = AuthorService(mock_connection)

    # Führe die Methode aus
    service.add_author("Kaya Senay", "2005-04-06")

    # Überprüfe, ob die korrekte SQL-Abfrage mit den richtigen Parametern ausgeführt wurde
    mock_cursor.execute.assert_called_once_with(
        "INSERT INTO Author (name, birth_date) VALUES (?, ?)", ("Kaya Senay", "2005-04-06")
    )
    mock_connection.commit.assert_called_once()
