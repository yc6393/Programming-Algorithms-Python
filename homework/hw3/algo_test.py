# LLM Usage:
# Claude Code (claude-sonnet-4-6) scaffolded this file for hw3.
# Used to fix bugs in test bodies (wrong order, missing .get_name(), wrong args).

from contact import Contact
from address_book import AddressBook


# ========== sort_contacts TESTS ==========

def test_sort_contacts_common():
    """common: three contacts sorted by name in descending order"""
    book = AddressBook()
    book.add_contact(Contact(name="Ayuri"))
    book.add_contact(Contact(name="Byuri"))
    book.add_contact(Contact(name="Zyuri"))
    result = book.sort_contacts('name')
    # descending: Z comes first, A comes last
    assert result[0].get_name() == "Zyuri"
    assert result[1].get_name() == "Byuri"
    assert result[2].get_name() == "Ayuri"

def test_sort_contacts_edge():
    """edge: sorting an empty address book returns an empty list"""
    book = AddressBook()
    result = book.sort_contacts('name')
    assert result == []

def test_sort_contacts_special():
    """special: contacts missing the sort field sink to the bottom"""
    book = AddressBook()
    book.add_contact(Contact(name="Ayuri"))
    book.add_contact(Contact(email="yuri@gmail.com"))  # no name, sinks to bottom
    book.add_contact(Contact(name="Zyuri"))
    result = book.sort_contacts('name')
    # named contacts come first descending, None-name contact last
    assert result[0].get_name() == "Zyuri"
    assert result[1].get_name() == "Ayuri"
    assert result[2].get_name() is None


# ========== search_contacts TESTS ==========

def test_search_contacts_common():
    """common: searching by name finds the matching contact"""
    book = AddressBook()
    book.add_contact(Contact(name="Ayuri"))
    book.add_contact(Contact(name="Byuri"))
    book.add_contact(Contact(name="Zyuri"))
    result = book.search_contacts('name', 'Ayuri')
    assert len(result) == 1
    assert result[0].get_name() == "Ayuri"

def test_search_contacts_edge():
    """edge: searching an empty address book returns an empty list"""
    book = AddressBook()
    result = book.search_contacts('name', 'rando')
    assert result == []

def test_search_contacts_special():
    """special: searching for a value that doesn't exist returns an empty list"""
    book = AddressBook()
    book.add_contact(Contact(name="Ayuri"))
    book.add_contact(Contact(name="Byuri"))
    book.add_contact(Contact(name="Cyuri"))
    result = book.search_contacts('name', 'Zyuri')
    assert result == []


# ========== TEST RUNNER ==========

def test_all():
    tests = [
        test_sort_contacts_common,
        test_sort_contacts_edge,
        test_sort_contacts_special,
        test_search_contacts_common,
        test_search_contacts_edge,
        test_search_contacts_special,
    ]
    for test in tests:
        test()
    print(f"OK: All {len(tests)} tests passed.")


if __name__ == "__main__":
    test_all()
