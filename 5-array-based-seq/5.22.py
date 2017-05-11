"""
Develop an experiment to compare the relative efficiency of the extend method of Python's list class versus using repeated calls to append to accomplish the equivalent task.
"""

import time

def extend_l(l1, l2):
    l1.extend(l2)

def append_l(l1, l2):
    for v in l2:
        l1.append(v)

def main():
    n = 5000000
    l1 = ['a'] * n
    l2 = ['b'] * n

    start_t = time.time()
    extend_l(l1,l2)
    end_t = time.time()
    print 'extend uses {0} seconds'.format(end_t - start_t)

    start_t = time.time()
    append_l(l1,l2)
    end_t = time.time()
    print 'append uses {0} seconds'.format(end_t - start_t)

if __name__ == '__main__':
    main()
