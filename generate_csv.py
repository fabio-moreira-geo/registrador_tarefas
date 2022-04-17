import database_interface
import csv

def get_contact_records():
    contact_records = database_interface.retrieve_contacts()
    return contact_records


def create():
    contact_records_array = get_contact_records()
    headings = ['Name', 'Date', 'Task']

    file = open('contacts.csv', 'w', encoding='UTF8', newline='')
    writer = csv.writer(file)

    # write the header
    writer.writerow(headings)

    # write multiple rows
    writer.writerows(contact_records_array)
    file.close()
