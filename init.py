import sqlite3


def init():
    connection = sqlite3.connect("contacts.db")

    cursor = connection.cursor()

    # Chekcking if the table exists
    cursor.execute("""SELECT name FROM sqlite_master WHERE type = 'table';""")

    if cursor.fetchall() == []:
        connection.execute("""CREATE TABLE contacts(
        first_name TEXT,
        last_name TEXT,
        phone_number TEXT);""")
    else:
        pass
    connection.close()

if __name__ == '__main__':
    pass