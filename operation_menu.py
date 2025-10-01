def add_contact(contacts):
    name = input("Enter contact name: ")
    phone = input("Enter contact number: ")
    email = input("Enter email: ")
    contacts[name] = {"phone": phone, "email": email}   # 🔹 Guardamos en el diccionario
    print(f'Contact {name} has been added to your contact book successfully.')


def view_contacts(contacts):
    if contacts:
        print("\n --- Contact List ---")
        for name, details in contacts.items():
            print(f'Name: {name}')
            print(f"Phone: {details['phone']}")
            print(f"Email: {details['email']}")
            print("-" * 20)
    else:
        print("Your contact book is empty.")


def search_contact(contacts):
    name = input("Enter the name of the contact you want to search: ")
    if name in contacts:
        print(f"\n --- Contact Details for {name} ---")
        print(f"Name: {name}")
        print(f"Phone: {contacts[name]['phone']}")
        print(f"Email: {contacts[name]['email']}")
    else:
        print(f"Contact {name} not found in your contact book.")


def edit_contact(contacts):
    name = input("Enter the name of the contact you want to edit: ")
    if name in contacts:
        phone = input("Enter new phone: ")
        email = input("Enter new Email: ")
        contacts[name] = {"phone": phone, "email": email}
        print(f"Contact {name} has been updated successfully.")
    else:
        print(f"Contact {name} not found in your contact book.")


def delete_contact(contacts):
    name = input("Enter the name of the contact you want to delete: ")
    if name in contacts:
        del contacts[name]
        print(f"Contact {name} has been deleted successfully.")
    else:
        print(f"Contact {name} not found in your contact book.")


def select_option_menu(option, contacts):
    if option == "1":
        add_contact(contacts)
    elif option == "2":
        view_contacts(contacts)
    elif option == "3":
        search_contact(contacts)
    elif option == "4":
        edit_contact(contacts)
    elif option == "5":
        delete_contact(contacts)
    elif option == "6":
        print("Thanks you for using the Contact Book. Goodbye!")
        return False  # 🔹 Indicamos que el programa debe terminar
    else:
        print("Invalid choice. Please select a valid option (1-6).")
    return True  # 🔹 Continuamos ejecutando
