class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name 
        self.cuisine_type = cuisine_type
        self.number_served = 0 

    def describe_restaurant(self):
        print(f"The restaurant {self.restaurant_name} with cuisine type {self.cuisine_type}.")

    def open_restaurant(self):
        print(f"The restaurant {self.restaurant_name} is open.")

    def set_number_served(self, number):
        self.number_served = number

    def increment_number_served(self, number):
        self.number_served += number

    def print_restaurant(self):
        print(f"{self.number_served}")
        
class IceCreamStand(Restaurant):
    
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavours = ['vanilla', 'chocolate', 'asorte']

    def describe_flavours(self):
        print(f'The icecream stand is with {self.flavours} and i like it, yum!')

class user:

    def __init__(self, first_name, last_name, sex, age, login_attempts):
        self.first_name = first_name
        self.last_name = last_name
        self.sex = sex
        self.age = age
        self.login_attempts = login_attempts

    def describe_user(self):
        print(f"The customer is named {self.first_name} {self.last_name} {self.sex} age {self.age}.and has a number of {self.login_attempts} login attempts.")

    def greet_user(self):
        print(f"Greetings {self.first_name} {self.last_name}")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

class Priviledges:

    def __init__(self, priviledges = ['can add post', 'can delete post', 'can ban user']):
        self.priviledges = priviledges

    def show_priviledges(self):
        print(f'The priviledges of the admin {self.priviledges}.')


class Admin(user):

    def __init__(self, first_name, last_name, sex, age, login_attempts):
        super().__init__(first_name, last_name, sex, age, login_attempts)
        self.priviledges = Priviledges()

restaurant1 = Restaurant("BinBelt", "cafea")
restaurant2 = Restaurant("Levant", "libanez")
restaurant3 = Restaurant("Prepelitescu", "yuck")

user1 = user("Gabriel", "Marin", "M", 34, 0)
user2 = user("Adina", "Marin", "F", 32, 0)
admin1 = Admin('Gabi', 'Sefu', 'M', 50, 0)

restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()


user1.describe_user()
user2.describe_user()

user1.greet_user()
user2.greet_user()

restaurant3.number_served = 15
print(f"{restaurant3.number_served}")
restaurant3.set_number_served(20)
print(f"{restaurant3.number_served}")
restaurant3.increment_number_served(5)
restaurant3.print_restaurant()

user1.increment_login_attempts()
print(f"{user1.login_attempts}")
user1.increment_login_attempts()
print(f"{user1.login_attempts}")
user1.reset_login_attempts()
print(f"{user1.login_attempts}")

icecreamstand1 = IceCreamStand('Inghetata gratis', 'Inghetata')
icecreamstand1.describe_flavours()

admin1.priviledges.show_priviledges()
