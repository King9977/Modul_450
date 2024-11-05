# db_setup.py

import sqlite3

def initialize_db():
    # Lösche die Datei, falls sie existiert
    try:
        import os
        if os.path.exists("book_management.db"):
            os.remove("book_management.db")
    except Exception as e:
        print(f"Fehler beim Löschen der alten Datenbank: {e}")

    # Erstelle eine neue Datenbankverbindung
    connection = sqlite3.connect("book_management.db")
    cursor = connection.cursor()

    # Lese das SQL-Skript und führe es aus
    with open("initialize_db.sql", "r") as sql_file:
        sql_script = sql_file.read()
        cursor.executescript(sql_script)

    connection.commit()
    connection.close()
    print("Datenbank wurde erfolgreich initialisiert.")

if __name__ == "__main__":
    initialize_db()
