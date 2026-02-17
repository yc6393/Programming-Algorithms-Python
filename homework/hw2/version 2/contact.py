"""
Contact class for the Social Address Book program.
Represents a single contact with name, email, and phone fields.
"""

class Contact:
    """Represents a contact with name, email, and phone information."""
    
    def __init__(self, name="", email="", phone=""):
        """
        Initialize a Contact object.
        
        Args:
            name (str): Contact's name
            email (str): Contact's email address
            phone (str): Contact's phone number
        """
        self._name = name
        self._email = email
        self._phone = phone
    
    # Getters and setters with encapsulation
    @property
    def name(self):
        """Get the contact's name."""
        return self._name
    
    @name.setter
    def name(self, value):
        """Set the contact's name."""
        self._name = value
    
    @property
    def email(self):
        """Get the contact's email."""
        return self._email
    
    @email.setter
    def email(self, value):
        """Set the contact's email."""
        self._email = value
    
    @property
    def phone(self):
        """Get the contact's phone number."""
        return self._phone
    
    @phone.setter
    def phone(self, value):
        """Set the contact's phone number."""
        self._phone = value
    
    def update(self, name=None, email=None, phone=None):
        """
        Update contact fields.
        
        Args:
            name (str, optional): New name
            email (str, optional): New email
            phone (str, optional): New phone number
        """
        if name is not None:
            self._name = name
        if email is not None:
            self._email = email
        if phone is not None:
            self._phone = phone
    
    # Dunder methods for string representation and comparison
    def __str__(self):
        """String representation for users."""
        parts = []
        if self._name:
            parts.append(f"Name: {self._name}")
        if self._email:
            parts.append(f"Email: {self._email}")
        if self._phone:
            parts.append(f"Phone: {self._phone}")
        
        if parts:
            return " | ".join(parts)
        return "Empty Contact"
    
    def __repr__(self):
        """Representation for developers."""
        return f"Contact(name='{self._name}', email='{self._email}', phone='{self._phone}')"
    
    def __eq__(self, other):
        """
        Compare two contacts for equality.
        Contacts are considered equal if they share any identifying information.
        """
        if not isinstance(other, Contact):
            return False
        
        # Check if they share any common identifying information
        if self._name and other._name and self._name.lower() == other._name.lower():
            return True
        if self._email and other._email and self._email.lower() == other._email.lower():
            return True
        if self._phone and other._phone and self._phone == other._phone:
            return True
        
        return False
    
    def __ne__(self, other):
        """Inequality comparison."""
        return not self.__eq__(other)
    
    def is_empty(self):
        """Check if contact has no data."""
        return not (self._name or self._email or self._phone)