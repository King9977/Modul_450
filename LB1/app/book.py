import datetime

class BookService:
    def __init__(self, db_connection):
        self.db_connection = db_connection

    def add_book(self, title, author_id, genre_id, publication_date):
        cursor = self.db_connection.cursor()
        cursor.execute("INSERT INTO Book (title, author_id, genre_id, publication_date) VALUES (?, ?, ?, ?)",
        (title, author_id, genre_id, publication_date))
        self.db_connection.commit()

    def get_book(self, book_id):
        cursor = self.db_connection.cursor()
        cursor.execute("SELECT * FROM Book WHERE id = ?", (book_id,))
        return cursor.fetchone()
