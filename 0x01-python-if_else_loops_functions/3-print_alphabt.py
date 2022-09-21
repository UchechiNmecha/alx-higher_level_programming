#!/usr/bin/python3
for alphabets in range(ord('a'), ord('z') + 1):
    if alphabets != ord('e') and alphabets != ord('q'):
        print("{:c}".format(alphabets), end="")
