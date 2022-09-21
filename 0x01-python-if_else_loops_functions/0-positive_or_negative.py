#!/usr/bin/python3
import random
number = random.randint(-10, 10)
# YOUR CODE HERE
postive = "is positive"
negative = "is negative"
zero = "is zero"

if number > 0:
    print ("{} {}".format(number, positive)
elif number == 0:
    print ("{} {}".format(number, zero)
else:
    print("{} {}".format(number, negative)
