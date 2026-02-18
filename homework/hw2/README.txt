Yuri Chentsov
Homework 2: Social Address Book
Tech.UB.27.002 Spring 2026
===============================

PROGRAM DESCRIPTION
-------------------
A terminal-based Address Book program built with Object Oriented Programming.
Users can add, view, update, and delete Contacts, with duplicate prevention
and the ability to merge two Contacts into one.

FILE STRUCTURE
--------------
main.py         Entry point. Main menu, interactive UI, and demo.
contact.py      Contact class. Manages a single contact's name, email, and phone.
address_book.py AddressBook class. Manages a collection of Contact objects.
test.py         All unit tests (3 per method: common, edge, and special cases).
README.txt      This file.

CLASSES
-------
Contact (contact.py)
  - Attributes: name, email, phone (at least one required at creation)
  - Methods: get_name, set_name, get_email, set_email, get_phone, set_phone
  - Dunder methods: __str__ (display), __eq__ (duplicate detection)

AddressBook (address_book.py)
  - Attributes: contacts (internal list of Contact objects)
  - Methods: add_contact, get_contact, update_contact, delete_contact,
             merge_contacts, list_contacts, count

LLM USAGE
---------
Used Claude code to help with dunder methods, duplicate detection and merge logic, test cases, and main.py.