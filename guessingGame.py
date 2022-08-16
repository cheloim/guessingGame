#!/usr/bin/env python3.10
# encoding=utf8


import random

machineNumber = random.randint(1, 100)

print('Welcome to Guessing Game')
print('------------------------')
print('')
print('The rules are simple, you have unlitimed trys to gues the number')
print('the closer you get the wormer you get')
print("If your guess is more than 10 away from my number, I'll tell you you're COLD")  # noqa: E501
print("If your guess is within 10 of my number, I'll tell you you're WARM")
print("If your guess is farther than your most recent guess, I'll say you're getting COLDER")  # noqa: E501
print("If your guess is closer than your most recent guess, I'll say you're getting WARMER")  # noqa: E501
print("LET'S PLAY!")

guesses = [0]

while True:
    guess = int(input('Choose a number between 1 and 100: '))

    if guess < 1 or guess > 100:
        print('Number out of Bounds! Please try again: ')
        continue

    if guess == machineNumber:
        print(f"Congratulations, you've guesses it in only {len(guesses)} guessess!!")  # noqa: E501
        break

    guesses.append(guess)

    if guesses[-2]:
        if abs(machineNumber-guess) < abs(machineNumber-guesses[-2]):
            print("Warmer!")
        else:
            print("Colder!")
    else:
        if abs(machineNumber-guess) <= 100:
            print("Warm!")
        else:
            print("Cold!")
