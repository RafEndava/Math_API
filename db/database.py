import sqlite3
from pathlib import Path

# Calea către fișierul SQLite
DB_PATH = Path(__file__).parent / "operations.db"


def init_db():
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute('''
            CREATE TABLE IF NOT EXISTS operations (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                type TEXT,
                a INTEGER,
                b INTEGER,
                result TEXT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        ''')
