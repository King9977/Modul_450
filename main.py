import sqlite3
from app.author import AuthorService
from app.genre import GenreService
from app.book import BookService

def main():
    db_connection = sqlite3.connect("book_management.db")
    
    author_service = AuthorService(db_connection)
    genre_service = GenreService(db_connection)
    book_service = BookService(db_connection)

    # Beispiel: Autor hinzufügen
    author_service.add_author("Kaya Senay", "2005-04-06")
    genre_service.add_genre("Fiktion")
    book_service.add_book("Cyber Solutions", 1, 1, "2023-10-01")

    # Beispiel: Buch abrufen
    book = book_service.get_book(1)
    print(book)

    db_connection.close()

if __name__ == "__main__":
    main()
