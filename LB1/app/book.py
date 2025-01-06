from db_connection import get_db_connection

import datetime
import sqlite3  # Importieren des sqlite3-Moduls

class BookService:

    def get_db_connection(db_path="../book_management.db"):
        try:
            connection = sqlite3.connect(db_path)
            connection.row_factory = sqlite3.Row
            connection.execute("PRAGMA foreign_keys = ON;")  # Fremdschlüsselprüfung aktivieren
            return connection
        except sqlite3.Error as e:
            print(f"Error connecting to database: {e}")
            raise


    def __init__(self, db_connection):
        self.db_connection = db_connection

    def add_book(self, title, author_id, genre_id, publication_date):

        if not title.strip():
            raise ValueError("Der Titel darf nicht leer sein.")
        if not isinstance(author_id, int) or author_id <= 0:
            raise ValueError("Die Autor-ID muss eine positive Ganzzahl sein.")
        if not isinstance(genre_id, int) or genre_id <= 0:
            raise ValueError("Die Genre-ID muss eine positive Ganzzahl sein.")
        if not publication_date.strip():
            raise ValueError("Das Veröffentlichungsdatum darf nicht leer sein.")

        cursor = self.db_connection.cursor()

        # Überprüfen, ob die `author_id` in der Tabelle `Author` existiert
        cursor.execute("SELECT id FROM Author WHERE id = ?", (author_id,))
        if cursor.fetchone() is None:
            raise ValueError(f"Die Autor-ID {author_id} existiert nicht in der Tabelle Author.")

        # Überprüfen, ob die `genre_id` in der Tabelle `Genre` existiert
        cursor.execute("SELECT id FROM Genre WHERE id = ?", (genre_id,))
        if cursor.fetchone() is None:
            raise ValueError(f"Die Genre-ID {genre_id} existiert nicht in der Tabelle Genre.")

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