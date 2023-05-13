class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.fucks_given = 0
    def give_a_fuck(self):
        self.fucks_given += 1
    def lose_a_fuck(self):
        self.fucks_given -= 1


user_1 = User("001", "nico")
user_2 = User("002", "zak")

user_1.give_a_fuck()
print(user_1.fucks_given)