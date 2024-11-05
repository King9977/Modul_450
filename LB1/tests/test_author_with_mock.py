# Unit Test 1: Mock anstatt DB
import unittest
from unittest.mock import MagicMock
from app.author import AuthorService

class TestAuthorService(unittest.TestCase):
    def setUp(self):
        self.mock_connection = MagicMock()
        self.mock_cursor = self.mock_connection.cursor.return_value
        self.service = AuthorService(self.mock_connection)

    def test_add_author_with_mock(self):
        self.service.add_author("Kaya Senay", "2005-04-06")
        self.mock_cursor.execute.assert_called_once_with("INSERT INTO Author (name, birth_date) VALUES (?, ?)", ("Kaya Senay", "2005-04-06"))
        self.mock_connection.commit.assert_called_once()
