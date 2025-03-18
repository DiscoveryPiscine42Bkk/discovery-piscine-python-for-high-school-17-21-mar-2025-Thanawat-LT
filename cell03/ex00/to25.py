#!/usr/bin/env python3
a=int(input("Enter a number less than 25"))
if a > 25:
    print("Error")
elif a < 25:
    print(a)
while a < 26:
    print(f"Inside the loop, my variable is  {a}")
    a += 1