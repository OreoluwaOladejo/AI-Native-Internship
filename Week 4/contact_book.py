# Store contacts in a dictionary becasue it has like key and value 
contacts = {}
# Store phone numbers in a set to prevent duplicates
phone_numbers = set()

# Use a tuple for fixed contact field names
CONTACT_FIELDS = ("phone", "email")


# Keep displaying the menu until the user exits
while True:
    print("\n CONTACT BOOK ")
    print("1. Add contact")
    print("2. Update contact")
    print("3. Remove contact")
    print("4. Look up contact")
    print("5. Display all contacts")
    print("6. Exit")

    choice = input("Choose an option: ")

    # For adding contacts do this 

    if choice == "1":
        name = input("Enter name: ").strip()
        phone = input("Enter phone number: ").strip()
        email = input("Enter email: ").strip()

        if not name:
            print("Name cannot be empty.")

        elif name in contacts:
            print("Contact already exists.")

        elif phone in phone_numbers:
            print("Phone number already exists.")

        else:
            contacts[name] = {
                CONTACT_FIELDS[0]: phone,
                CONTACT_FIELDS[1]: email
            }

            phone_numbers.add(phone)
            print("Contact added successfully.")

    # For updating contacts 
    elif choice == "2":
        name = input("Enter the name to update: ").strip()

        if name not in contacts:
            print("Contact not found.")

        else:
            print("1. Update phone number")
            print("2. Update email")

            detail = input("Choose what to update: ")

            if detail == "1":
                new_phone = input("Enter new phone number: ").strip()
                old_phone = contacts[name]["phone"]

                if not new_phone:
                    print("Phone number cannot be empty.")

                elif new_phone != old_phone and new_phone in phone_numbers:
                    print("Phone number already belongs to another contact.")

                else:
                    phone_numbers.remove(old_phone)
                    phone_numbers.add(new_phone)
                    contacts[name]["phone"] = new_phone
                    print("Phone number updated.")

            elif detail == "2":
                new_email = input("Enter new email: ").strip()
                contacts[name]["email"] = new_email
                print("Email updated successfully.")

            else:
                print("Invalid option.")

    # REMOVE CONTACT
    elif choice == "3":
        name = input("Enter the name to remove: ").strip()

        if name in contacts:
            phone = contacts[name]["phone"]

            # Remove the phone number from the set first
            phone_numbers.remove(phone)

            # Remove the contact from the dictionary
            del contacts[name]

            print("Contact removed successfully.")

        else:
            print("Contact not found.")

    # For looking up contscts 
    elif choice == "4":
        name = input("Enter the name to search for: ").strip()

        if name in contacts:
            print(f"\nName: {name}")
            print(f"Phone: {contacts[name]['phone']}")
            print(f"Email: {contacts[name]['email']}")

        else:
            print("Contact not found.")

    # Dispalying contacts
    elif choice == "5":
        if not contacts:
            print("Your contact book is empty.")

        else:
            for name, details in contacts.items():
                print(f"\nName: {name}")
                print(f"Phone: {details['phone']}")
                print(f"Email: {details['email']}")

    # Exiting the loop or menu 
    elif choice == "6":
        print("Bye for now ")
        break

    else:
        print("Invalid choice. Try again.")