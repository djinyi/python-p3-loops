#!/usr/bin/env python3

def happy_new_year():
    i = 10
    while i > 0:
        print(f"{i}")
        i -= 1
    print("Happy New Year!")

def square_integers(int_list):
    new_int = [int*int for int in int_list]
    return [1, 4, 9, 16, 25]

def fizzbuzz():
    i = 1
    while i < 101:
        if i%3==0 and i%5==0:
            print("FizzBuzz")
        elif i%5==0:
            print("Buzz")
        elif i%3==0:
            print("Fizz")
        else:
            print(f"{i}")
        i += 1
