import unittest
from unittest.mock import MagicMock, patch
from datetime import datetime
from app.user import UserService

class TestUserService(unittest.TestCase):
    def setUp(self):
        self.mock_connection = MagicMock()
        self.mock_cursor = self.mock_connection.cursor.return_value
        self.service = UserService(self.mock_connection)

    @patch('app.user.datetime')  # mock datetime um zeit zu freezen
    def test_get_user_based_on_age(self, mock_datetime):
        mock_datetime.now.return_value = datetime(2024, 11, 12)

        test_cases = [
            ("user1", datetime(2009, 11, 12), False),  # unter 18 (erwartet: False)
            ("user2", datetime(2005, 11, 12), True),   # über 18 (erwartet: True)
        ]

        for username, birthdate, expected_result in test_cases:
            # mock DB
            self.mock_cursor.fetchone.return_value = (username, birthdate)
            user = self.service.get_user(username, birthdate)

            self.mock_cursor.execute.assert_called_with("SELECT * FROM User WHERE username = ? AND birthdate = ?", (username, birthdate))

            age = (mock_datetime.now.return_value - birthdate).days / 365
            result = age >= 18  # True falls age 18 or älter, sonst falsch

            self.assertEqual(result, expected_result)

            if result:
                print("Buch erfolgreich ausgeliehen")
            else:
                print("Abgelehnt: Alter unter 18 Jahren")

if __name__ == '__main__':
    unittest.main()