#!/usr/bin/env python3
from sys import argv
def sum_digits(sumthing):
    total = 0
    while sumthing > 0:
        total += sumthing % 10
        sumthing /= 10
    if total >= 10:
        total = sum_digits(total) 
    return total

def sum_up(upto):
    total = 0
    for n in range(0, upto + 1):
        total = sum_digits(total + n)
    return total
lucky = sum_up(int(argv[1]))
print("your lucky digit calculated by python is {}".format(lucky))
