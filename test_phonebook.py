import unittest
from phonebook import PhoneBook

class PhoneBookTest(unittest.TestCase):
    def test_lookup_by_name(self):
        phonebook = PhoneBook()
        phonebook.add("Bob", "12345")
        
        number = phonebook.lookup("Bob")
        
        self.assertEqual(number, "12345")
        
    def test_missing_name(self):
        phonebook = PhoneBook()
        phonebook.add("Bob", "12345")
        
        number = phonebook.lookup("Alice")
        
        self.assertIsNone(number)