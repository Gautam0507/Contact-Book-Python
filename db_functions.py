import sqlite3

def add_row(fname, lname, ph_no):
    connection = sqlite3.connect("contacts.db")
    cursor = connection.cursor()
    command = '''INSERT INTO contacts (first_name, last_name, phone_number) VALUES (?,?,?)'''
    values = (fname, lname, ph_no)
    cursor.execute(command, values)
    connection.commit()
    connection.close()

def remove_element(row_id:int):
    connection = sqlite3.connect("contacts.db")
    cursor = connection.cursor()
    command = '''DELETE FROM contacts WHERE rowid == ?'''
    cursor.execute(command, str(row_id))
    connection.commit()
    connection.close()

def modify_value(row_id:int, column_name:str, changed_value:str):
    connection = sqlite3.connect("contacts.db")
    cursor = connection.cursor()
    command = '''UPDATE contacts SET {} = ? WHERE rowid == ?'''.format(column_name)
    cursor.execute(command, (changed_value, str(row_id)))
    connection.commit()
    connection.close()