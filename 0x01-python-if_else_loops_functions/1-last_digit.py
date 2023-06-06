#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)


def lastdegit(number):
    if number < 0:
        number = -(number)
        return -(number % 10)
    return (number % 10)


if lastdegit(number) == 0:
    print(f"Last digit of {number} is {lastdegit(number)} and is 0")
elif lastdegit(number) > 5:
    print(f"Last digit of {number} is {lastdegit(number)} and "
          f"is greater than 5")
elif lastdegit(number) < 6 and lastdegit(number) != 0:
    if number < 0:
        print(f"Last digit of {number} is {lastdegit(number)} and "
              f"is less than 6 and not 0")
