import unittest
from phone_book import PhoneBook

class TestPhoneBook(unittest.TestCase):
    def test_validate_entry(self):
        self.assertTrue(PhoneBook.validateEntry('brian 12345678'))
        self.assertFalse(PhoneBook.validateEntry('klaus4 1234567'))
        self.assertFalse(PhoneBook.validateEntry('thomas 1234567a'))
        self.assertFalse(PhoneBook.validateEntry('thomas4 1234567a'))

if __name__ == "__main__":
    unittest.main()