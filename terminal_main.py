import sqlite3
import db_functions
from init import init


def input_values():
    fname = input("Enter first name: ")
    lname = input("Enter last name: ")
    phno = input("Enter phone number: ")

    if fname == '':
        fname = None
    if lname == '':
        lname = None
    if phno == '':
        phno = None

    return fname, lname, phno


if __name__ == "__main__":
    init()
    state = True
    while state:
        function_condition = input(
            """Enter the following numbres for the corresponding functions\n1.Add New contact\n2.Remove a contact\n3.Modify a single value\n4.Search a particular Conatact\n5.View All contacts\nYour Choice: """)
        if function_condition == '1':
            fname, lname, phno = input_values()
            db_functions.add_row(fname, lname, phno)
            print("Successfully added element")

        elif function_condition == "2":
            fname, lname, phno = input_values()
            data = db_functions.search_records(fname= fname,lname= lname,ph_no= phno)
            if len(data) == 1:
                db_functions.remove_element(data[0])
                print("Successfully removed element")
            else:
                print("Please choose again and provide more data")

        elif function_condition == "3":
            fname, lname, phno = input_values()
            data = db_functions.search_records(fname = fname,lname= lname,ph_no= phno)
            if len(data) == 1:
                column = input(
                    "Enter the correct type of value to be modified (first_name, last_name, phone_number)")
                changed_value = input("Enter the new value: ")
                db_functions.modify_value(data[0], column, changed_value)
                print("Successfully modified element")
            else:
                print("Please choose again and provide more data")

        elif function_condition == "4":
            fname, lname, phno = input_values()
            rowids = db_functions.search_records(
                fname=fname, lname=lname, ph_no=phno)
            if rowids == []:
                print("There is no data to be displayed")
            else:
                print("First Name \tLast Name \tPhone Number")
                for rowid in rowids:
                    record = db_functions.fetch_record(rowid)
                    print(f"{record[1]:<15}\t{record[2]:<15}\t{record[3]:<15}")

        elif function_condition == "5":
            data = db_functions.fetch_all_records()
            if data == []:
                print("There is no data to be displayed")
            else:
                print("First Name \tLast Name \tPhone Number")
                for record in data:
                    print(f"{record[1]:<15}\t{record[2]:<15}\t{record[3]:<15}")

        else:
            print("Enter the valid number for the action needed.\n")
        state_resp = None
        while state_resp not in ["Y", "N"]:
            state_resp = input("Do you have any more queries Y/N:").upper()
            if state_resp == "Y":
                state = True
                break
            elif state_resp == "N":
                state = False
                break
            else:
                print("Please enter Y or N")
