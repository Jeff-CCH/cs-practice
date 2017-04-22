"""
Exercise:
    Write a short Python function, is_even(k), that takes an integer value and returns True if k is even, and False otherwise. However, your function cannot use the multiplication, modulo, or division operators.
"""

def is_even(k):
    return True if (-1) ** k == 1 else False
    return True if "{:b}".format(k)[-1] == '0' else False

def main():
    while True:
        k = input("Please input an integer: ")
        print is_even(k)
        con = input("Continue? [y/n]: ")
        if con != 'y':
            break

if __name__ == '__main__':
    main()
