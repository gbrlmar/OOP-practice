from user_class import user 

class Priviledges:
    
    def __init__(self, priviledges = ['can add porst', 'can delete post', 'can ban user']):
        self.priviledges = priviledges

    def show_priviledges(self):
        print(f'The priviledges of the admin are {self.priviledges}')

class Admin(user):

    def __init__(self, f_name, l_name, sex, age, login_attempts):
        super().__init__(f_name, l_name, sex, age, login_attempts)
        self.priviledges = Priviledges()
