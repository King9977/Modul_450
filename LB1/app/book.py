from db_connection import get_db_connection

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
        try:
            # schau ob int und positiv
            if not isinstance(book_id, int) or book_id <= 0:
                raise ValueError("book_id muss positiv und eine Zahl sein.")
            
            cursor = self.db_connection.cursor()
            cursor.execute("SELECT loaned FROM Book WHERE id = ?", (book_id,))
            result = cursor.fetchone()
            
            if result is None:
                print(f"Buch mit id {book_id} nicht gefunden.")
                return None
            
            print(result[0])  # zu schauen ob true oder false in der cli
            return bool(result[0])
        
        except ValueError as ve:
            print(f"Error: {ve}")
            return None
        except Exception as e:
            print(f"Unerwarteter error: {e}")
            return None