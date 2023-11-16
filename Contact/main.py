import sqlite3
conn = sqlite3.connect('contacts.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS contacts (
        id INTEGER PRIMARY KEY,
        name TEXT,
        phone_number TEXT
    )
''')

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

contacts = {}
def add_contact():
    name = input(bcolors.BOLD+"Enter name: "+bcolors.ENDC)
    number = input(bcolors.BOLD+"Enter mobile number: "+bcolors.ENDC)
    if(len(number)==10):
        cursor.execute('''INSERT INTO contacts(
            name, phone_number) VALUES 
            (?,?)''',(name,number))
        print(bcolors.OKGREEN + "Added contact for {} successfully!".format(name)+ bcolors.ENDC)
    else:
        print(bcolors.WARNING + "Please enter valid 10 digit number"+bcolors.ENDC)

def view_all_contacts():
    cursor.execute('''SELECT * FROM contacts''')
    contacts=cursor.fetchall()
    if len(contacts)==0:
        print(bcolors.WARNING+"No contact to show. Please add contacts!"+bcolors.ENDC)
    else:
        for row in contacts:
            print(bcolors.BOLD+"Contact List:"+bcolors.ENDC)
            print(bcolors.OKBLUE+"{} : {} {}".format(row[0],row[1],row[2])+ bcolors.ENDC)
            print(bcolors.UNDERLINE+"Total {} contact(s)...".format(len(contacts))+bcolors.ENDC)

def delete_contact():
    cursor.execute('''SELECT * FROM contacts''')
    contacts=cursor.fetchall()
    if len(contacts)==0:
        print(bcolors.WARNING+"No contact to show. Please add contacts!"+bcolors.ENDC)
    else:
        name = input(bcolors.BOLD+"Enter name to delete: "+bcolors.ENDC)
        cursor.execute('''DELETE FROM contacts where name = (?)''',(name,))
        conn.commit()
        print(bcolors.WARNING+"Deleted contact for {} successfully!".format(name)+bcolors.ENDC)
 
def update_contact():
    name = input(bcolors.BOLD+"Enter name to update contact: "+bcolors.ENDC)
    newNumber = input(bcolors.BOLD+"Enter new number for contact with {}.".format(name)+bcolors.ENDC)
    if len(newNumber)==10:
        cursor.execute('''UPDATE contacts set phone_number = (?) where name=(?)''',(newNumber,name))
        conn.commit()
        print(bcolors.OKBLUE+"Updated contact for {} successfully!".format(name)+bcolors.ENDC)
    else:
        print(bcolors.WARNING+"Contact not available for this name."+bcolors.ENDC)

def search_contact():
    name = input(bcolors.BOLD+"Enter name to update contact: "+bcolors.ENDC)
    cursor.execute('''SELECT * FROM contacts where name = ?''',(name,))
    contacts=cursor.fetchall()
    if len(contacts)==0:
        print(bcolors.WARNING+"No contact to show. Please add contacts!"+bcolors.ENDC)
    else:
        for row in contacts:
            print(bcolors.BOLD+"Contact List:"+bcolors.ENDC)
            print(bcolors.OKBLUE+"{} : {} {}".format(row[0],row[1],row[2])+ bcolors.ENDC)
            print(bcolors.UNDERLINE+"Total {} contact(s)...".format(len(contacts))+bcolors.ENDC)

def search_contact_bynumber():
    number = input(bcolors.BOLD+"Enter number to search contact: "+bcolors.ENDC)
    cursor.execute('''SELECT * FROM contacts where phone_number = ?''',(number,))
    contacts=cursor.fetchall()
    if len(contacts)==0:
        print(bcolors.WARNING+"No contact to show. Please add contacts!"+bcolors.ENDC)
    else:
        for row in contacts:
            print(bcolors.BOLD+"Contact List:"+bcolors.ENDC)
            print(bcolors.OKBLUE+"{} : {} {}".format(row[0],row[1],row[2])+ bcolors.ENDC)
            print(bcolors.UNDERLINE+"Total {} contact(s)...".format(len(contacts))+bcolors.ENDC)
        

while True:
    print("\nMenu:")
    print("1. Add contact")
    print("2. Delete contact")
    print("3. Update contact")
    print("4. View all contacts")
    print("5. Search contact by name")
    print("6. Search contact by number")
    print("7. Exit")
    choice = input("Enter your choice: ")
    print("--------------- Output ---------------")
    if choice == '1':
        add_contact()
    elif choice == '2':
        delete_contact()
    elif choice == '3':
        update_contact()
    elif choice == '4':
        view_all_contacts()
    elif choice == '5':
        search_contact()
    elif choice == '6':
        search_contact_bynumber()
    elif choice == '7':
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 6.")
    print("--------------------------------------")
