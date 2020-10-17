from random import randint

class Dice:

    def __init__(self, sides = 6):
        self.sides = sides

    def roll_dice(self, roll_number):
        self.roll_number = roll_number
        for i in range(0, self.roll_number):
            self.roll = randint(1, self.sides)
            print(f'The number that the dice is showing is {self.roll}.')

dice1 = Dice(2)
dice1.roll_dice(10)
