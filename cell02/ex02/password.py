#!/usr/bin/env python3
password = "Python is awesome"
user_pwd = input("Please type your password")
print(user_pwd)
if password == user_pwd:
    print("ACCESS GRANTED")
else:
    print("ACCESS DENIED")