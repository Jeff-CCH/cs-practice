"""
Write a short Python function that takes a sequence of integer values and
determines if there is a distinct pair of numbers in the sequence whose
product is odd.
"""

def odd_product(in_list):
    num = 0
    output = []
    for v in in_list:
        if v % 2 != 0:
            output.append(v)
            num += 1
            return True, output if num == 2
    return False, []

def main():
    while True:
        integer_list = input("Please insert a list of integer: ")
        print odd_product(integer_list)
        con = input("Continue? [y/n]: ")
        if con != 'y':
            break
    
if __name__ == '__main__':
    main()