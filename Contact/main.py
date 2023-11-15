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
    name = input("Enter name: ")
    number = input("Enter mobile number: ")
    contacts[name]=number
    print(bcolors.OKGREEN + "Added contact for {} successfully!".format(name)+ bcolors.ENDC)

def view_all_contacts():
    if len(contacts)==0:
        print("No contact to show. Please add contacts!")
    else:
        print("Contact List:")
        for name ,number in contacts.items():
            print("{} : {}".format(name,number))
        print("Total {} contact(s)...".format(len(contacts)))
def delete_contact():
    name = input("Enter name to delete: ")
    try:
        del contacts[name]
        print("Deleted contact for {} successfully!".format(name))
    except KeyError:
        print("Please enter valid name to delete.")
 
def update_contact():
    name = input("Enter name to update contact: ")
    newNumber = input("Enter new number for contact with {}.".format(name))
    if contacts[name] :
        contacts[name]=newNumber
        print("Updated contact for {} successfully!".format(name))
    else:
        print("Contact not available for this name.")
        
def search_contact():
    name = input("Enter name to search contact: ")
    if contacts[name] :
        print("{}:{}".format(name,contacts[name]))
    else:
        print("Contact not available for this name.")

while True:
    print("\nMenu:")
    print("1. Add contact")
    print("2. Delete contact")
    print("3. Update contact")
    print("4. View all contacts")
    print("5. Search contact by name")
    print("6. Exit")
    choice = input("Enter your choice: ")
    print("--------------- Output ---------------")
    if choice == '1':
        add_contact()
    elif choice == '4':
        view_all_contacts()
    elif choice == '2':
        delete_contact()
    elif choice == '3':
        update_contact()
    elif choice == '5':
        search_contact()
    elif choice == '6':
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 6.")
    print("--------------------------------------")
