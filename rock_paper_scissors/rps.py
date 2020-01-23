#!/usr/bin/python

import sys

def rock_paper_scissors(n):
  options = ['rock', 'paper', 'scissors']
  possible_chances = []

  if n == 0:
      return [[]]
  elif n == 1:
      return [[options[0]], [options[1]], [options[2]]]
  if n == 2:
      for first_option in options:
        for second_option in options:
          comb = [first_option, second_option]
          possible_chances.append(comb)
  if n == 3:
      for first_option in options:
        for second_option in options:
          for third_option in options:
            comb = [first_option, second_option, third_option]
            possible_chances.append(comb)
  if n == 4:
      for first_option in options:
        for second_option in options:
          for third_option in options:
            for fourth_option in options:
                comb = [first_option, second_option, third_option, fourth_option]
                possible_chances.append(comb)
  if n == 5:
      for first_option in options:
        for second_option in options:
          for third_option in options:
            for fourth_option in options:
              for fifth_option in options:
                  comb = [first_option, second_option, third_option, fourth_option, fifth_option]
                  possible_chances.append(comb)
  return possible_chances


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')