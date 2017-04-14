"""
Exercise:
    Write a short Python function, is multiple(n, m), that takes two integer values and returns True if n is a multiple of m, that is, n = mi for some integer i, and False otherwise.
"""


def is_multiple(n,m):
    return True if n % m == 0 else False

def main():
    while True:
        n,m = input("please input two integers divided by a comma: ")
        print is_multiple(n,m)
        con = input("Continue? [y/n]: ")
        if con != 'y':
            break;

if __name__ == '__main__':
    main()
