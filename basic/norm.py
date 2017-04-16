"""
The p-norm of a vector v = (v1,v2,...,vn) in n-dimensional space is de-
fined as

For the special case of p = 2, this results in the traditional Euclidean
norm, which represents the length of the vector. For example, the Euclidean
norm of a two-dimensional vector with coordinates (4,3) has a
Euclidean norm of
Give an implementation
of a function named norm such that norm(v, p) returns the p-norm
value of v and norm(v) returns the Euclidean norm of v. You may assume
that v is a list of numbers.
"""

import math

def norm(v,p=2):
    en_value = 0
    for value in v:
        en_value += value ** p
    return math.pow(en_value, 1.0/float(p))
        
def main():
    while True:
        input_list = input("Please insert p with a list of number: ")
        if input_list[0] == 2:
            print norm(input_list[1:])
        else:
            print norm(input_list[1:], input_list[0])
        con = input("Continue? [y/n]: ")
        if con != 'y':
            break

if __name__ == '__main__':
    main()