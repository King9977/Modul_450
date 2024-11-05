-- initialize_db.sql

-- Tabelle für Autoren
CREATE TABLE IF NOT EXISTS Author (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    birth_date TEXT
);

-- Tabelle für Genres
CREATE TABLE IF NOT EXISTS Genre (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE
);

-- Tabelle für Bücher
CREATE TABLE IF NOT EXISTS Book (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    author_id INTEGER,
    genre_id INTEGER,
    publication_date TEXT,
    FOREIGN KEY (author_id) REFERENCES Author(id),
    FOREIGN KEY (genre_id) REFERENCES Genre(id)
);
