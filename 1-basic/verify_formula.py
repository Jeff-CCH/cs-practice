"""
Write a short program that takes as input three integers, a, b, and c, from
the console and determines if they can be used in a correct arithmetic
formula (in the given order), like "a+b = c," "a = b - c," or "a * b = c."
"""

def verify_formula(a,b,c):
    if a + b == c:
        print("{0} + {1} = {2}".format(a,b,c))
    if a == b - c:
        print("{0} = {1} - {2}".format(a,b,c))
    if a * b == c:
        print("{0} * {1} = {2}".format(a,b,c))

def main():
    while True:
        a,b,c = input("Please input 3 integers separated by comma: ")
        verify_formula(a,b,c)
        con = input("Continue? [y/n]: ")
        if con != 'y':
            break
    
if __name__ == '__main__':
    main()