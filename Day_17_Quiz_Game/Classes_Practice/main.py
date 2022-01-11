class User:
    def __init__(self, user_id, user_name):
        self.id = user_id
        self.username = user_name
        self.followers = 0
        self.following = 0
        print("New user created")

    def follow(self, user):
        user.followers += 1
        self.following += 1

    pass


user_1 = User("001", "Felipe")
#print(user_1.username)
user_2 = User("002", "Jorge")
#print(user_2.username)

user_1.follow(user_2)
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)