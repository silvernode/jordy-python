#!/usr/bin/python3

# Guess the randomly generated number
#

from random import *


answer = randint(1, 100)


while True:

    guess = int(input("Guess a number between 1 and 100: "))


    if guess > answer:
        print("too high")

    elif guess < answer:
        print("too low")

    elif guess == answer:
        print("you win")
        break


