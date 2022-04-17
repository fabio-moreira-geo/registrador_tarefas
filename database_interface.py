import sqlite3

def insert_contact(name, date, task):
    conn = sqlite3.connect('contact_information.db')
    conn.execute("INSERT INTO CONTACT_INFORMATION (NAME,DATE,TASK) \
VALUES (?,?,?)", (name,date,task))
    conn.commit()
    conn.close()

def delete_contact_by_name(name):
    conn = sqlite3.connect('contact_information.db')
    conn.execute("DELETE from CONTACT_INFORMATION where name = ?",(name,))
    conn.close()

def edit_date_by_name(name, date):
    conn = sqlite3.connect('contact_information.db')
    conn.execute("UPDATE CONTACT_INFORMATION set DATE = ? where NAME = ?", (name, date))
    conn.commit()
    conn.close()

def edit_task_by_name(name, task):
    conn = sqlite3.connect('contact_information.db')
    conn.execute("UPDATE CONTACT_INFORMATION set DATE = ? where NAME = ?", (name, task))
    conn.close()

def retrieve_contacts():
    results = []
    conn = sqlite3.connect('contact_information.db')
    cursor = conn.execute("SELECT name, date, task from CONTACT_INFORMATION")
    # Contact records are tuples and need to be converted into an array
    for row in cursor:
        results.append(list(row))
    return results