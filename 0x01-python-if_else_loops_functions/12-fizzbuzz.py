#!/usr/bin/python3
def fizzbuzz():
    for i in range(1, 101):
        if i % 3 is 0 and i % 5 is 0:
            print("{} ".format("FizzBuzz"), end="")
        elif i % 3 is 0:
            print("{} ".format("Fizz"), end="")
        elif i % 5 is 0:
            print("{} ".format("Buzz"), end="")
        else:
            print("{} ".format(i), end="")
