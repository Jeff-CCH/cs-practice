"""
Write a pseudo-code description of a function that reverses a list of n
integers, so that the numbers are listed in the opposite order than they
were before, and compare this method to an equivalent Python function
for doing the same thing.
"""

def reverse_list(in_list):
    out_list = []
    l_len = len(in_list)*(-1)
    for v in range(-1, l_len-1, -1):
        out_list.append(in_list[v])
    return out_list

def main():
    while True:
        integer_list = input("Please insert a list of integer: ")
        print reverse_list(integer_list)
		integer_list.reverse()
        print integer_list
        con = input("Continue? [y/n]: ")
        if con != 'y':
            break
    
if __name__ == '__main__':
    main()