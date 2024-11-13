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

    def is_book_loaned(self, book_id):
        cursor = self.db_connection.cursor()
        cursor.execute("SELECT loaned FROM Book WHERE id = ?", (book_id,))
        result = cursor.fetchone()
        
        if result is None:
            return None
        
        print((result[0])) # to see if true or false in cli
        return bool(result[0])