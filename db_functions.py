import sqlite3


def add_row(fname, lname, ph_no):
    connection = sqlite3.connect("contacts.db")
    cursor = connection.cursor()
    command = '''INSERT INTO contacts (first_name, last_name, phone_number) VALUES (?,?,?)'''
    values = (fname, lname, ph_no)
    cursor.execute(command, values)
    connection.commit()
    connection.close()


def remove_element(row_id: int):
    connection = sqlite3.connect("contacts.db")
    cursor = connection.cursor()
    command = '''DELETE FROM contacts WHERE rowid == ?'''
    cursor.execute(command, str(row_id))
    connection.commit()
    connection.close()


def modify_value(row_id: int, column_name: str, changed_value: str):
    connection = sqlite3.connect("contacts.db")
    cursor = connection.cursor()
    command = '''UPDATE contacts SET {} = ? WHERE rowid == ?'''.format(
        column_name)
    cursor.execute(command, (changed_value, str(row_id)))
    connection.commit()
    connection.close()


def fetch_all_records():
    connection = sqlite3.connect("contacts.db")
    cursor = connection.cursor()
    command = '''SELECT rowid, * FROM contacts'''
    cursor.execute(command)
    data = cursor.fetchall()
    connection.commit()
    connection.close()
    return data


def fetch_record(rowid):
    connection = sqlite3.connect("contacts.db")
    cursor = connection.cursor()
    command = f"SELECT rowid, * FROM contacts WHERE rowid == '{rowid}'"
    cursor.execute(command)
    data = cursor.fetchone()
    connection.commit()
    connection.close()
    return data


def search_records(rowid: int = None, fname: str = None, lname: str = None, ph_no: str = None):
    connection = sqlite3.connect('contacts.db')
    cursor = connection.cursor()
    base_command = """SELECT rowid,* FROM contacts WHERE """
    where_conditions = ''
    if not where_conditions:
        if rowid is not None:
            where_conditions += f"rowid == '{rowid}'"
            rowid = None
        elif fname is not None:
            where_conditions += f"first_name == '{fname}'"
            fname = None
        elif lname is not None:
            where_conditions += f"last_name == '{lname}'"
            lname = None
        elif ph_no is not None:
            where_conditions += f"phone_number == '{ph_no}'"
            ph_no = None
    if where_conditions:
        if rowid is not None:
            where_conditions += f" AND rowid == '{rowid}'"
            rowid = None
        if fname is not None:
            where_conditions += f" AND first_name == '{fname}'"
            fname = None
        if lname is not None:
            where_conditions += f" AND last_name == '{lname}'"
            lname = None
        if ph_no is not None:
            where_conditions += f" AND phone_number == '{ph_no}'"
            ph_no = None

    command = base_command + where_conditions + ';'
    cursor.execute(command)
    data = cursor.fetchall()
    connection.commit()
    connection.close()
    result = []
    for i in data:
        result.append(i[0])
    return result


if __name__ == "__main__":
    pass
