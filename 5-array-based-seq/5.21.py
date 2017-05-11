"""
n Section 5.4.2, we described four different ways to compose a long string: (1) repeated concatenation, (2) appending to a temporary list and then joining, (3) using list comprehension with join, and (4) using genera- tor comprehension with join. Develop an experiment to test the efficiency of all four of these approaches and report your findings.
"""

import time

def repeated_cc(data_list, word=''):
    for d in data_list:
        word = word + d
    return word

def append_tmp_list(data_list, tmp=[]):
    for d in data_list:
        tmp.append(d)
    return tmp

def list_compre_join(data_list):
    return ''.join([d for d in data_list])

def gen_compre_join(data_list):
    return ''.join(d for d in data_list)

def main():
    n = 1000000
    data_list = ['a'] * n

    time_s = time.time()
    repeated_cc(data_list)
    time_e = time.time()
    print time_e - time_s

    time_s = time.time()
    append_tmp_list(data_list)
    time_e = time.time()
    print time_e - time_s

    time_s = time.time()
    list_compre_join(data_list)
    time_e = time.time()
    print time_e - time_s

    time_s = time.time()
    gen_compre_join(data_list)
    time_e = time.time()
    print time_e - time_s

if __name__ == '__main__':
    main()
