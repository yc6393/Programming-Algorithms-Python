Social Address Book — Homework 2
Tech.UB.27.002 Spring 2026
=====================================

PROGRAM DESCRIPTION
-------------------
A terminal-based Address Book program built with Object Oriented Programming.
Users can add, view, update, and delete Contacts, with duplicate prevention
and the ability to merge two Contacts into one.

HOW TO RUN
----------
From the hw2/ directory, run:
    python main.py

You will be prompted to choose one of three modes:
    1. Run unit tests  — runs all automated tests and reports pass/fail
    2. Run demo        — shows an automated walkthrough of all features
    3. Use Address Book — interactive terminal program

FILE STRUCTURE
--------------
main.py         Entry point. Contains the main menu, interactive UI, and demo.
contact.py      Contact class. Manages a single contact's name, email, and phone.
address_book.py AddressBook class. Manages a collection of Contact objects.
test.py         All unit tests (3 per method: common, edge, and special cases).
README.txt      This file.

CLASSES
-------
Contact (contact.py)
  - Fields: name, email, phone (at least one required)
  - Methods: get/set for each field
  - Dunder methods: __str__, __eq__, __repr__

AddressBook (address_book.py)
  - Methods: add_contact, get_contact, update_contact, delete_contact,
             merge_contacts, list_contacts, count

DESIGN PRINCIPLES
-----------------
KISS  — Each method does one simple, clear thing.
DRY   — Shared logic (e.g., pick_contact, prompt_fields) is factored into helpers.
SRP   — Contact only manages a single contact's data; AddressBook only manages
        the collection; main.py only handles user interaction.

LLM USAGE CITATION
------------------
Claude (claude-sonnet-4-6) was used to assist with the design and implementation
of this program, including: class structure, getter/setter patterns, dunder method
implementation, test case design, and overall program organization. The student
directed the design decisions and reviewed all generated code.
