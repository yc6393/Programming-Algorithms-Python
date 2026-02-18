"""
AddressBook class for the Social Address Book program.
Manages a collection of Contact objects.
"""

from contact import Contact

class AddressBook:
    """Manages a collection of contacts."""
    
    def __init__(self):
        """Initialize an empty address book."""
        self._contacts = []
    
    def add_contact(self, contact):
        """
        Add a contact to the address book.
        
        Args:
            contact (Contact): Contact to add
            
        Returns:
            bool: True if added successfully, False if duplicate or invalid
        """
        # Check if contact is valid (has at least one field)
        if contact.is_empty():
            return False
        
        # Check for duplicates
        if self._is_duplicate(contact):
            return False
        
        self._contacts.append(contact)
        return True
    
    def _is_duplicate(self, contact):
        """
        Check if a contact already exists in the address book.
        
        Args:
            contact (Contact): Contact to check
            
        Returns:
            bool: True if duplicate exists
        """
        for existing in self._contacts:
            if existing == contact:
                return True
        return False
    
    def get_all_contacts(self):
        """
        Get all contacts in the address book.
        
        Returns:
            list: List of all contacts
        """
        return self._contacts.copy()
    
    def find_contact(self, search_term):
        """
        Find contacts matching a search term.
        
        Args:
            search_term (str): Term to search for in name, email, or phone
            
        Returns:
            list: List of matching contacts
        """
        matches = []
        search_term_lower = search_term.lower()
        
        for contact in self._contacts:
            if (search_term_lower in contact.name.lower() or
                search_term_lower in contact.email.lower() or
                search_term in contact.phone):  # Phone numbers are exact match
                matches.append(contact)
        
        return matches
    
    def delete_contact(self, contact):
        """
        Delete a contact from the address book.
        
        Args:
            contact (Contact): Contact to delete
            
        Returns:
            bool: True if deleted successfully
        """
        if contact in self._contacts:
            self._contacts.remove(contact)
            return True
        return False
    
    def update_contact(self, old_contact, name=None, email=None, phone=None):
        """
        Update a contact's information.
        
        Args:
            old_contact (Contact): Contact to update
            name (str, optional): New name
            email (str, optional): New email
            phone (str, optional): New phone
            
        Returns:
            bool: True if updated successfully
        """
        if old_contact not in self._contacts:
            return False
        
        # Create updated version to check for duplicates
        updated = Contact(
            name if name is not None else old_contact.name,
            email if email is not None else old_contact.email,
            phone if phone is not None else old_contact.phone
        )
        
        # Check if updated version would create a duplicate
        # (excluding the current contact)
        for contact in self._contacts:
            if contact != old_contact and contact == updated:
                return False
        
        # Update the original contact
        old_contact.update(name, email, phone)
        return True
    
    def merge_contacts(self, contact1, contact2):
        """
        Merge two contacts into one.
        
        Args:
            contact1 (Contact): First contact to merge
            contact2 (Contact): Second contact to merge
            
        Returns:
            Contact or None: Merged contact if successful, None otherwise
        """
        if contact1 not in self._contacts or contact2 not in self._contacts:
            return None
        
        if contact1 == contact2:
            return contact1
        
        # Create merged contact
        merged = Contact(
            name=contact1.name or contact2.name,
            email=contact1.email or contact2.email,
            phone=contact1.phone or contact2.phone
        )
        
        # Check if merged contact would be a duplicate
        for contact in self._contacts:
            if contact != contact1 and contact != contact2 and contact == merged:
                return None
        
        # Remove both original contacts and add merged
        self._contacts.remove(contact1)
        self._contacts.remove(contact2)
        self._contacts.append(merged)
        
        return merged
    
    def size(self):
        """
        Get the number of contacts in the address book.
        
        Returns:
            int: Number of contacts
        """
        return len(self._contacts)