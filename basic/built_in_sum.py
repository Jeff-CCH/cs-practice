"""
Give a single command that computes the sum from Exercise R-1.4, rely- ing on Python's comprehension syntax and the built-in sum function.
"""

def main():
    while True:
        n = input("Please input an integer: ")
        print sum(k*k for k in range(n))
        con = input("Continue? [y/n]: ")
        if con != 'y':
            break

if __name__ == '__main__':
    main()
