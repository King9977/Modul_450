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
