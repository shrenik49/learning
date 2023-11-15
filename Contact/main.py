contacts = {}

def add_contact():
    name = input("Enter name")
    number = input("Enter mobile number")
    contacts[name]={number}


def view_all_contacts():
    for name ,number in contacts.items():
        print(f"{name} : {number}" )

while True:
    print("\nMenu:")
    print("1. Add contact")
    print("2. Delete contact")
    print("3. Update contact")
    print("4. View all contacts")
    print("5. Search contact by name")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        add_contact()

    elif choice == '4':
        view_all_contacts()
    # elif choice == '2':
    #     delete_contact()
    # elif choice == '3':
    #     update_contact()
    # elif choice == '5':
    #     search_contact()
    elif choice == '6':
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 6.")
