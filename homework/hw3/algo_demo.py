# LLM Usage:
# Claude Code (claude-sonnet-4-6) scaffolded and completed this file for hw3.

from contact import Contact
from address_book import AddressBook


SEPARATOR = '-' * 40


# Task: print a list of Contact objects returned by sort or search
# Solution: handle the empty case first, then loop with enumerate and print each entry
def print_results(contacts):
    # if the list is empty, say so and stop
    if not contacts:
        print("  (no results)")
        return
    # enumerate gives us both the index and the contact on each iteration
    for i, c in enumerate(contacts):
        print(f"  [{i}] {c}")


# Task: demonstrate sort_contacts and search_contacts on a 12-contact address book
# Solution: build the book, then show each method with different fields and values,
#           including a no-match search so the empty-result path is visible
def run_demo():
    book = AddressBook()

    # --- address book data ---
    book.add_contact(Contact(name="Alice Smith",   email="alice@example.com",  phone="555-1001"))
    book.add_contact(Contact(name="Bob Jones",     email="bob@example.com",    phone="555-2002"))
    book.add_contact(Contact(name="Carol White",   email="carol@example.com",  phone="555-3003"))
    book.add_contact(Contact(name="David Brown",   email="david@example.com",  phone="555-4004"))
    book.add_contact(Contact(name="Eve Davis",     email="eve@example.com",    phone="555-5005"))
    book.add_contact(Contact(name="Frank Miller",  email="frank@example.com",  phone="555-6006"))
    book.add_contact(Contact(name="Grace Wilson",  email="grace@example.com",  phone="555-7007"))
    book.add_contact(Contact(name="Henry Moore",   email="henry@example.com",  phone="555-8008"))
    book.add_contact(Contact(name="Iris Taylor",   email="iris@example.com",   phone="555-9009"))
    book.add_contact(Contact(name="Jack Anderson", email="jack@example.com",   phone="555-0010"))
    book.add_contact(Contact(name="Karen Thomas",  email="karen@example.com"))   # no phone
    book.add_contact(Contact(email="anon@example.com", phone="555-1212"))        # no name

    # print the full unsorted book first
    print(f"\n{SEPARATOR}")
    print("DEMO: Social Address Book — Homework 3")
    print(SEPARATOR)
    print(f"\nAddress book loaded with {book.count()} contacts:")
    print_results(book.list_contacts())

    # sort by name descending — Z before A
    print(f"\n{SEPARATOR}")
    print("SORT by name (descending):")
    print(SEPARATOR)
    print_results(book.sort_contacts('name'))

    # sort by phone descending — highest number first
    print(f"\n{SEPARATOR}")
    print("SORT by phone (descending):")
    print(SEPARATOR)
    print_results(book.sort_contacts('phone'))

    # sort by email descending — Z before A on email
    print(f"\n{SEPARATOR}")
    print("SORT by email (descending):")
    print(SEPARATOR)
    print_results(book.sort_contacts('email'))

    # search by name — should find exactly one match
    print(f"\n{SEPARATOR}")
    print("SEARCH name = 'Grace Wilson':")
    print(SEPARATOR)
    results = book.search_contacts('name', 'Grace Wilson')
    if results:
        print_results(results)
    else:
        print("  No contacts found matching that name.")

    # search by email — should find exactly one match
    print(f"\n{SEPARATOR}")
    print("SEARCH email = 'bob@example.com':")
    print(SEPARATOR)
    results = book.search_contacts('email', 'bob@example.com')
    if results:
        print_results(results)
    else:
        print("  No contacts found matching that email.")

    # search by phone — should find exactly one match
    print(f"\n{SEPARATOR}")
    print("SEARCH phone = '555-5005':")
    print(SEPARATOR)
    results = book.search_contacts('phone', '555-5005')
    if results:
        print_results(results)
    else:
        print("  No contacts found matching that phone.")

    # search by name — no match, shows the empty-result path
    print(f"\n{SEPARATOR}")
    print("SEARCH name = 'Zara Unknown' (no match expected):")
    print(SEPARATOR)
    results = book.search_contacts('name', 'Zara Unknown')
    if results:
        print_results(results)
    else:
        print("  No contacts found matching that name.")

    print(f"\n{SEPARATOR}")
    print("End of demo.")
    print(SEPARATOR)


if __name__ == "__main__":
    run_demo()
