# LLM Usage:
# Claude Code to help with menu structure, interactive loop, and demo sequence

from contact import Contact
from address_book import AddressBook
from test import test_all


SEPARATOR = '-' * 40


# ========== HELPERS ==========

# Task: print all contacts in the book with their index numbers
# Solution: loop through list_contacts() and print each with its index,
#           or print a message if the book is empty
def print_contacts(book):
    if book.count() == 0:
        print("(Address book is empty)")
        return
    for i, c in enumerate(book.list_contacts()):
        print(f"  [{i}] {c}")


# Task: show the contact list and ask the user to pick one by index
# Solution: display contacts, read input, validate the index,
#           return -1 if invalid or the book is empty
def pick_contact(book, prompt="Enter contact number: "):
    print_contacts(book)
    if book.count() == 0:
        return -1
    try:
        index = int(input(prompt))
        if book.get_contact(index) is None:
            print("Invalid contact number.")
            return -1
        return index
    except ValueError:
        print("Please enter a number.")
        return -1


# Task: prompt the user to enter values for name, email, and phone
# Solution: read each field, treat blank input as None (skipped),
#           reject and return None if all three fields were left blank
def prompt_fields():
    print("(Leave a field blank to skip it)")
    name  = input("  Name: ").strip() or None
    email = input("  Email: ").strip() or None
    phone = input("  Phone: ").strip() or None
    if name is None and email is None and phone is None:
        print("Error: At least one field is required.")
        return None
    return name, email, phone


# ========== INTERACTIVE ADDRESS BOOK ==========

# Task: run the interactive address book with a looping menu
# Solution: show a menu, read the user's choice, and call the appropriate
#           AddressBook method. Loop until the user chooses to exit.
def run_address_book():
    book = AddressBook()
    while True:
        print(f"\n{SEPARATOR}")
        print("Address Book")
        print(SEPARATOR)
        print("1. Add Contact")
        print("2. View All Contacts")
        print("3. Update Contact")
        print("4. Delete Contact")
        print("5. Merge Two Contacts")
        print("6. Exit")
        print(SEPARATOR)
        choice = input("Choose an option: ").strip()

        if choice == '1':
            print("\n-- Add Contact --")
            fields = prompt_fields()
            if fields is None:
                continue
            name, email, phone = fields
            contact = Contact(name=name, email=email, phone=phone)
            if book.add_contact(contact):
                print("Contact added.")
            else:
                print("Error: That contact already exists.")

        elif choice == '2':
            print("\n-- All Contacts --")
            print_contacts(book)

        elif choice == '3':
            print("\n-- Update Contact --")
            index = pick_contact(book, "Select contact to update: ")
            if index == -1:
                continue
            print(f"Editing: {book.get_contact(index)}")
            print("Enter new values (blank = keep existing, space = clear field):")
            name_in  = input("  Name: ").strip()
            email_in = input("  Email: ").strip()
            phone_in = input("  Phone: ").strip()
            # blank input -> pass None (no change), space input -> pass '' (clear field)
            name_arg  = '' if name_in  == ' ' else (None if name_in  == '' else name_in)
            email_arg = '' if email_in == ' ' else (None if email_in == '' else email_in)
            phone_arg = '' if phone_in == ' ' else (None if phone_in == '' else phone_in)
            if not book.update_contact(index, name=name_arg, email=email_arg, phone=phone_arg):
                print("Error: Update would leave contact empty. At least one field required.")
            else:
                print(f"Updated: {book.get_contact(index)}")

        elif choice == '4':
            print("\n-- Delete Contact --")
            index = pick_contact(book, "Select contact to delete: ")
            if index == -1:
                continue
            contact = book.get_contact(index)
            confirm = input(f"Delete '{contact}'? (y/n): ").strip().lower()
            if confirm == 'y':
                book.delete_contact(index)
                print("Contact deleted.")
            else:
                print("Cancelled.")

        elif choice == '5':
            print("\n-- Merge Two Contacts --")
            if book.count() < 2:
                print("Need at least 2 contacts to merge.")
                continue
            print("Select FIRST contact (its fields take priority):")
            index1 = pick_contact(book, "First contact: ")
            if index1 == -1:
                continue
            print("Select SECOND contact:")
            index2 = pick_contact(book, "Second contact: ")
            if index2 == -1:
                continue
            if book.merge_contacts(index1, index2):
                print(f"Merged into: {book.get_contact(min(index1, index2))}")
            else:
                print("Error: Could not merge (same contact selected twice?).")

        elif choice == '6':
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please enter 1-6.")


# ========== DEMO ==========

# Task: run an automated demonstration showing all address book features
# Solution: create a book, then perform a scripted sequence of add, view,
#           update, merge, and delete operations, printing results at each step
def run_demo():
    print(f"\n{SEPARATOR}")
    print("DEMO: Social Address Book")
    print(SEPARATOR)

    book = AddressBook()

    # add three contacts with varying fields
    print("\n[1] Adding contacts...")
    book.add_contact(Contact(name="Alice Smith", email="alice@example.com", phone="555-1001"))
    book.add_contact(Contact(name="Bob Jones", phone="555-2002"))
    book.add_contact(Contact(email="carol@example.com"))
    print("Added 3 contacts:")
    print_contacts(book)

    # show duplicate rejection
    print(f"\n[2] Attempting to add a duplicate of Alice Smith...")
    result = book.add_contact(Contact(name="Alice Smith", email="alice@example.com", phone="555-1001"))
    print(f"Result: {'Added' if result else 'Rejected — duplicate contact'}")
    print(f"Book still has {book.count()} contacts.")

    # view a single contact by index
    print("\n[3] Viewing contact [1] (Bob Jones):")
    print(f"  {book.get_contact(1)}")

    # update a field on an existing contact
    print("\n[4] Updating Bob Jones' email to bob@example.com...")
    book.update_contact(1, email="bob@example.com")
    print(f"  Updated: {book.get_contact(1)}")

    # add a name to a contact that only had an email
    print("\n[5] Adding a name to contact [2] (Carol)...")
    book.update_contact(2, name="Carol White")
    print(f"  Updated: {book.get_contact(2)}")

    # merge two contacts into one
    print("\n[6] Merging Bob Jones [1] and Carol White [2]...")
    print(f"  Before merge:")
    print(f"    [1] {book.get_contact(1)}")
    print(f"    [2] {book.get_contact(2)}")
    book.merge_contacts(1, 2)
    print(f"  After merge, book has {book.count()} contacts:")
    print_contacts(book)

    # delete a contact
    print("\n[7] Deleting Alice Smith [0]...")
    book.delete_contact(0)
    print(f"  Book now has {book.count()} contact(s):")
    print_contacts(book)

    print(f"\n{SEPARATOR}")
    print("End of demo.")
    print(SEPARATOR)


# ========== MAIN ==========

if __name__ == "__main__":
    print(SEPARATOR)
    print("Social Address Book — Homework 2")
    print(SEPARATOR)
    print("1. Run unit tests")
    print("2. Run demo")
    print("3. Use Address Book")
    print(SEPARATOR)
    choice = input("Choose an option (1/2/3): ").strip()

    if choice == '1':
        test_all()
    elif choice == '2':
        run_demo()
    elif choice == '3':
        run_address_book()
    else:
        print("Invalid choice. Please run the program again and enter 1, 2, or 3.")
