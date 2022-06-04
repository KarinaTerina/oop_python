from user import User
class Admin(User):
    def __init__(self, first_name, last_name, age, email):
        super().__init__(first_name, last_name, age, email)
        self.priv = Privileges
class Privileges(Admin):
    def __init__(self,privileges):
        self.privileges = privileges
    def show_privileges(self):
        return f'Priveleges - {self.privileges}.'
admin = Privileges('«Allowed to add message», «Allowed to delete users», «Allowed to ban users»')
print(admin.show_privileges())