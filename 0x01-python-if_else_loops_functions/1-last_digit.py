#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# YOUR CODE HERE
num = str(number)
digit = num[-1]

if number < 0:
    last = (int(digit)) * -1
else:
    last = int(digit)

if last > 5:
    print("Last digit of {} is {} and is greater than 5".format(num, last))
elif last == 0:
    print("Last digit of {} is {} and is 0".format(num, last))
elif last < 6 and last != 0:
    print(f"Last digit of {num} is {last} and is less than 6 and not 0")
