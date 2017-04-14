"""
Write a short Python function that takes a positive integer n and returns the sum of the squares of all the odd positive integers smaller than n
"""

def sum_of_odd(n):
    total = 0
    for v in range(n):
        if v % 2 != 0:
            total += v*v
    return total

def main():
    while True:
        n = input("Please input an integer n: ")
        print sum_of_odd(n)
        con = input("Continue? [y/n]: ")
        if con != 'y':
            break

if __name__ == '__main__':
    main()
