# test_birthday.py
import unittest
from main import BirthdayReminder
from datetime import date
class TestBirthdayReminder(unittest.TestCase):
    def test_add_friend(self):
        br = BirthdayReminder()
        br.add_friend("Иван", "1990-05-15")
        self.assertEqual(len(br.friends), 1)

    def test_today_birthdays(self):
        br = BirthdayReminder()
        test_date = date.today().strftime("%Y-%m-%d")
        br.add_friend("Сегодняшний", test_date)

        birthdays = br.get_today_birthdays()
        self.assertEqual(len(birthdays), 1)
if __name__ == '__main__':
    unittest.main()
