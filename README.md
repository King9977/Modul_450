<<<<<<< HEAD
# Modul_450
=======
# Buchverwaltungssystem

Dieses Projekt ist ein einfaches Buchverwaltungssystem, das die Speicherung, Anzeige und Suche von Büchern in einer SQLite-Datenbank ermöglicht. Es wurde als Teil der LB1-Aufgabe im Modul 450 erstellt und enthält Unit-Tests, um die Funktionalität sicherzustellen.

## Projektübersicht

Das Buchverwaltungssystem ermöglicht die Verwaltung von Büchern, Autoren und Genres in einer SQLite-Datenbank. Es werden grundlegende CRUD-Operationen unterstützt, und das Projekt ist so strukturiert, dass es leicht erweitert werden kann.

## Verwendete Technologien

- **Programmiersprache**: Python
- **Datenbank**: SQLite
- **Entwicklungsumgebung**: Visual Studio Code
- **Testing-Framework**: Pytest, Unittest (für Mocking)

## Projektstruktur

```
LB1/
├── app/
│   ├── __init__.py
│   ├── author.py       # AuthorService zum Verwalten der Autoren
│   ├── book.py         # BookService zum Verwalten der Bücher
│   ├── genre.py        # GenreService zum Verwalten der Genres
│
├── tests/
│   ├── __init__.py
│   ├── test_author.py                 # Test für AuthorService
│   ├── test_author_with_mock.py       # Test mit Mocking für AuthorService
│   ├── test_book.py                   # Test für BookService
│   ├── test_book_with_time_freezing.py # Test mit Time-Freezing für BookService
│   ├── test_genre.py                  # Test für GenreService
│
├── db_setup.py           # Skript zum Initialisieren der Datenbank
├── initialize_db.sql     # SQL-Datei zum Erstellen der Tabellen
├── main.py               # Hauptskript zum Testen der Grundfunktionen
└── README.md             # Projektbeschreibung
```

## Installation und Einrichtung

1. **Projekt klonen**:

   ```bash
   git clone git@github.com:King9977/Modul_450.git
   cd Modul_450
   ```
2. **Virtuelle Umgebung erstellen und aktivieren** (optional):

   ```bash
   python -m venv venv
   source venv/bin/activate  # Für Linux/macOS
   venv\Scripts\activate     # Für Windows
   ```
3. **Abhängigkeiten installieren**:

   ```bash
   pip install -r requirements.txt
   ```
4. **Datenbank initialisieren**:

   ```bash
   python db_setup.py
   ```

## Verwendung

Nach der Installation und Einrichtung kannst du das System testen, indem du das `main.py`-Skript ausführst. Dieses Skript fügt beispielhafte Daten hinzu und zeigt sie an.

```bash
python main.py
```

## Unit-Tests

Das Projekt enthält verschiedene Unit-Tests, die sicherstellen, dass die Funktionalität korrekt implementiert ist. Die Tests umfassen:

- **Mock-Tests**: Verwendet `unittest.mock`, um die Datenbank zu simulieren.
- **Time-Freezing-Test**: Testet die `add_book`-Methode mit einem eingefrorenen Datum.
- **TDD-Tests**: Der Ansatz des Test-Driven Development (TDD) wurde verwendet, um einige der Funktionen zu entwickeln.

### Tests ausführen

Führe alle Tests mit dem folgenden Befehl aus:

```bash
pytest tests/
```

## Autor

- **Kaya Senay / Martin Stoyanov**

## Lizenz

Dieses Projekt steht unter keiner spezifischen Lizenz und ist für Schulungszwecke gedacht.
>>>>>>> LB1
