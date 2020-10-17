class user:

    def __init__(self, f_name, l_name, sex, age, login_attempts):
        self.f_name = f_name
        self.l_name = l_name
        self.sex = sex
        self.age = age
        self.login_attempts = login_attempts

    def describe_user(self):
        print(f"The customer named {self.f_name} {self.l_name} is a {self.sex} and is {self.age} years old has {self.login_attempts} login attempts")

    def greet_user(self):
        print(f"Greetings {self.f_name} {self.l_name}")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def resert_login_attempts(self):
        self.login_attempts = 0

