Yuri Chentsov
Homework 3: Social Address Book
Tech.UB.27.002 Spring 2026
===============================

PROGRAM DESCRIPTION
-------------------
Extends the Homework 2 Address Book with sorting and searching functionality.
The AddressBook class gains two new public methods: sort_contacts, which sorts
all contacts by a chosen field (name, email, or phone) in descending order using
a recursive merge sort algorithm, and search_contacts, which returns all contacts
whose chosen field exactly matches a given value.

HOW TO RUN
----------
Unit tests:          python algo_test.py
Demo (10+ contacts): python algo_demo.py

FILE STRUCTURE
--------------
contact.py      Contact class. Unchanged from hw2.
address_book.py AddressBook class. Extended with sort and search methods.
algo_test.py    Unit tests for the two new methods (3 per method: common, edge, special).
algo_demo.py    Demonstration of sort and search on a 12-contact address book.
README.md       This file.

NEW METHODS IN AddressBook (address_book.py)
--------------------------------------------
_get_getter(field)
  - Private helper. Maps 'name', 'email', or 'phone' to its getter lambda.
  - Returns None for any other field name (used for validation).

sort_contacts(field)
  - Sorts contacts by the given field in descending order.
  - Returns a sorted list; does not modify the address book itself.
  - Uses recursive merge sort (_merge_sort / _merge).

_merge_sort(contacts, getter)
  - Private. Recursively splits the list in half and sorts each half.

_merge(left, right, getter)
  - Private. Merges two sorted halves into one descending sorted list.
  - Treats None field values as '' so contacts missing the field sort to the end.

search_contacts(field, value)
  - Returns a list of all contacts whose field exactly matches value.
  - Returns an empty list when no match is found.

LLM USAGE
---------
Used Claude Code (claude-sonnet-4-6) to scaffold file structure, check code for
bugs, and help fix issues during development. All method logic was written and
reviewed by the student with Claude providing step-by-step guidance in chat.
Claude also made this README for me!
