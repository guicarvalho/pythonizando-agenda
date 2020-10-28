import sqlite3
from contextlib import contextmanager


@contextmanager
def get_cursor():
    """Get database cursor."""
    conn = sqlite3.connect("contacts.db")
    yield conn.cursor()
    conn.commit()
    conn.close()


def create_all():
    """Create all tables."""
    with get_cursor() as cursor:
        cursor.execute("CREATE TABLE IF NOT EXISTS contact (name TEXT, phone TEXT)")
