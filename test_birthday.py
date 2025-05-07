# test_birthday.py
import unittest
import tempfile
import os
from main import BirthdayReminder
from datetime import date, timedelta
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


    def test_upcoming_birthdays(self):
        br = BirthdayReminder()
        today = date.today()
        future_date = (today + timedelta(days=5)).strftime("%Y-%m-%d")
        br.add_friend("Ближайший", future_date)
        upcoming = br.get_upcoming_birthdays(7)
        self.assertEqual(len(upcoming), 1)

    def test_save_to_file(self):
        br = BirthdayReminder()
        br.add_friend("Тест", "2000-01-01")

        with tempfile.NamedTemporaryFile(delete=False) as tmp:
            filename = tmp.name

        try:
            br.save_to_file(filename)
            self.assertTrue(os.path.exists(filename))
            self.assertGreater(os.path.getsize(filename), 0)
        finally:
            os.unlink(filename)


    def test_load_from_file(self):
        br = BirthdayReminder()

        # Создаем тестовый файл с данными
        with tempfile.NamedTemporaryFile(mode='w', delete=False) as tmp:
            tmp.write('[{"name": "Тест", "birthday": "2000-01-01"}]')
            filename = tmp.name

        try:
            br.load_from_file(filename)
            self.assertEqual(len(br.friends), 1)
            self.assertEqual(br.friends[0]["name"], "Тест")
        finally:
            os.unlink(filename)
if __name__ == '__main__':
    unittest.main()
