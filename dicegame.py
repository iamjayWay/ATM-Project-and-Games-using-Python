import random

class Dice:
    def roll(self):
        first = random.randint(1, 6)
        second = random.randint(1, 6)
        third = random.randint(1, 6)
        return first, second, third
    
dice = Dice()
print(dice.roll())