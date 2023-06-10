#!/usr/bin/python3
for i in range(1, 89):
    tens_digit = i // 10
    ones_digit = i % 10
    if ones_digit > tens_digit:
        print("{:02d}, ".format(i), end='')

print(89)
