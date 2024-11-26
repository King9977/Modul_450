import sqlite3
def get_db_connection(db_path="../book_management.db"):
    try:
        connection = sqlite3.connect(db_path)
        connection.row_factory = sqlite3.Row
        return connection
    except sqlite3.Error as e:
        print(f"Error connecting to database: {e}")
        raise