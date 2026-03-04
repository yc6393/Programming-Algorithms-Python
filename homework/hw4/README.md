Yuri Chentsov
Homework 4: Social Address Book
Tech.UB.27.002 Spring 2026
===============================

PROGRAM DESCRIPTION
-------------------
Extends the Homework 3 Address Book with social graph functionality.
The AddressBook class gains a new dictionary attribute (_edges) to store
undirected edges between contacts, along with methods to add and remove
edges, display the full adjacency list (1st degree connections), and
display an individual contact's network up to the 3rd degree using
Breadth First Search (BFS).

HOW TO RUN
----------
Demo (20 contacts): python social_demo.py

FILE STRUCTURE
--------------
contact.py      Contact class. Unchanged from hw2/hw3.
address_book.py AddressBook class. Extended with graph methods.
social_demo.py  Demonstration of graph capabilities on a 20-contact address book.
README.md       This file.

NEW METHODS IN AddressBook (address_book.py)
--------------------------------------------
add_edge(index1, index2)
  - Adds an undirected edge between two contacts by index.
  - Both indices must be valid and different.
  - Stores edges in the _edges dictionary (adjacency list of sets).

remove_edge(index1, index2)
  - Removes an undirected edge between two contacts.
  - Returns False if the edge does not exist.

display_adjacency_list()
  - Prints each contact and its 1st degree neighbors.
  - Format: Node X (Degree Y): connected to -> a, b, c

display_third_degree(index)
  - Uses BFS to find all connections up to 3rd degree for a contact.
  - Prints results grouped by degree (1st, 2nd, 3rd).

LLM USAGE
---------
Used Claude Code (claude-opus-4-6) to scaffold file structure, generate
the graph methods, and build the 20-contact demo. All method logic was
written and reviewed by the student with Claude providing step-by-step
guidance in chat. Claude also made this README for me!
