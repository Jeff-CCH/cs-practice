"""
Based on the discussion of page 207, develop an experiment to compare the efficiency of Python's list comprehension syntax versus the construction of a list by means of repeated calls to append
"""

import time

def main():
    n = 10000000
    in_list = []
    time_s = time.time()
    for i in range(n):
        in_list.append(i)
    time_e = time.time()
    print 'append uses {0}'.format(time_e - time_s)

    time_s = time.time()
    in_list = [i for i in range(n)]
    time_e = time.time()
    print 'comprehension syntax uses {0}'.format(time_e - time_s)

if __name__ == '__main__':
    main()
