from db_connection import get_db_connection

import datetime

class UserService:
    def __init__(self, db_connection):
        self.db_connection = db_connection

    def add_user(self, username, birthdate):
        cursor = self.db_connection.cursor()
        cursor.execute("INSERT INTO User (username, birthdate) VALUES (?, ?)", (username, birthdate))
        self.db_connection.commit()

    def get_user(self, username, birthdate):
        cursor = self.db_connection.cursor()
        cursor.execute("SELECT * FROM User WHERE username = ? AND birthdate = ?", (username, birthdate))
        return cursor.fetchone()

    def is_user_adult(self, username, birthdate):
        cursor = self.db_connection.cursor()
        cursor.execute("SELECT * FROM User WHERE username = ? AND birthdate = ?", (username, birthdate))
        current_date = datetime.now()
        age = (current_date - birthdate).days / 365

        return age >= 18