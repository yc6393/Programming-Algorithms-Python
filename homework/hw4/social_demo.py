# LLM Usage:
# Claude Code (claude-opus-4-6) scaffolded and completed this file for hw4.
# Used to generate the 20-contact demo, edge wiring, and BFS display.

from contact import Contact
from address_book import AddressBook


SEPARATOR = '-' * 40


# Task: demonstrate the Social Address Book's graph capabilities
# Solution: create 20 contacts, wire up a ring plus cross-edges so each
#           contact has at least 2 connections, then display the adjacency
#           list and run a BFS 3rd-degree lookup based on user input
def run_demo():
    book = AddressBook()

    # --- 20 contacts ---
    book.add_contact(Contact(name="Alice Smith",     email="alice@example.com",    phone="555-1001"))   # 0
    book.add_contact(Contact(name="Bob Jones",       email="bob@example.com",      phone="555-1002"))   # 1
    book.add_contact(Contact(name="Carol White",     email="carol@example.com",    phone="555-1003"))   # 2
    book.add_contact(Contact(name="David Brown",     email="david@example.com",    phone="555-1004"))   # 3
    book.add_contact(Contact(name="Eve Davis",       email="eve@example.com",      phone="555-1005"))   # 4
    book.add_contact(Contact(name="Frank Miller",    email="frank@example.com",    phone="555-1006"))   # 5
    book.add_contact(Contact(name="Grace Wilson",    email="grace@example.com",    phone="555-1007"))   # 6
    book.add_contact(Contact(name="Henry Moore",     email="henry@example.com",    phone="555-1008"))   # 7
    book.add_contact(Contact(name="Iris Taylor",     email="iris@example.com",     phone="555-1009"))   # 8
    book.add_contact(Contact(name="Jack Anderson",   email="jack@example.com",     phone="555-1010"))   # 9
    book.add_contact(Contact(name="Karen Thomas",    email="karen@example.com",    phone="555-1011"))   # 10
    book.add_contact(Contact(name="Leo Martinez",    email="leo@example.com",      phone="555-1012"))   # 11
    book.add_contact(Contact(name="Mia Robinson",    email="mia@example.com",      phone="555-1013"))   # 12
    book.add_contact(Contact(name="Noah Clark",      email="noah@example.com",     phone="555-1014"))   # 13
    book.add_contact(Contact(name="Olivia Lewis",    email="olivia@example.com",   phone="555-1015"))   # 14
    book.add_contact(Contact(name="Paul Walker",     email="paul@example.com",     phone="555-1016"))   # 15
    book.add_contact(Contact(name="Quinn Hall",      email="quinn@example.com",    phone="555-1017"))   # 16
    book.add_contact(Contact(name="Ruby Allen",      email="ruby@example.com",     phone="555-1018"))   # 17
    book.add_contact(Contact(name="Sam Young",       email="sam@example.com",      phone="555-1019"))   # 18
    book.add_contact(Contact(name="Tina King",       email="tina@example.com",     phone="555-1020"))   # 19

    # --- ring edges: connect each contact to its neighbor in a circular chain ---
    # guarantees every contact has at least 2 connections
    for i in range(20):
        book.add_edge(i, (i + 1) % 20)

    # --- cross edges: add shortcuts across the ring ---
    book.add_edge(0, 5)
    book.add_edge(5, 10)
    book.add_edge(10, 15)
    book.add_edge(2, 17)

    # --- display full adjacency list (1st degree graph) ---
    print(f"\n{SEPARATOR}")
    print("DEMO: Social Address Book — Homework 4")
    print(SEPARATOR)
    print(f"\nAddress book loaded with {book.count()} contacts.\n")
    book.display_adjacency_list()

    # --- display 3rd degree connections via BFS ---
    print()
    node_id = int(input("Enter Node ID (0-19) for BFS depth check: "))
    print()
    book.display_third_degree(node_id)

    print(f"\n{SEPARATOR}")
    print("End of demo.")
    print(SEPARATOR)


if __name__ == "__main__":
    run_demo()
