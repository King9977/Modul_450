from db_connection import get_db_connection

class AuthorService:
    def __init__(self, db_connection):
        self.db_connection = db_connection

    def add_author(self, name, birth_date):
        cursor = self.db_connection.cursor()
        cursor.execute("INSERT INTO Author (name, birth_date) VALUES (?, ?)", (name, birth_date))
        self.db_connection.commit()

    def get_author(self, author_id):
        cursor = self.db_connection.cursor()
        cursor.execute("SELECT * FROM Author WHERE id = ?", (author_id,))
        return cursor.fetchone()
    

if __name__ == "__main__":
    try:
        db_connection = get_db_connection()
        print("Database connection successful!")

        author_service = AuthorService(db_connection)

        author_service.add_author("Mark Twain", "1835-11-30")

        author = author_service.get_author(1)
        if author:
            print(f"Author Found: {author['name']}, Born: {author['birth_date']}")
        else:
            print("Author not found.")

        db_connection.close()
        print("Database connection closed!")
    except Exception as e:
        print(f"Failed to connect to the database: {e}")

