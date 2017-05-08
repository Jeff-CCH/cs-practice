"""
Describe a recursive algorithm to compute the integer part of the base-two logarithm of n using only addition and integer division.
"""

def logarithm(n):
    n = n//2
    if n < 0:
        raise ValueError('no negative input')
    elif 0 <= n <= 1:
        return n
    else:
        return 1 + logarithm(n)

def main():
    while True:
        data = int(input("Please give an integer number: "))
        print "The integer part of the base two logarithm of {0} is {1}".format(data, logarithm(data))
        con = input("Continue? [y/n]: ")
        if con != 'y':
            break

if __name__ == '__main__':
    main()
