"""
Unit tests for the Social Address Book program.
Tests Contact and AddressBook classes.
"""

import unittest
from contact import Contact
from address_book import AddressBook

class TestContact(unittest.TestCase):
    """Test cases for Contact class."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.contact1 = Contact("John Doe", "john@email.com", "123-456-7890")
        self.contact2 = Contact("Jane Smith", "jane@email.com", "098-765-4321")
        self.empty_contact = Contact()
    
    # Common case tests
    def test_contact_creation_common(self):
        """Test creating a contact with all fields."""
        self.assertEqual(self.contact1.name, "John Doe")
        self.assertEqual(self.contact1.email, "john@email.com")
        self.assertEqual(self.contact1.phone, "123-456-7890")
    
    def test_contact_update_common(self):
        """Test updating contact fields."""
        self.contact1.update(name="John Updated", email="john.updated@email.com")
        self.assertEqual(self.contact1.name, "John Updated")
        self.assertEqual(self.contact1.email, "john.updated@email.com")
        self.assertEqual(self.contact1.phone, "123-456-7890")
    
    def test_contact_equality_common(self):
        """Test contact equality with matching name."""
        contact_duplicate = Contact("John Doe", "different@email.com", "999-999-9999")
        self.assertEqual(self.contact1, contact_duplicate)
    
    # Edge case tests
    def test_contact_creation_edge(self):
        """Test creating contact with minimal fields."""
        minimal = Contact(name="Minimal")
        self.assertEqual(minimal.name, "Minimal")
        self.assertEqual(minimal.email, "")
        self.assertEqual(minimal.phone, "")
        self.assertFalse(minimal.is_empty())
    
    def test_is_empty_edge(self):
        """Test is_empty method with partially filled contact."""
        contact = Contact(name="Test")
        self.assertFalse(contact.is_empty())
        
        contact = Contact(email="test@email.com")
        self.assertFalse(contact.is_empty())
    
    def test_equality_edge(self):
        """Test equality with different matching fields."""
        # Match by email
        contact_email = Contact("Different Name", "john@email.com", "999-999-9999")
        self.assertEqual(self.contact1, contact_email)
        
        # Match by phone
        contact_phone = Contact("Different Name", "different@email.com", "123-456-7890")
        self.assertEqual(self.contact1, contact_phone)
    
    # Special case tests
    def test_empty_contact_special(self):
        """Test empty contact behavior."""
        self.assertTrue(self.empty_contact.is_empty())
        self.assertEqual(str(self.empty_contact), "Empty Contact")
    
    def test_equality_special(self):
        """Test equality with non-Contact objects."""
        self.assertNotEqual(self.contact1, "Not a contact")
        self.assertNotEqual(self.contact1, None)
    
    def test_string_representation_special(self):
        """Test string representation with missing fields."""
        contact = Contact(name="Only Name")
        self.assertIn("Name: Only Name", str(contact))
        
        contact = Contact(email="only@email.com")
        self.assertIn("Email: only@email.com", str(contact))

class TestAddressBook(unittest.TestCase):
    """Test cases for AddressBook class."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.book = AddressBook()
        self.contact1 = Contact("John Doe", "john@email.com", "123-456-7890")
        self.contact2 = Contact("Jane Smith", "jane@email.com", "098-765-4321")
        self.contact3 = Contact("Bob Johnson", "bob@email.com", "555-555-5555")
    
    # Common case tests
    def test_add_contact_common(self):
        """Test adding a contact to address book."""
        result = self.book.add_contact(self.contact1)
        self.assertTrue(result)
        self.assertEqual(self.book.size(), 1)
    
    def test_find_contact_common(self):
        """Test finding contacts by search term."""
        self.book.add_contact(self.contact1)
        self.book.add_contact(self.contact2)
        
        matches = self.book.find_contact("john")
        self.assertEqual(len(matches), 1)
        self.assertEqual(matches[0], self.contact1)
    
    def test_delete_contact_common(self):
        """Test deleting a contact."""
        self.book.add_contact(self.contact1)
        result = self.book.delete_contact(self.contact1)
        self.assertTrue(result)
        self.assertEqual(self.book.size(), 0)
    
    # Edge case tests
    def test_add_duplicate_edge(self):
        """Test preventing duplicate contacts."""
        self.book.add_contact(self.contact1)
        
        # Try to add duplicate
        duplicate = Contact("John Doe", "different@email.com", "999-999-9999")
        result = self.book.add_contact(duplicate)
        self.assertFalse(result)
        self.assertEqual(self.book.size(), 1)
    
    def test_update_contact_edge(self):
        """Test updating contact without creating duplicate."""
        self.book.add_contact(self.contact1)
        self.book.add_contact(self.contact2)
        
        # Try to update contact1 to match contact2
        result = self.book.update_contact(self.contact1, 
                                          name=self.contact2.name,
                                          email=self.contact2.email)
        self.assertFalse(result)
    
    def test_merge_contacts_edge(self):
        """Test merging two contacts."""
        self.book.add_contact(self.contact1)
        self.book.add_contact(self.contact2)
        
        merged = self.book.merge_contacts(self.contact1, self.contact2)
        self.assertIsNotNone(merged)
        self.assertEqual(self.book.size(), 1)
        self.assertEqual(merged.name, "John Doe")  # First contact's name kept
        self.assertEqual(merged.email, "john@email.com")  # First contact's email kept
    
    # Special case tests
    def test_add_empty_contact_special(self):
        """Test adding empty contact."""
        empty = Contact()
        result = self.book.add_contact(empty)
        self.assertFalse(result)
        self.assertEqual(self.book.size(), 0)
    
    def test_merge_same_contact_special(self):
        """Test merging a contact with itself."""
        self.book.add_contact(self.contact1)
        
        merged = self.book.merge_contacts(self.contact1, self.contact1)
        self.assertEqual(merged, self.contact1)
        self.assertEqual(self.book.size(), 1)
    
    def test_find_nonexistent_special(self):
        """Test finding non-existent contact."""
        self.book.add_contact(self.contact1)
        matches = self.book.find_contact("nonexistent")
        self.assertEqual(len(matches), 0)
    
    def test_delete_nonexistent_special(self):
        """Test deleting non-existent contact."""
        result = self.book.delete_contact(self.contact1)
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()