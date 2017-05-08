"""
Give a recursive algorithm to compute the product of two positive integers, m and n, using only addition and subtraction.
"""

def product(m, n):
    if n == 1:
        return m
    else:
        return m + product(m, n-1)

def main():
    print product(5,4)
    print product(10,10)
    print product(20,5)

if __name__ == '__main__':
    main()
