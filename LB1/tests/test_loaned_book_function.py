import unittest
from unittest.mock import MagicMock
from app.book import BookService

class TestBookService(unittest.TestCase):
    def setUp(self):
        self.mock_connection = MagicMock()
        self.mock_cursor = self.mock_connection.cursor.return_value
        self.service = BookService(self.mock_connection)

    def test_is_book_loaned(self):
        test_cases = [(1, True),(2, False),(999, None)]

        for book_id, expected_result in test_cases:
            if expected_result is not None:
                self.mock_cursor.fetchone.return_value = (expected_result,)
            else:
                self.mock_cursor.fetchone.return_value = None

            result = self.service.is_book_loaned(book_id)
            self.assertEqual(result, expected_result)
            self.mock_cursor.execute.assert_called_with("SELECT loaned FROM Book WHERE id = ?", (book_id,))

if __name__ == '__main__':
    unittest.main()