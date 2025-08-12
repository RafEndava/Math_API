import sqlite3
import csv
from db.database import DB_PATH, init_db
from services.logger import logger

init_db()


def save_operation(op_type, a, b, result):
    # Salvare în SQLite
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute(
            "INSERT INTO operations (type, a, b, result) VALUES (?, ?, ?, ?)",
            (op_type, a, b, str(result))
        )

    # Simulare trimitere către sistem de mesagerie
    logger.info(
        f"[STREAMING] Pushed to mock messaging queue: {op_type}({a}, {b}) = {result}"
    )

    # Scriere în CSV (simulare RabbitMQ)
    with open("stream_log.csv", mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([op_type, a, b, result])


def get_all_operations():
    with sqlite3.connect(DB_PATH) as conn:
        conn.row_factory = sqlite3.Row
        rows = conn.execute(
            "SELECT * FROM operations ORDER BY timestamp DESC"
        ).fetchall()
        return [dict(row) for row in rows]
