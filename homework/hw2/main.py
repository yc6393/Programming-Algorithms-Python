# LLM Usage Citation:
# Claude (claude-sonnet-4-6) was used to help design and implement this program.
# Specifically: menu structure, interactive loop design, demo sequence,
# and ensuring KISS, DRY, and SRP principles were followed throughout.

from contact import Contact
from address_book import AddressBook
from test import test_all


# ============================================================
# Helpers
# ============================================================

SEPARATOR = '-' * 40


def print_contacts(book):
    """Print all contacts with their index numbers."""
    if book.count() == 0:
        print("(Address book is empty)")
        return
    for i, c in enumerate(book.list_contacts()):
        print(f"  [{i}] {c}")


def pick_contact(book, prompt="Enter contact number: "):
    """Ask user to pick a contact by index. Returns index or -1 on cancel."""
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


def prompt_fields(require_one=True):
    """Prompt the user for contact fields. Returns (name, email, phone) or None if invalid."""
    print("(Leave a field blank to skip it)")
    name = input("  Name: ").strip() or None
    email = input("  Email: ").strip() or None
    phone = input("  Phone: ").strip() or None
    if require_one and name is None and email is None and phone is None:
        print("Error: At least one field is required.")
        return None
    return name, email, phone


# ============================================================
# Interactive Address Book
# ============================================================

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
            print("Enter new values (leave blank to keep existing, enter a space to clear a field):")
            name_in = input("  Name: ").strip()
            email_in = input("  Email: ").strip()
            phone_in = input("  Phone: ").strip()
            # Convert: blank = no change (None arg), single space = clear ('')
            name_arg  = None if name_in  == '' else (None if name_in  == ' ' else name_in)
            email_arg = None if email_in == '' else (None if email_in == ' ' else email_in)
            phone_arg = None if phone_in == '' else (None if phone_in == ' ' else phone_in)
            # '' sentinel for update_contact means "clear the field"
            name_arg  = '' if name_in  == ' ' else (None if name_in  == '' else name_in)
            email_arg = '' if email_in == ' ' else (None if email_in == '' else email_in)
            phone_arg = '' if phone_in == ' ' else (None if phone_in == '' else phone_in)
            book.update_contact(index, name=name_arg, email=email_arg, phone=phone_arg)
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


# ============================================================
# Demo
# ============================================================

def run_demo():
    print(f"\n{SEPARATOR}")
    print("DEMO: Social Address Book")
    print(SEPARATOR)

    book = AddressBook()

    # Add contacts
    print("\n[1] Adding contacts...")
    book.add_contact(Contact(name="Alice Smith", email="alice@example.com", phone="555-1001"))
    book.add_contact(Contact(name="Bob Jones", phone="555-2002"))
    book.add_contact(Contact(email="carol@example.com"))
    print("Added 3 contacts:")
    print_contacts(book)

    # Attempt to add a duplicate
    print(f"\n[2] Attempting to add a duplicate of Alice Smith...")
    result = book.add_contact(Contact(name="Alice Smith", email="alice@example.com", phone="555-1001"))
    print(f"Result: {'Added' if result else 'Rejected — duplicate contact'}")
    print(f"Book still has {book.count()} contacts.")

    # View a specific contact
    print("\n[3] Viewing contact [1] (Bob Jones):")
    print(f"  {book.get_contact(1)}")

    # Update a contact's email
    print("\n[4] Updating Bob Jones' email to bob@example.com...")
    book.update_contact(1, email="bob@example.com")
    print(f"  Updated: {book.get_contact(1)}")

    # Update contact [2] (carol) with a name
    print("\n[5] Adding a name to contact [2] (Carol)...")
    book.update_contact(2, name="Carol White")
    print(f"  Updated: {book.get_contact(2)}")

    # Merge Bob (index 1) and Carol (index 2)
    print("\n[6] Merging Bob Jones [1] and Carol White [2]...")
    print(f"  Before merge:")
    print(f"    [1] {book.get_contact(1)}")
    print(f"    [2] {book.get_contact(2)}")
    book.merge_contacts(1, 2)
    print(f"  After merge, book has {book.count()} contacts:")
    print_contacts(book)

    # Delete Alice
    print("\n[7] Deleting Alice Smith [0]...")
    book.delete_contact(0)
    print(f"  Book now has {book.count()} contact(s):")
    print_contacts(book)

    print(f"\n{SEPARATOR}")
    print("End of demo.")
    print(SEPARATOR)


# ============================================================
# Main Menu
# ============================================================

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
