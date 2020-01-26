#!/usr/bin/python

import sys

# the itertools module let you use multiple variables in a for loop, acting as nested loops.
# ex. 
# for i in n:
  # for j in n:
# Same as... for i, j in itertools.product(n):
import itertools

def rock_paper_scissors(n):
    # variable that holds the options available to choose
    options = ['rock', 'paper', 'scissors']
    # variable that holds the possible chances according to n
    possible_chances = []
    # BASES CASES
    if n == 0:
        return [[]]
    elif n == 1:
        return [[options[0]], [options[1]], [options[2]]]
    if n == 2:
        for a, b in itertools.product(options, options):
            possible_chances.append([a, b])
    if n == 3:
        for a, b, c in itertools.product(options, options, options):
            possible_chances.append([a, b, c])
    if n == 4:
        for a, b, c, d in itertools.product(options, options, options, options):
            possible_chances.append([a, b, c, d])
    if n == 5:
        for a, b, c, d, e in itertools.product(options, options, options, options, options):
            possible_chances.append([a, b, c, d, e])             
    return possible_chances

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')