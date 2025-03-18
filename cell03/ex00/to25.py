#!/usr/bin/env python3
X=int(input("Enter a number less than 25"))
if X > 25:
    print("Error")
elif X < 25:
    print(X)
while X < 26:
    print(f"Inside the loop, my variable is  {X}")
    X += 1