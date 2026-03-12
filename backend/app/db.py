import sqlite3

DB_PATH = "data/metrics/search_logs.db"


def get_connection():
    return sqlite3.connect(DB_PATH)


def init_db():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS query_logs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        request_id TEXT,
        query TEXT,
        top_k INTEGER,
        alpha REAL,
        latency_ms INTEGER,
        result_count INTEGER,
        timestamp TEXT
    )
    """)

    conn.commit()
    conn.close()


def log_query(request_id, query, top_k, alpha, latency_ms, result_count, timestamp):

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
    INSERT INTO query_logs
    (request_id, query, top_k, alpha, latency_ms, result_count, timestamp)
    VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (request_id, query, top_k, alpha, latency_ms, result_count, timestamp))

    conn.commit()
    conn.close()