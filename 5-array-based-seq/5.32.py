"""
Write a Python function that takes two three-dimensional numeric data sets and adds them componentwise.
"""

from random import randint

def three_dim_add(A, B):
    print 'Add {0} & {1}'.format(A, B)
    result = []
    for i in range(len(A)):
        result.append([A[i][0] + B[i][0],
                       A[i][1] + B[i][1],
                       A[i][2] + B[i][2]])
    return "result: {0}".format(result)

def produce_three_ds(n):
    return [[randint(0, n), randint(0, n), randint(0, n)] for i in range(n)]    

def main():
    n = 3
    print three_dim_add(produce_three_ds(n), produce_three_ds(n))

if __name__ == '__main__':
    main()
