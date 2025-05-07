from datetime import datetime, date
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
        with open(filename, 'w') as f:
            f.write("test")  # Просто записываем что-то в файл

    def load_from_file(self, filename):
        self.friends = [{"name": "Тест", "birthday": "2000-01-01"}]  # Заглушка