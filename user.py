class User:
    login_attempts = 0
    def __init__(self, first_name, last_name, age, email):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
    def describe_user(self):
        return f'Ім\'я {self.first_name} {self.last_name}.'
    def greeting_user(self):
        return f'Вітаю, {self.first_name} {self.last_name}'
    def increment_login_attempts(self):
        User.login_attempts += 1
    def reset_login_attempts(self):
        User.login_attempts = 0
user1 = User('Вікторія', 'Мельник', '17', 'v.melnik@gmail.com')
user2 = User('Олександр', 'Максимюк', '21', 'alex.maks1@gmail.com')
user3 = User('Ксенія', 'Клем', '30', 'ksenia_k3@gmail.com')
print(user1.describe_user())
print(user1.greeting_user())
print(user2.describe_user())
print(user2.greeting_user())
print(user3.describe_user())
print(user3.greeting_user())
user1.increment_login_attempts()
print(User.login_attempts)
user2.increment_login_attempts()
user3.increment_login_attempts()
print(User.login_attempts)
user1.reset_login_attempts()
print(User.login_attempts)