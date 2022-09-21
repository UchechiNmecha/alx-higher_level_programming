#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# YOUR CODE HERE
num = str(number)
last = num[-1]

if number < 0:
    last_digit = (int(last)) * -1
else:
    last_digit = int(last)

if last_digit > 5:
    print("Last digit of {} is {} and is greater than 5".format(num, last_digit))
elif last_digit == 0:
    print("Last digit of {} is {} and is 0".format(num, last_digit))
elif last_digit < 6 and last_digit != 0:
    print("Last digit of {} is {} and is less than 6 and not 0".format(num, last_digit))
