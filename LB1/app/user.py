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
        user = cursor.fetchone()

        if not user:
            return False  # Benutzer existiert nicht

        # Konvertiere den String (birthdate) in ein datetime-Objekt
        birth_date = datetime.datetime.strptime(birthdate, "%Y-%m-%d")
        current_date = datetime.datetime.now()

        # Berechne das Alter in Jahren
        age = (current_date - birth_date).days // 365
        return age >= 18
