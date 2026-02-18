"""
Main program for the Social Address Book.
Provides menu interface for tests, demo, and direct usage.
Implemented as a set of functions following functional programming style.
"""

import sys
import unittest
from contact import Contact
from address_book import AddressBook
import test  # Import the test module

# Global address book instance
address_book = None

def initialize_address_book():
    """Initialize the global address book with demo data."""
    global address_book
    address_book = AddressBook()
    setup_demo_data()

def setup_demo_data():
    """Add some Star Wars characters as demo contacts."""
    global address_book
    demo_contacts = [
        Contact("Luke Skywalker", "luke@jediorder.org", "555-0123"),
        Contact("Leia Organa", "leia@rebellion.com", "555-0456"),
        Contact("Han Solo", "han@millenniumfalcon.net", "555-0789"),
        Contact("Darth Vader", "vader@empire.gov", "555-0001"),
        Contact("Yoda", "yoda@jediorder.org"),
        Contact("Obi-Wan Kenobi", "ben@jediorder.org", "555-0003"),
        Contact(email="darkside.support@empire.gov"),
        Contact(name="R2D2"),
        Contact(phone="800-DEATH-STAR"),
    ]
    for contact in demo_contacts:
        address_book.add_contact(contact)

def run_tests():
    """Run all unit tests."""
    print("\n" + "="*50)
    print("RUNNING UNIT TESTS")
    print("="*50)
    
    # Run the tests
    test_suite = unittest.TestLoader().loadTestsFromModule(test)
    test_runner = unittest.TextTestRunner(verbosity=2)
    result = test_runner.run(test_suite)
    
    print("\nTest Summary:")
    print(f"Tests run: {result.testsRun}")
    print(f"Failures: {len(result.failures)}")
    print(f"Errors: {len(result.errors)}")
    
    input("\nPress Enter to return to main menu...")

def display_all_contacts():
    """Display all contacts in the address book."""
    global address_book
    contacts = address_book.get_all_contacts()
    if not contacts:
        print("   No contacts in address book")
    else:
        for i, contact in enumerate(contacts, 1):
            print(f"   {i}. {contact}")

def run_demo():
    """Run a demonstration of the address book with Star Wars characters."""
    global address_book
    print("\n" + "="*50)
    print("ADDRESS BOOK DEMONSTRATION")
    print("Star Wars Edition")
    print("="*50)
    
    # Show initial contacts
    print("\n1. Initial Contacts in Address Book:")
    display_all_contacts()
    
    # Add a new contact
    print("\n2. Adding a new contact (Chewbacca):")
    new_contact = Contact("Chewbacca", "chewie@millenniumfalcon.net", "555-4242")
    if address_book.add_contact(new_contact):
        print("✓ Chewbacca added successfully!")
    else:
        print("✗ Failed to add contact (possible duplicate)")
    display_all_contacts()
    
    # Update a contact
    print("\n3. Updating Han Solo's contact:")
    han_matches = address_book.find_contact("Han")
    if han_matches:
        han = han_matches[0]
        if address_book.update_contact(han, phone="555-0000"):
            print("✓ Han Solo's contact updated successfully!")
        else:
            print("✗ Failed to update contact")
    else:
        print("   Han Solo not found in contacts")
    display_all_contacts()
    
    # Search for contacts
    print("\n4. Searching for Jedi contacts (searching for 'jedi'):")
    matches = address_book.find_contact("jedi")
    if matches:
        for contact in matches:
            print(f"   Found: {contact}")
    else:
        print("   No Jedi found")
    
    # Demonstrate merge concept
    print("\n5. Merge demonstration (showing how merge would work):")
    yoda_matches = address_book.find_contact("Yoda")
    leia_matches = address_book.find_contact("Leia")
    
    if yoda_matches and leia_matches:
        yoda = yoda_matches[0]
        leia = leia_matches[0]
        print(f"   Contact 1: {yoda}")
        print(f"   Contact 2: {leia}")
        print(f"   Merged would be: Name='{yoda.name or leia.name}', "
              f"Email='{yoda.email or leia.email}', "
              f"Phone='{yoda.phone or leia.phone}'")
    address_book.merge_contacts(yoda, leia)
    display_all_contacts()

    # Delete a contact
    print("\n6. Deleting Darth Vader:")
    vader_matches = address_book.find_contact("Vader")
    if vader_matches:
        vader = vader_matches[0]
        if address_book.delete_contact(vader):
            print("✓ Darth Vader deleted successfully")
        else:
            print("✗ Failed to delete contact")
    else:
        print("   Darth Vader not found in contacts")
    display_all_contacts()
    
    print("\n" + "="*50)
    print("DEMONSTRATION COMPLETE")
    print("May the Force be with you!")
    print("="*50)
    input("\nPress Enter to return to main menu...")

def print_interactive_menu():
    """Print the interactive menu."""
    global address_book
    print("\n" + "="*50)
    print("SOCIAL ADDRESS BOOK - INTERACTIVE MODE")
    print("Star Wars Edition")
    print("="*50)
    print("1. Add a new contact")
    print("2. View all contacts")
    print("3. Find a contact")
    print("4. Update a contact")
    print("5. Delete a contact")
    print("6. Merge two contacts")
    print("7. Return to main menu")
    print("-" * 50)
    print(f"Total contacts in your Holocron: {address_book.size()}")

def add_contact_interactive():
    """Interactive contact addition."""
    global address_book
    print("\n--- Add New Contact to Your Holocron ---")
    print("(Press Enter to skip any field)")
    print("Example: Enter Star Wars character details")
    
    name = input("Name (e.g., 'R2-D2'): ").strip()
    email = input("Email (e.g., 'r2d2@droids.com'): ").strip()
    phone = input("Phone (e.g., '555-beepboop'): ").strip()
    
    if not (name or email or phone):
        print("Error: Contact must have at least one field.")
        return
    
    contact = Contact(name, email, phone)
    
    if address_book.add_contact(contact):
        print("✓ Contact added successfully to your Holocron!")
    else:
        print("✗ Failed to add contact. It may be a duplicate or invalid.")

def view_all_contacts():
    """Display all contacts."""
    print("\n--- Your Holocron Contacts ---")
    display_all_contacts()

def find_contact_interactive():
    """Interactive contact search."""
    global address_book
    if address_book.size() == 0:
        print("\nYour Holocron is empty. Add some contacts first.")
        return
    
    search = input("\nEnter name, email, or phone to search (e.g., 'Jedi'): ").strip()
    if not search:
        print("Search term cannot be empty.")
        return
    
    matches = address_book.find_contact(search)
    
    if matches:
        print(f"\nFound {len(matches)} matching contact(s) in your Holocron:")
        for i, contact in enumerate(matches, 1):
            print(f"{i}. {contact}")
    else:
        print("No matching contacts found in the galaxy.")

def update_contact_interactive():
    """Interactive contact update."""
    global address_book
    if address_book.size() == 0:
        print("\nYour Holocron is empty. Add some contacts first.")
        return
    
    # First, find the contact to update
    search = input("\nEnter name, email, or phone of contact to update: ").strip()
    matches = address_book.find_contact(search)
    
    if not matches:
        print("No matching contacts found.")
        return
    
    contact = select_contact_from_matches(matches, "update")
    if not contact:
        return
    
    print(f"\nUpdating: {contact}")
    print("\nEnter new values (press Enter to keep current value):")
    
    name_input = input(f"Name [{contact.name}]: ").strip()
    email_input = input(f"Email [{contact.email}]: ").strip()
    phone_input = input(f"Phone [{contact.phone}]: ").strip()
    
    # Use None for fields not provided (keeps existing)
    name = name_input if name_input else None
    email = email_input if email_input else None
    phone = phone_input if phone_input else None
    
    if address_book.update_contact(contact, name, email, phone):
        print("✓ Contact updated successfully!")
    else:
        print("✗ Failed to update contact. Update may create a duplicate.")

def delete_contact_interactive():
    """Interactive contact deletion."""
    global address_book
    if address_book.size() == 0:
        print("\nYour Holocron is empty. Add some contacts first.")
        return
    
    search = input("\nEnter name, email, or phone of contact to delete: ").strip()
    matches = address_book.find_contact(search)
    
    if not matches:
        print("No matching contacts found.")
        return
    
    contact = select_contact_from_matches(matches, "delete")
    if not contact:
        return
    
    confirm = input(f"\nAre you sure you want to delete {contact.name} from your Holocron? (y/n): ").strip().lower()
    if confirm == 'y':
        if address_book.delete_contact(contact):
            print(f"✓ {contact.name} has been removed from your Holocron.")
        else:
            print("✗ Failed to delete contact.")
    else:
        print("Deletion cancelled.")

def select_contact_from_matches(matches, action):
    """
    Helper function to select a contact from multiple matches.
    
    Args:
        matches (list): List of matching contacts
        action (str): Action being performed (for display)
    
    Returns:
        Contact or None: Selected contact or None if invalid selection
    """
    if len(matches) > 1:
        print(f"\nMultiple matches found. Please select one to {action}:")
        for i, contact in enumerate(matches, 1):
            print(f"{i}. {contact}")
        
        try:
            choice = int(input(f"\nSelect contact number: "))
            if 1 <= choice <= len(matches):
                return matches[choice-1]
            else:
                print("Invalid selection.")
                return None
        except ValueError:
            print("Invalid input.")
            return None
    else:
        return matches[0]

def merge_contacts_interactive():
    """Interactive contact merging."""
    global address_book
    if address_book.size() < 2:
        print("\nNeed at least 2 contacts to merge.")
        return
    
    print("\n--- Merge Two Contacts in Your Holocron ---")
    print("Like combining the knowledge of two Jedi Masters")
    contacts = address_book.get_all_contacts()
    
    print("\nCurrent contacts:")
    for i, contact in enumerate(contacts, 1):
        print(f"{i}. {contact}")
    
    try:
        # Select first contact
        choice1 = int(input("\nSelect first contact number: "))
        if 1 <= choice1 <= len(contacts):
            contact1 = contacts[choice1-1]
        else:
            print("Invalid selection.")
            return
        
        # Select second contact
        choice2 = int(input("Select second contact number: "))
        if 1 <= choice2 <= len(contacts) and choice2 != choice1:
            contact2 = contacts[choice2-1]
        else:
            print("Invalid selection. Must select a different contact.")
            return
        
        # Show merge preview
        print(f"\nMerging:")
        print(f"1. {contact1}")
        print(f"2. {contact2}")
        
        # Show what the merged contact would look like
        merged_name = contact1.name or contact2.name
        merged_email = contact1.email or contact2.email
        merged_phone = contact1.phone or contact2.phone
        print(f"\nResult would be: Name='{merged_name}', Email='{merged_email}', Phone='{merged_phone}'")
        print("Like the creation of a Force Dyad!")
        
        confirm = input("\nProceed with merge? (y/n): ").strip().lower()
        if confirm == 'y':
            merged = address_book.merge_contacts(contact1, contact2)
            if merged:
                print(f"✓ Contacts merged successfully!")
                print(f"   Result: {merged}")
            else:
                print("✗ Failed to merge contacts. Merge may create a duplicate.")
        else:
            print("Merge cancelled.")
            
    except ValueError:
        print("Invalid input. Please enter numbers only.")

def run_interactive():
    """Run interactive address book program."""
    global address_book
    while True:
        print_interactive_menu()
        choice = input("\nEnter your choice (1-7): ").strip()
        
        if choice == '1':
            add_contact_interactive()
        elif choice == '2':
            view_all_contacts()
        elif choice == '3':
            find_contact_interactive()
        elif choice == '4':
            update_contact_interactive()
        elif choice == '5':
            delete_contact_interactive()
        elif choice == '6':
            merge_contacts_interactive()
        elif choice == '7':
            print("\nReturning to main menu...")
            break
        else:
            print("\nInvalid choice. Please enter a number between 1 and 7.")
        
        if choice in ['1', '2', '3', '4', '5', '6']:
            input("\nPress Enter to continue...")

def print_main_menu():
    """Print the main menu."""
    print("\n" + "="*50)
    print("SOCIAL ADDRESS BOOK")
    print("Star Wars Edition")
    print("="*50)
    print("1. Run Unit Tests")
    print("2. Run Demonstration")
    print("3. Use Address Book Directly")
    print("4. Exit")
    print("-" * 50)
    print("May the Force be with you!")

def main():
    """Main program entry point."""
    # Initialize the address book
    initialize_address_book()
    
    while True:
        print_main_menu()
        choice = input("Enter your choice (1-4): ").strip()
        
        if choice == '1':
            run_tests()
        elif choice == '2':
            run_demo()
        elif choice == '3':
            run_interactive()
        elif choice == '4':
            print("\nThank you for using Social Address Book. May the Force be with you!")
            sys.exit(0)
        else:
            print("\nInvalid choice. Please enter a number between 1 and 4.")
            input("Press Enter to continue...")

if __name__ == "__main__":
    # Import unittest here to ensure it's available
    import unittest
    main()