class User:
    def __init__(self, username, email, password):
        self.username = username
        self._email = email
        self.password = password

    def sayHiToUser(self, user):
        print(
            f"Sending message to {user.username}: Hi {user.username}, it's {self.username} ;)"
        )
    def get_email(self):
        return self._email
    def clean_email(self):
        return self._email.lower().strip()

user1 = User("dantheman", "Dan@gmail.com ", "123")
user2 = User("batman", "bat@gmail.com", "abc")
user1.sayHiToUser(user2)

print(user1.email)

user1.email = "danoutlook.com"  # PROBLEM: we can set email to anything!

print(user1.email)

print(user1._email)#

print(user1.clean_email())

#52:46