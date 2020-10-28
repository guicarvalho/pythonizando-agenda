"""Module define all CRUD operations."""


def save(cursor, name, phone):
    """Save contact.

    Parameters:
        name:
            User full name.
        phone:
            User phone number.
        cursor:
            Database cursor instance.
    """
    cursor.execute("INSERT INTO contact VALUES (?, ?)", (name, phone))


def find_all(cursor):
    """Get all contacts.

    Parameters:
        cursor:
            Database cursor instance.

    Returns:
        All contacts.
    """
    cursor.execute("SELECT * FROM contact")
    return cursor.fetchall()


def delete_by_name(cursor, name):
    """Delete contact by name.

    Parameters:
        cursor:
            Database cursor instance.
        name:
            User name.
    """
    cursor.execute("DELETE FROM contact WHERE name = ?", (name,))
