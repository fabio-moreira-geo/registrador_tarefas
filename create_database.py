import sqlite3


conn = sqlite3.connect('contact_information.db')
query = (''' CREATE TABLE CONTACT_INFORMATION
            (NAME           TEXT    NOT NULL,
            DATE        TEXT    NOT NULL,
            TASK    TEXT)''')
conn.execute(query)
conn.close()
