# database.py
import sqlite3
from config import DB_NAME

def get_db_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn

def create_table():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS emails (
        gmail_id TEXT PRIMARY KEY,
        thread_id TEXT,
        sender TEXT,
        recipients TEXT,
        subject TEXT,
        date_received TEXT,
        snippet TEXT,
        labels TEXT
    )
    """)
    conn.commit()
    conn.close()

def save_email(email_data):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
    INSERT OR REPLACE INTO emails
    (gmail_id, thread_id, sender, recipients, subject, date_received, snippet, labels)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        email_data['gmail_id'],
        email_data['thread_id'],
        email_data['sender'],
        email_data['recipients'],
        email_data['subject'],
        email_data['date_received'],
        email_data['snippet'],
        email_data['labels']
    ))
    conn.commit()
    conn.close()

def fetch_emails():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM emails")
    rows = cursor.fetchall()
    conn.close()
    return rows

def clear_emails():
    """Delete all rows from the emails table."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM emails")
    conn.commit()
    conn.close()
    print("All emails have been deleted from the database.")