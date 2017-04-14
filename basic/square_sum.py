"""
Write a short Python function that takes a positive integer n and returns the sum of the squares of all the positive integers smaller than n.
"""

def square_sum(n):
    total = 0
    for v in range(n):
        total += v*v
    return total

def main():
    while True:
        n = input("Please input an integer: ")
        print square_sum(n)
        print square_sum2(n)
        con = input("Continue? [y/n]: ")
        if con != 'y':
            break

if __name__ == '__main__':
    main()
