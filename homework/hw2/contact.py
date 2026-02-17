# LLM Usage:
# Claude Code to help with dunder methods, also to make sure everything looked fine


# represent a single person in address book, up to three fields:
#   - name, email, phone number
# getter/setter methods, as well as __str__ and __eq__ for display and comparison
class Contact:

    # constructor, default values of None
    def __init__(self, name=None, email=None, phone=None):
        
        # require at least one field
        if name is None and email is None and phone is None:
            raise ValueError("A contact must have at least one field (name, email, or phone).")
        
        # store each field as a private attribute
        self._name = name
        self._email = email
        self._phone = phone


    # ========== GETTER / SETTER ==========

    # name GETTER/SETTER
    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    # email GETTER/SETTER
    def get_email(self):
        return self._email

    def set_email(self, email):
        self._email = email

    # phone GETTER/SETTER
    def get_phone(self):
        return self._phone

    def set_phone(self, phone):
        self._phone = phone


    # ========== DUNDERS ==========
  
    # Task: produce readable string showing contacts non-empty fields
    # Solution: build a list of "label: value" strings for available fields, then join with "|"
    #           for separation
    def __str__(self):
        # start with an empty list and add only the fields that have a value
        parts = []
        if self._name:
            parts.append(f"Name: {self._name}")
        if self._email:
            parts.append(f"Email: {self._email}")
        if self._phone:
            parts.append(f"Phone: {self._phone}")
        # join all present fields with a separator
        return " | ".join(parts)


    # Task: check if two contacts are identical (duplicate)
    # Solution: return True <=> object is contact, AND all three fields match
    def __eq__(self, other):
        # ensure the other object is a contact type
        if not isinstance(other, Contact):
            return False
        # all three fields must match for the contacts to be equal
        return (self._name == other._name and
                self._email == other._email and
                self._phone == other._phone)

