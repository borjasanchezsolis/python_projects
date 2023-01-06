import random


class Dice:
    def roll(self):
        print(random.randint(1, 6))


dice1 = Dice()
dice2 = Dice()
print(dice1.roll(), dice2.roll())



class Dice:
    def roll(self):
        first = random.randint(1, 6)
        second = random.randint(1, 6)
        return first, second


dice = Dice()
print(dice.roll())
