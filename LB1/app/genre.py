from db_connection import get_db_connection
class GenreService:
    def __init__(self, db_connection):
        self.db_connection = db_connection

    def add_genre(self, name):
        cursor = self.db_connection.cursor()
        cursor.execute("INSERT INTO Genre (name) VALUES (?)", (name,))
        self.db_connection.commit()

    def get_genre(self, genre_id):
        cursor = self.db_connection.cursor()
        cursor.execute("SELECT * FROM Genre WHERE id = ?", (genre_id,))
        return cursor.fetchone()
