#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    tempnum = -number
    lastnum = tempnum % 10
    lastnum = -lastnum
else:
    lastnum = number % 10
if lastnum > 5:
    print("Last digit of {:d} is {:d} and is greater than 5"
          .format(number, lastnum))
elif lastnum is 0:
    print("Last digit of {:d} is 0 and is 0".format(number))
else:
    print("Last digit of {:d} is {:d} and is less than 6 and not 0"
          .format(number, lastnum))
