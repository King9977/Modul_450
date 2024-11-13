# Unit Test 2: Mock mit Time-Freezing (mock "now()")
import unittest
from unittest.mock import MagicMock, patch
from datetime import datetime
from app.user import UserService

class TestUserService(unittest.TestCase):
    def setUp(self):
        self.mock_connection = MagicMock()
        self.mock_cursor = self.mock_connection.cursor.return_value
        self.service = UserService(self.mock_connection)

    @patch('app.user.datetime', wraps=datetime)
    def test_is_user_adult(self, mock_datetime):
        mock_datetime.now.return_value = datetime(2024, 11, 12)

        test_cases = [
            ("user1", datetime(2009, 11, 12), False),  # unter 18 (erwartet: False)
            ("user2", datetime(2005, 11, 12), True),   # über 18 (erwartet: True)
        ]

        for username, birthdate, expected_result in test_cases:
            self.mock_cursor.fetchone.return_value = (username, birthdate)
            result = self.service.is_user_adult(username, birthdate)
            self.assertEqual(result, expected_result)

            self.mock_cursor.execute.assert_called_with("SELECT * FROM User WHERE username = ? AND birthdate = ?", (username, birthdate))

if __name__ == '__main__':
    unittest.main()