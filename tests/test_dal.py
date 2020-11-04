"""All tests for DAL module."""

from database.dal import save, find_all


def test_save_contact(cursor):
    """
    [Scenario] Save contact.
    [Assertion] That contact was saved.
    """
    with cursor as cur:
        cur.execute("SELECT * FROM contact")
        contacts = cur.fetchall()

        assert len(contacts) == 0

        save(cursor=cur, name="Guilherme", phone="3333-3333")

        cur.execute("SELECT * FROM contact")
        contacts = cur.fetchall()

    assert len(contacts) == 1

def test_find_all_contacts(cursor):
    with cursor as cur:
        cur.execute("INSERT INTO contact (name, phone) VALUES (?, ?)", ("Python", "123",))
        contacts = find_all(cursor=cur)

    assert len(contacts) == 1


def test_find_all_2(mocker):
    cur = mocker.Mock()
    find_all(cursor=cur)

    assert cur.execute.called is True
    assert cur.fetchall.called is True
    cur.execute.assert_called_once_with("SELECT * FROM contact")
