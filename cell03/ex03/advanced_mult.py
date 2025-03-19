#!/usr/bin/env python3
def print_table(number):
    print(f"Table de {number}: ", end="")
    for int in range(11):
        print(number * int, end=" ")
    print()
for num in range(11):
    print_table(num)