import unittest
from main import BirthdayReminder

class TestBirthdayReminder(unittest.TestCase):
    def test_birth(self):
        birth = BirthdayReminder()
        self.assertIsNotNone(birth)

if __name__ == '__main__':
    unittest.main()