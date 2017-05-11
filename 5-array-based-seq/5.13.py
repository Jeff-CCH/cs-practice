"""
In the experiment of Code Fragment 5.1, we begin with an empty list. If data were initially constructed with nonempty length, does this affect the sequence of values at which the underlying array is expanded? Perform your own experiments, and comment on any relationship you see between the initial length and the expansion sequence
"""

import sys

def append_list(data, n):
    for k in range(n):
        a = len(data)
        b = sys.getsizeof(data)
        print('Length: {0:3d}; Size in bytes: {1:4d}'.format(a,b))
        data.append(None)

def main():
    append_list([], 10)
    print '----'
    append_list([None]*10, 10)
    print '----'
    append_list([None]*20, 40)
    print '----'


if __name__ == '__main__':
    main()


