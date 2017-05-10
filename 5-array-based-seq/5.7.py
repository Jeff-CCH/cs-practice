"""
Let A be an array of size n >= 2 containing integers from 1 to n - 1, inclusive, with exactly one repeated. Describe a fast algorithm for finding the integer in A that is repeated.
"""

def find_repeat(data, n):
    data_tt = sum(data)
    real_tt = sum(k for k in range(n+1))
    return n - (real_tt - data_tt)

def main():
    data = [1,1,2,3]
    print find_repeat(data, len(data))

    data = [1,2,2,3]
    print find_repeat(data, len(data))

    data = [1,2,3,3,4,5]
    print find_repeat(data, len(data))

if __name__ == '__main__':
    main()
