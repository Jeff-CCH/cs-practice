"""
The birthday paradox says that the probability that two people in a room will have the same birthday is more than half, provided n, the number of people in the room, is more than 23. This property is not really a paradox, but many people find it surprising. Design a Python program that can test this paradox by a series of experiments on randomly generated birthdays, which test this paradox for n = 5,10,15,20,...,100.
"""

import random

def test_paradox(n):
    birth = set()
    for i in range(n):
        birth.add(str(random.randint(1,12)) + str(random.randint(1, 31)))
    if len(birth) < n:
        return n, len(birth), True
    else:
        return n, len(birth), False

def main():
    for k in range(5, 105, 5):
        print test_paradox(k)

if __name__ == '__main__':
    main()
