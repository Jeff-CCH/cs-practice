"""
Python allows negative integers to be used as indices into a sequence, such as a string. If string s has length n, and expression s[k] is used for index -n<= k < 0, what is the equivalent index j>=0 such that s[j] references the same element?
"""

def show_string_by_index(string):
    str_len = len(string)
    n_str_len = str_len * (-1)
    # -n <= k < 0 equals to 0 <= k < n-1
    return string[n_str_len:-1] + string[-1], string[0:str_len]


def main():
    while True:
        string = input("Please input a string: ")
        print show_string_by_index(string)
        con = input("Continue? [y/n]: ")
        if con != 'y':
            break

if __name__ == '__main__':
    main()
