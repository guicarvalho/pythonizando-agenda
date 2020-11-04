"""Define Pytest fixtures."""

import os
import sqlite3
from contextlib import contextmanager
from pathlib import Path

import pytest


@contextmanager
def get_cursor():
    """Get database cursor."""
    conn = sqlite3.connect("contacts_test.db")
    yield conn.cursor()
    conn.commit()
    conn.close()


@pytest.fixture(scope="session")
def create_database(request):
    with get_cursor() as cursor:
        cursor.execute("CREATE TABLE IF NOT EXISTS contact (name TEXT, phone TEXT)")

    def remove_database():
        ROOT_DIR = str(Path(__file__).parent.parent)
        os.remove(os.path.join(ROOT_DIR, "contacts_test.db"))

    request.addfinalizer(remove_database)


@pytest.fixture
def cursor(create_database):
    yield get_cursor()

    with get_cursor() as cursor:
        cursor.execute("DELETE FROM contact")
