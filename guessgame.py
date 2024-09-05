import random

guess = 0
randNum = random.randrange(1,11)
while guess != randNum:
    guess = int(input("Try to guess your number from 1-10: "))
    if guess == randNum:
        print("You got it")
    if guess > randNum:
        print("Wrong, your number is too High!")
    if guess < randNum:
        print("Wrong, your number is too Low!")