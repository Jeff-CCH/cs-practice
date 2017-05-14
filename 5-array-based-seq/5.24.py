"""
Perform experiments to evaluate the efficiency of the remove method of Python's list class, as we did for insert on page 205. Use known values so that all removals occur either at the beginning, middle, or end of the list. Report your results akin to Table 5.5.
"""

import time

def list_remove(n,k):
    data_list = ['a'] * 2 * n
    start_t = time.time()
    for i in range(n):
        data_list.remove(data_list[k])
    end_t = time.time()
    print "n: {0} k {1} uses {2}".format(n, k, end_t - start_t)

def main():
    n = [100, 1000, 10000, 100000, 1000000]
    for k in n:
        list_remove(k, 0)
        list_remove(k, k//2)
        list_remove(k, -1)


if __name__ == '__main__':
    main()
