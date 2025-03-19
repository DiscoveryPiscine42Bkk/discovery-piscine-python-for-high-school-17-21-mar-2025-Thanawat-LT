#!/usr/bin/env python3
a = float(input("Give me a number: "))
print(a)
if a.is_integer():
    print('This is an integer')
else:
    print('This is a decimal')