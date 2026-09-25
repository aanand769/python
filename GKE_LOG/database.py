import sqlite3
import os

DATABASE = "data/logs.db"

def create_database():
    os.mkdirs("data", exist_ok=True)

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


    if __name__=="__main__":
        create_database()