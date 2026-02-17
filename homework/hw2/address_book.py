# LLM Usage:
# Claude Code to help with duplicate detection and merge logic

from contact import Contact


# manages a collection of Contact objects
# all changes to contacts (add, view, update, delete, merge) happen through class methods
class AddressBook:

    # constructor, initialize empty list of contacts
    def __init__(self):
        self._contacts = []


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
    # Solution: look up the contact by index, then use appropriate setter for each argument.
    #           passing '' should clear a field, and omitting an argument leaves that field unchanged
    def update_contact(self, index, name=None, email=None, phone=None):
        # get contact, returns False if index invalid
        contact = self.get_contact(index)
        if contact is None:
            return False
        # only update fields that were passed
        if name is not None:
            # if '', set as None, else set as name entered
            contact.set_name(name if name != '' else None)
        if email is not None:
            contact.set_email(email if email != '' else None)
        if phone is not None:
            contact.set_phone(phone if phone != '' else None)
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
