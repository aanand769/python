import sqlite3
from config import DATABASE

def create_database():

    conn = sqlite3.connect(DATABASE)

    cursor = conn.cursor()

    cursor.execute(
        """
        CREATE TABLE IF MOT EXISTS logs(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        timestamp TEXT,
        deployment TEXT,
        prod TEXT,
        namespace TEXT,
        severity TEXT,
        message TEXT,
        error_type TEXT
        )

        """
    )

    conn.commit()

    conn.close()

def insert_log(
        timestamp,
        deployment,
        pod,
        namespace,
        severity,
        message,
        error_type
    ):

    conn = sqlite3.connect(DATABASE)

    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO logs(
         timestamp,
        deployment,
        pod,
        namespace,
        severity,
        message,
        error_type
        )

        VALUES(?,?,?,?,?,?,?)
    """,
        (timestamp,
        deployment,
        pod,
        namespace,
        severity,
        message,
        error_type))

    conn.commit()

    conn.close()