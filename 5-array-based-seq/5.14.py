"""
The shuffle method, supported by the random module, takes a Python list and rearranges it so that every possible ordering is equally likely. Implement your own version of such a function. You may rely on the randrange(n) function of the random module, which returns a random number between 0 and n - 1inclusive
"""

import random

def shuffle(l):
    length = len(l)
    for i in range(length):
        rand_i = random.randrange(length)
        l[i], l[rand_i] = l[rand_i], l[i]
    print l

def main():
   shuffle(['H', 'E', 'L', 'L', 'O']) 
   shuffle(['W', 'O', 'R', 'L', 'D']) 
   shuffle(['T', 'R', 'E', 'E']) 

if __name__ == '__main__':
    main()
