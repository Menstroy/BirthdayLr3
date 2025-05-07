# test_birthday.py
import unittest
from main import BirthdayReminder

class TestBirthdayReminder(unittest.TestCase):
    def test_add_friend(self):
        br = BirthdayReminder()
        br.add_friend("Иван", "1990-05-15")
        self.assertEqual(len(br.friends), 1)

if __name__ == '__main__':
    unittest.main()