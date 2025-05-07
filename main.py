class BirthdayReminder:
    def __init__(self):
        self.friends = []

    def add_friend(self, name, birthday):
        self.friends.append({"name": name, "birthday": birthday})
