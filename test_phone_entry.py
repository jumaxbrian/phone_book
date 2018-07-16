import unittest
from phone_entry import PhoneEntry

class TestPhoneEntry(unittest.TestCase):
    def test_validate_number(self):
        self.assertTrue(PhoneEntry.validateNumber('12345678'))
        self.assertFalse(PhoneEntry.validateNumber('1234567'))
        self.assertFalse(PhoneEntry.validateNumber('1234567a'))


if __name__ == "__main__":
    unittest.main()
