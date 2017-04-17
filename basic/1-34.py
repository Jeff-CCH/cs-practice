"""
A common punishment for school children is to write out a sentence multiple times. Write a Python stand-alone program that will write out the following sentence one hundred times: "I will never spam my friends again." Your program should number each of the sentences and it should make eight different random-looking typos.
"""

import random

def gen_typo(in_list):
    len_list = len(in_list)

    rand_int1 = random.randint(0, len_list-1)
    while in_list[rand_int1] == ' ':
        rand_int1 = random.randint(0, len_list-1)

    rand_int2 = random.randint(0, len_list-1)
    while rand_int2 == rand_int1 or in_list[rand_int2] == ' ':
        rand_int2 = random.randint(0, len_list-1)

    in_list[rand_int1] = in_list[rand_int2] 

def main():
    string = "I will never spam my friends again."
    for i in range(100):
        if i < 8:
            strList = list(string)
            gen_typo(strList)
            output_str = ''.join(strList)
        else:
            output_str = string
        print "{0}:{1}".format(i+1, output_str)

if __name__ == '__main__':
    main()
