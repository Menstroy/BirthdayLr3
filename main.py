import json
import argparse
from datetime import datetime, date, timedelta


class BirthdayReminder:
    def __init__(self):
        self.friends = []

    def add_friend(self, name, birthday):
        try:
            datetime.strptime(birthday, "%Y-%m-%d")
        except ValueError:
            raise ValueError("Дата должна быть в формате YYYY-MM-DD")
        self.friends.append({"name": name, "birthday": birthday})

    def get_today_birthdays(self):
        today = date.today().strftime("%m-%d")
        return [f for f in self.friends if f["birthday"][5:] == today]

    def get_upcoming_birthdays(self, days=30):
        today = date.today()
        upcoming = []

        for friend in self.friends:
            bday = datetime.strptime(friend["birthday"], "%Y-%m-%d").date()
            bday_this_year = bday.replace(year=today.year)

            if bday_this_year < today:
                bday_this_year = bday_this_year.replace(year=today.year + 1)

            delta = (bday_this_year - today).days
            if 0 <= delta <= days:
                upcoming.append({
                    "name": friend["name"],
                    "date": bday_this_year.strftime("%Y-%m-%d"),
                    "days_until": delta
                })

        return sorted(upcoming, key=lambda x: x["days_until"])

    def save_to_file(self, filename):
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(self.friends, f, ensure_ascii=False, indent=2)

    def load_from_file(self, filename):
        with open(filename, encoding='utf-8') as f:
            self.friends = json.load(f)


def main():
    br = BirthdayReminder()
    parser = argparse.ArgumentParser()

    # Автозагрузка по умолчанию
    if os.path.exists("birthdays.json"):
        br.load_from_file("birthdays.json")

    parser.add_argument('--add', nargs=2, metavar=('NAME', 'DATE'))
    parser.add_argument('--today', action='store_true')
    parser.add_argument('--upcoming', type=int, default=30)

    args = parser.parse_args()

    if args.add:
        name, bday = args.add
        try:
            br.add_friend(name, bday)
            br.save_to_file("birthdays.json")  # Автосохранение
            print(f"Добавлен: {name}")
        except ValueError as e:
            print(f"Ошибка: {e}")

    if args.today:
        today = br.get_today_birthdays()
        if today:
            print("Сегодня день рождения у:")
            for friend in today:
                print(f" - {friend['name']}")
        else:
            print("Сегодня дней рождения нет")

    if args.upcoming:
        upcoming = br.get_upcoming_birthdays(args.upcoming)
        if upcoming:
            print(f"Ближайшие дни рождения ({args.upcoming} дней):")
            for friend in upcoming:
                print(f" - {friend['name']} ({friend['date'][5:]}, через {friend['days_until']} дней)")
        else:
            print(f"Нет дней рождения в ближайшие {args.upcoming} дней")


if __name__ == '__main__':
    import os

    main()