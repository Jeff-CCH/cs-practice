"""
Python's random module includes a function shuffle(data) that accepts a
list of elements and randomly reorders the elements so that each possible
order occurs with equal probability. The random module includes a
more basic function randint(a, b) that returns a uniformly random integer
from a to b (including both endpoints). Using only the randint function,
implement your own version of the shuffle function.
"""

import random

def shuffle_data(data):
    len_d = len(data)
    out_list = ['None' for k in range(len_d)]
    for v in data:
        while True:
            index = random.randint(0, len_d-1)
            if out_list[index] == 'None':
                out_list[index] = v
                break
    return out_list

def shuffle_data2(data):
    len_d = len(data)
    for i in range(len_d):
        ran_index = random.randint(0, len_d - 1)
        data[i], data[ran_index] = data[ran_index], data[i] 

    return data

def main():
    while True:
        input_d = input("Please input a list of elements: ")
        print shuffle_data2(input_d)
        con = input("Continue? [y/n]: ")
        if con != 'y':
            break
    
if __name__ == '__main__':
    main()
