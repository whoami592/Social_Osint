import sqlite3
from datetime import datetime

DB_NAME = "osint.db"


def connect():
    return sqlite3.connect(DB_NAME)


def init_db():
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS investigations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            platform TEXT NOT NULL,
            profile_url TEXT,
            notes TEXT,
            created_at TEXT NOT NULL
        )
    """)

    conn.commit()
    conn.close()


def add_result(username, platform, profile_url, notes=""):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO investigations
        (username, platform, profile_url, notes, created_at)
        VALUES (?, ?, ?, ?, ?)
    """, (
        username,
        platform,
        profile_url,
        notes,
        datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    ))

    conn.commit()
    conn.close()


def get_results():
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, username, platform, profile_url, notes, created_at
        FROM investigations
        ORDER BY id DESC
    """)

    results = cursor.fetchall()
    conn.close()

    return results