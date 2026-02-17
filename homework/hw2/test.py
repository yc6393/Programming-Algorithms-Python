# LLM Usage:
# Claude Code to help with all tests

from contact import Contact
from address_book import AddressBook


# ========== CONTACT TESTS ==========

# __init__

def test_contact_init_common():
    """common: create contact with all three fields"""
    c = Contact(name="Yuri", email="yuri@gmail.com", phone="123-4567")
    assert c.get_name() == "Yuri"
    assert c.get_email() == "yuri@gmail.com"
    assert c.get_phone() == "123-4567"

def test_contact_init_edge():
    """edge: create contact with only one field"""
    c = Contact(name="blah")
    assert c.get_name() == "blah"
    assert c.get_email() is None
    assert c.get_phone() is None

def test_contact_init_special():
    """creating contact with no fields raises ValueError"""
    try:
        Contact()
        assert False, "Should have raised ValueError"
    except ValueError:
        pass


# get_name / set_name

def test_contact_set_get_name_common():
    """set and retrieve common name"""
    c = Contact(name="Yuri")
    c.set_name("Yuri Cool")
    assert c.get_name() == "Yuri Cool"

def test_contact_set_get_name_edge():
    """set name to None"""
    c = Contact(name="Yuri", email="yuri@gmail.com")
    c.set_name(None)
    assert c.get_name() is None

def test_contact_set_get_name_special():
    """set name with special characters"""
    c = Contact(name="Yuri")
    c.set_name("O'Brien-Smith, Jr.")
    assert c.get_name() == "O'Brien-Smith, Jr."


# get_email / set_email

def test_contact_set_get_email_common():
    """set and retrieve common email"""
    c = Contact(name="Yuri")
    c.set_email("yuri@gmail.com")
    assert c.get_email() == "yuri@gmail.com"

def test_contact_set_get_email_edge():
    """set email to None"""
    c = Contact(name="Yuri", email="yuri@gmail.com")
    c.set_email(None)
    assert c.get_email() is None

def test_contact_set_get_email_special():
    """set email with subdomain and plus addressing"""
    c = Contact(name="Yuri")
    c.set_email("user+tag@sub.domain.org")
    assert c.get_email() == "user+tag@sub.domain.org"


# get_phone / set_phone

def test_contact_set_get_phone_common():
    """set and retrieve common phone number"""
    c = Contact(name="Yuri")
    c.set_phone("123-4567")
    assert c.get_phone() == "123-4567"

def test_contact_set_get_phone_edge():
    """set phone to None"""
    c = Contact(name="Yuri", phone="123-4567")
    c.set_phone(None)
    assert c.get_phone() is None

def test_contact_set_get_phone_special():
    """set phone with international format"""
    c = Contact(name="Yuri")
    c.set_phone("+1 (212) 555-9999")
    assert c.get_phone() == "+1 (212) 555-9999"


# __str__

def test_contact_str_common():
    """string includes all three fields"""
    c = Contact(name="Yuri", email="yuri@gmail.com", phone="123-4567")
    result = str(c)
    assert "Yuri" in result
    assert "yuri@gmail.com" in result
    assert "123-4567" in result

def test_contact_str_edge():
    """string with only one field set"""
    c = Contact(name="Yuri")
    result = str(c)
    assert "Yuri" in result
    assert "Email" not in result
    assert "Phone" not in result

def test_contact_str_special():
    """string with only email set, no name"""
    c = Contact(email="yuri@gmail.com")
    result = str(c)
    assert "yuri@gmail.com" in result
    assert "Name" not in result


# __eq__

def test_contact_eq_common():
    """two contacts with identical fields are equal"""
    c1 = Contact(name="Yuri", email="yuri@gmail.com", phone="123-4567")
    c2 = Contact(name="Yuri", email="yuri@gmail.com", phone="123-4567")
    assert c1 == c2

def test_contact_eq_edge():
    """two contacts with one differing field are not equal"""
    c1 = Contact(name="Yuri", email="yuri@gmail.com")
    c2 = Contact(name="Yuri", email="different@gmail.com")
    assert c1 != c2

def test_contact_eq_special():
    """contact compared to a non-Contact object returns False"""
    c = Contact(name="Yuri")
    assert c != "Yuri"
    assert c != 42
    assert c != None


# ========== ADDRESSBOOK TESTS ==========

# add_contact

def test_add_contact_common():
    """add a new contact successfully"""
    book = AddressBook()
    c = Contact(name="Yuri")
    result = book.add_contact(c)
    assert result is True
    assert book.count() == 1

def test_add_contact_edge():
    """adding a duplicate contact returns False and is not added"""
    book = AddressBook()
    c1 = Contact(name="Yuri", email="yuri@gmail.com")
    c2 = Contact(name="Yuri", email="yuri@gmail.com")
    book.add_contact(c1)
    result = book.add_contact(c2)
    assert result is False
    assert book.count() == 1

def test_add_contact_special():
    """add multiple distinct contacts, all succeed"""
    book = AddressBook()
    for i in range(5):
        result = book.add_contact(Contact(name=f"Person {i}"))
        assert result is True
    assert book.count() == 5


# get_contact

def test_get_contact_common():
    """retrieve the correct contact by valid index"""
    book = AddressBook()
    c = Contact(name="Yuri")
    book.add_contact(c)
    assert book.get_contact(0) == c

def test_get_contact_edge():
    """index 0 on an empty book returns None"""
    book = AddressBook()
    assert book.get_contact(0) is None

def test_get_contact_special():
    """negative index returns None"""
    book = AddressBook()
    book.add_contact(Contact(name="Yuri"))
    assert book.get_contact(-1) is None


# update_contact

def test_update_contact_common():
    """update a contact's email successfully"""
    book = AddressBook()
    book.add_contact(Contact(name="Yuri"))
    result = book.update_contact(0, email="yuri@gmail.com")
    assert result is True
    assert book.get_contact(0).get_email() == "yuri@gmail.com"

def test_update_contact_edge():
    """update on invalid index returns False"""
    book = AddressBook()
    result = book.update_contact(99, name="Ghost")
    assert result is False

def test_update_contact_special():
    """passing '' clears a field to None"""
    book = AddressBook()
    book.add_contact(Contact(name="Yuri", email="yuri@gmail.com"))
    book.update_contact(0, email='')
    assert book.get_contact(0).get_email() is None


# delete_contact

def test_delete_contact_common():
    """delete an existing contact successfully"""
    book = AddressBook()
    book.add_contact(Contact(name="Yuri"))
    result = book.delete_contact(0)
    assert result is True
    assert book.count() == 0

def test_delete_contact_edge():
    """delete on empty book returns False"""
    book = AddressBook()
    assert book.delete_contact(0) is False

def test_delete_contact_special():
    """delete middle contact, remaining contacts shift correctly"""
    book = AddressBook()
    book.add_contact(Contact(name="A"))
    book.add_contact(Contact(name="B"))
    book.add_contact(Contact(name="C"))
    book.delete_contact(1)
    assert book.count() == 2
    assert book.get_contact(0).get_name() == "A"
    assert book.get_contact(1).get_name() == "C"


# merge_contacts

def test_merge_contacts_common():
    """merge two contacts, first contact's fields take priority"""
    book = AddressBook()
    book.add_contact(Contact(name="Yuri", email="yuri@gmail.com"))
    book.add_contact(Contact(name="Yuri B", phone="123-4567"))
    result = book.merge_contacts(0, 1)
    assert result is True
    assert book.count() == 1
    merged = book.get_contact(0)
    assert merged.get_name() == "Yuri"
    assert merged.get_email() == "yuri@gmail.com"
    assert merged.get_phone() == "123-4567"

def test_merge_contacts_edge():
    """merge with same index returns False"""
    book = AddressBook()
    book.add_contact(Contact(name="Yuri"))
    assert book.merge_contacts(0, 0) is False

def test_merge_contacts_special():
    """merge with an invalid index returns False"""
    book = AddressBook()
    book.add_contact(Contact(name="Yuri"))
    assert book.merge_contacts(0, 99) is False
    assert book.count() == 1


# list_contacts

def test_list_contacts_common():
    """list returns all added contacts in order"""
    book = AddressBook()
    c1 = Contact(name="Yuri")
    c2 = Contact(name="Bob")
    book.add_contact(c1)
    book.add_contact(c2)
    contacts = book.list_contacts()
    assert contacts[0] == c1
    assert contacts[1] == c2

def test_list_contacts_edge():
    """list on empty book returns empty list"""
    book = AddressBook()
    assert book.list_contacts() == []

def test_list_contacts_special():
    """modifying the returned list does not affect the book"""
    book = AddressBook()
    book.add_contact(Contact(name="Yuri"))
    contacts = book.list_contacts()
    contacts.clear()
    assert book.count() == 1


# count

def test_count_common():
    """count increases as contacts are added"""
    book = AddressBook()
    assert book.count() == 0
    book.add_contact(Contact(name="Yuri"))
    assert book.count() == 1
    book.add_contact(Contact(name="Bob"))
    assert book.count() == 2

def test_count_edge():
    """count returns 0 for a new empty address book"""
    book = AddressBook()
    assert book.count() == 0

def test_count_special():
    """count after delete reflects the removal"""
    book = AddressBook()
    book.add_contact(Contact(name="Yuri"))
    book.add_contact(Contact(name="Bob"))
    book.delete_contact(0)
    assert book.count() == 1


# ========== TEST RUNNER ==========

def test_all():
    tests = [
        test_contact_init_common,
        test_contact_init_edge,
        test_contact_init_special,
        test_contact_set_get_name_common,
        test_contact_set_get_name_edge,
        test_contact_set_get_name_special,
        test_contact_set_get_email_common,
        test_contact_set_get_email_edge,
        test_contact_set_get_email_special,
        test_contact_set_get_phone_common,
        test_contact_set_get_phone_edge,
        test_contact_set_get_phone_special,
        test_contact_str_common,
        test_contact_str_edge,
        test_contact_str_special,
        test_contact_eq_common,
        test_contact_eq_edge,
        test_contact_eq_special,
        test_add_contact_common,
        test_add_contact_edge,
        test_add_contact_special,
        test_get_contact_common,
        test_get_contact_edge,
        test_get_contact_special,
        test_update_contact_common,
        test_update_contact_edge,
        test_update_contact_special,
        test_delete_contact_common,
        test_delete_contact_edge,
        test_delete_contact_special,
        test_merge_contacts_common,
        test_merge_contacts_edge,
        test_merge_contacts_special,
        test_list_contacts_common,
        test_list_contacts_edge,
        test_list_contacts_special,
        test_count_common,
        test_count_edge,
        test_count_special,
    ]
    for test in tests:
        test()
    print(f"OK: All {len(tests)} tests passed.")
