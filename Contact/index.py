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
        contacts[name]=number
        print(bcolors.OKGREEN + "Added contact for {} successfully!".format(name)+ bcolors.ENDC)
    else:
        print(bcolors.WARNING + "Please enter valid 10 digit number"+bcolors.ENDC)

def view_all_contacts():
    if len(contacts)==0:
        print("No contact to show. Please add contacts!")
        print(bcolors.WARNING+"No contact to show. Please add contacts!"+bcolors.ENDC)
    else:
        print("Contact List:")
        print(bcolors.BOLD+"Contact List:"+bcolors.ENDC)
        for name ,number in contacts.items():
            print(bcolors.OKBLUE+"{} : {}".format(name,number)+ bcolors.ENDC)
        print(bcolors.UNDERLINE+"Total {} contact(s)...".format(len(contacts))+bcolors.ENDC)

def delete_contact():
    name = input(bcolors.BOLD+"Enter name to delete: "+bcolors.ENDC)
    try:
        del contacts[name]
        print(bcolors.WARNING+"Deleted contact for {} successfully!".format(name)+bcolors.ENDC)
    except KeyError:
        print(bcolors.WARNING+"Please enter valid name to delete."+bcolors.ENDC)

def update_contact():
    name = input(bcolors.BOLD+"Enter name to update contact: "+bcolors.ENDC)
    newNumber = input(bcolors.BOLD+"Enter new number for contact with {}.".format(name)+bcolors.ENDC)
    if name in contacts :
        if len(newNumber)== 10:
            contacts[name]=newNumber
            print(bcolors.OKBLUE+"Updated contact for {} successfully!".format(name)+bcolors.ENDC)
        else:
            print(bcolors.WARNING + "Please enter valid 10 digit number"+bcolors.ENDC)
    else:
        print("Contact not available for this name.")
        print(bcolors.WARNING+"Contact not available for this name."+bcolors.ENDC)

def search_contact():
    if len(contacts)==0:
        print(bcolors.WARNING+"No contact to show. Please add contacts!"+bcolors.ENDC)
    else:
        name = input(bcolors.BOLD+"Enter name to search contact: "+bcolors.ENDC)
        if name in contacts:
            print(bcolors.OKBLUE+"{}:{}".format(name,contacts[name])+bcolors.ENDC)
        else:
            print(bcolors.WARNING+"Contact not available for this name."+bcolors.ENDC)

def search_contact_bynumber():
    number = input(bcolors.BOLD+"Enter number to search contact: "+bcolors.ENDC)
    flag=0
    for name,phone in contacts.items():
        if number == phone:
            print(bcolors.OKBLUE+"{}:{}".format(name,phone)+bcolors.ENDC)
            flag=1
            break
    if flag==0:
        print(bcolors.WARNING+"Contact not available for this name."+bcolors.ENDC)


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
    elif choice == '4':
        view_all_contacts()
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