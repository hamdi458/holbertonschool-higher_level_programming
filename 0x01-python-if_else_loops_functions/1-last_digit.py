#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    unite = number % -10
else:
    unite = number % 10
print("Last digit of {} is {} and is ".format(number, unite), end="")
if unite > 5:
    print("greater than 5")
elif unite == 0:
    print("0")
else:
    print("less than 6 and not 0")
