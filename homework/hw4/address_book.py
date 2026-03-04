# LLM Usage:
# Claude Code (claude-opus-4-6) scaffolded this file for hw4.
# hw2 and hw3 methods are kept as-is. Graph methods added for hw4.

from contact import Contact
from collections import deque


# manages a collection of Contact objects
# all changes to contacts (add, view, update, delete, merge) happen through class methods
# hw3 adds: sort_contacts, search_contacts, and two private merge-sort helpers
# hw4 adds: graph storage (_edges), add_edge, remove_edge, display_adjacency_list, display_third_degree
class AddressBook:

    # constructor, initialize empty list of contacts and empty edge dictionary
    def __init__(self):
        self._contacts = []
        self._edges = {}  # adjacency list: {index: set of neighbor indices}


    # ========== CONTACT CRUD ==========

    # Task: add a new contact to the address book
    # Solution: check for a duplicate first -- if one exists, reject and return False
    #           otherwise append the contact and return True
    def add_contact(self, contact):
        # reject if an identical contact already exists
        if any(c == contact for c in self._contacts):
            return False
        # no duplicate, append and return True
        self._contacts.append(contact)
        return True

    # Task: retrieve a contact by its position in the list
    # Solution: validate the index is in range before accessing, return None if not
    def get_contact(self, index):
        # check index is within valid range
        if 0 <= index < len(self._contacts):
            return self._contacts[index]
        return None

    # Task: remove a contact from the address book by index
    # Solution: validate the index, pop the contact if valid, return False otherwise
    def delete_contact(self, index):
        # check index is within valid range
        if 0 <= index < len(self._contacts):
            self._contacts.pop(index)
            return True
        return False

    # Task: return all contacts so the caller can display or iterate over them
    # Solution: return a copy of the internal list so the caller can't accidentally
    #           modify the address book's data directly
    def list_contacts(self):
        return list(self._contacts)

    # Task: return how many contacts are in the address book
    # Solution: return the length of the internal list
    def count(self):
        return len(self._contacts)


    # ========== FIELD UPDATE ==========

    # Task: update one or more fields in an existing contact
    # Solution: look up the contact by index, then compute what each field would become
    #           after the update. Reject if the result would leave all fields empty,
    #           since a contact must always have at least one field.
    #           passing '' clears a field, omitting an argument leaves it unchanged.
    def update_contact(self, index, name=None, email=None, phone=None):
        # get contact, returns False if invalid
        contact = self.get_contact(index)
        if contact is None:
            return False
        # compute what each field will be after the update
        # keep the existing value if the argument was not passed
        new_name  = (name  if name  != '' else None) if name  is not None else contact.get_name()
        new_email = (email if email != '' else None) if email is not None else contact.get_email()
        new_phone = (phone if phone != '' else None) if phone is not None else contact.get_phone()
        # reject if all fields would end up empty
        if new_name is None and new_email is None and new_phone is None:
            return False
        # apply the updates
        contact.set_name(new_name)
        contact.set_email(new_email)
        contact.set_phone(new_phone)
        return True


    # ========== MERGE ==========

    # Task: combine two contacts into one, keeping the first contact's fields
    #       where both have a value, and filling in gaps from the second contact
    # Solution: validate indices, build merged Contact, use or to prefer first contacts fields,
    #           then remove original contacts and insert new contact at the lower index
    def merge_contacts(self, index1, index2):
        # cant merge with itself
        if index1 == index2:
            return False
        # get both contacts, returns False if either is invalid
        c1 = self.get_contact(index1)
        c2 = self.get_contact(index2)
        if c1 is None or c2 is None:
            return False

        # build new contact, 'or' ensures c1 gets priority over c2
        merged_contact = Contact(
            name=c1.get_name() or c2.get_name(),
            email=c1.get_email() or c2.get_email(),
            phone=c1.get_phone() or c2.get_phone()
        )

        # remove the higher index first so removing it doesn't shift the lower index
        high, low = max(index1, index2), min(index1, index2)
        self._contacts.pop(high)
        self._contacts.pop(low)
        # insert merged contact at low index
        self._contacts.insert(low, merged_contact)
        return True


    # ========== SORTING ==========

    # Task: map a field name string to the lambda that reads that field from a Contact
    # Solution: return the matching lambda from a dict, or None for an invalid field name
    def _get_getter(self, field):
        return {
            'name':  lambda c: c.get_name(),
            'email': lambda c: c.get_email(),
            'phone': lambda c: c.get_phone(),
        }.get(field)

    # Task: sort the address book's contacts by one field in descending order
    # Solution: look up the getter, reject invalid fields, then run recursive merge sort
    #           on a COPY of the contacts list and return the result
    def sort_contacts(self, field):
        # look up the getter; returns None for invalid field names
        getter = self._get_getter(field)
        if getter is None:
            return None
        # sort a copy of the list so the address book itself is not modified
        return self._merge_sort(list(self._contacts), getter)

    # Task: recursively split a list of contacts in half and sort each half
    # Solution: base case handles lists that are already sorted (length 0 or 1),
    #           otherwise split at the midpoint, recurse on both halves,
    #           then merge the two sorted results back into one list
    def _merge_sort(self, contacts, getter):
        # base case: a list of 0 or 1 element is already sorted
        if len(contacts) <= 1:
            return contacts
        # split at the midpoint and recurse on each half
        midpoint = len(contacts) // 2
        left  = self._merge_sort(contacts[:midpoint], getter)
        right = self._merge_sort(contacts[midpoint:], getter)
        # merge the two sorted halves into one sorted result
        return self._merge(left, right, getter)

    # Task: combine two already-sorted lists into one descending sorted list
    # Solution: walk both lists with two pointers, always picking the larger front
    #           element (treat None as '' so missing values sink to the end),
    #           then tack on whatever is left in either half
    def _merge(self, left, right, getter):
        # two pointers, one per half; result collects the merged output
        result, i, j = [], 0, 0
        # compare the front of each half, always take the larger value first (descending)
        # treat None as '' so contacts missing this field sort to the end
        while i < len(left) and j < len(right):
            lv = getter(left[i])  or ''
            rv = getter(right[j]) or ''
            if lv >= rv:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        # one half may still have elements left after the loop — append them
        result.extend(left[i:])
        result.extend(right[j:])
        return result


    # ========== SEARCHING ==========

    # Task: find all contacts whose chosen field exactly matches a target value
    # Solution: validate the field, pick the right getter, walk self._contacts and
    #           collect every contact where getter(contact) == value;
    #           return the collected list (empty list = no match found)
    def search_contacts(self, field, value):
        # look up the getter; returns None for invalid field names
        getter = self._get_getter(field)
        if getter is None:
            return None
        # return every contact whose field value exactly matches the search target
        return [c for c in self._contacts if getter(c) == value]


    # ========== GRAPH (HW4) ==========

    # Task: add an undirected edge between two contacts by index
    # Solution: validate both indices, ensure they're different, then add each index
    #           to the other's neighbor set in the edges dictionary
    def add_edge(self, index1, index2):
        # can't connect a contact to itself
        if index1 == index2:
            return False
        # both indices must point to existing contacts
        if self.get_contact(index1) is None or self.get_contact(index2) is None:
            return False
        # initialize neighbor sets if they don't exist yet
        self._edges.setdefault(index1, set())
        self._edges.setdefault(index2, set())
        # add undirected edge (both directions)
        self._edges[index1].add(index2)
        self._edges[index2].add(index1)
        return True

    # Task: remove an undirected edge between two contacts by index
    # Solution: check the edge actually exists, then remove each index from the other's set
    def remove_edge(self, index1, index2):
        # both must have edges recorded
        if index1 not in self._edges or index2 not in self._edges:
            return False
        # check the edge actually exists
        if index2 not in self._edges[index1]:
            return False
        # remove both directions of the undirected edge
        self._edges[index1].discard(index2)
        self._edges[index2].discard(index1)
        return True

    # Task: print the full adjacency list showing each contact and its 1st degree connections
    # Solution: loop through all contacts by index, look up their neighbors in _edges,
    #           print the degree count and sorted neighbor list in the required format
    def display_adjacency_list(self):
        print("--- Social Address Book Adjacency List ---")
        for i in range(len(self._contacts)):
            neighbors = sorted(self._edges.get(i, set()))
            degree = len(neighbors)
            neighbor_str = ", ".join(str(n) for n in neighbors)
            print(f"Node {i:>2} (Degree {degree}): connected to -> {neighbor_str}")

    # Task: display all connections up to the 3rd degree for a given contact using BFS
    # Solution: run BFS from the start node, tracking depth with a queue of (node, depth) pairs;
    #           collect neighbors into degree buckets (1st, 2nd, 3rd) and skip already-visited
    #           nodes to avoid cycles; sort and print each degree's list
    def display_third_degree(self, index):
        # validate the index
        if self.get_contact(index) is None:
            print(f"Node {index} not found.")
            return

        # BFS setup: visited set and queue of (node, depth) pairs
        visited = {index}
        queue = deque([(index, 0)])
        degrees = {1: [], 2: [], 3: []}

        # BFS traversal, stop exploring beyond depth 3
        while queue:
            node, depth = queue.popleft()
            if depth >= 3:
                continue
            # visit all neighbors of the current node
            for neighbor in sorted(self._edges.get(node, set())):
                if neighbor not in visited:
                    visited.add(neighbor)
                    degrees[depth + 1].append(neighbor)
                    queue.append((neighbor, depth + 1))

        # print the results by degree, sorted for clean output
        print(f"--- 3rd Degree Connections for Node {index} ---")
        print(f"1st Degree   : {sorted(degrees[1])}")
        print(f"2nd Degree   : {sorted(degrees[2])}")
        print(f"3rd Degree   : {sorted(degrees[3])}")
