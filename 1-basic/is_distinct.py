"""
Write a Python function that takes a sequence of numbers and determines
if all the numbers are different from each other (that is, they are distinct)
"""

def is_distinct(in_list):
    out_set = set()
    for v in in_list:
        out_set.add(v)
    if len(out_set) == len(in_list):
        return True
    else:
        return False

def main():
    while True:
        integer_list = input("Please insert a list of integer: ")
        print is_distinct(integer_list)
        con = input("Continue? [y/n]: ")
        if con != 'y':
            break
    
if __name__ == '__main__':
    main()