from datetime import date
class BirthdayReminder:
    def __init__(self):
        self.friends = []

    def add_friend(self, name, birthday):
        self.friends.append({"name": name, "birthday": birthday})

    def get_today_birthdays(self):
        today = date.today().strftime("%m-%d")
        return [f for f in self.friends if f["birthday"][5:] == today]

    def get_upcoming_birthdays(self, days=30):
        return self.friends  # Заглушка
