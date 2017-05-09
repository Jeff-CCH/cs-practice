"""
Write a short recursive Python function that determines if a string s is a palindrome, that is, it is equal to its reverse. For example, racecar and gohangasalamiimalasagnahog are palindromes.
"""

def is_palindrome(in_str, ori_str, word=''):
    if len(in_str) == 0:
        print "{0} is palindrome: {1}".format(ori_str, ori_str == word) 
    else:
        return is_palindrome(in_str[:len(in_str)-1], ori_str, word + in_str[-1])

def is_palindrome2(in_str):
    if len(in_str) <= 1: return True
    if in_str[0] != in_str[-1]: return False
    else: return is_palindrome2(in_str[1:len(in_str)-1])


def main():
    str1 = "String"
    str2 = "racecar"
    str3 = "gohangasalamiimalasagnahog"

    is_palindrome(str1, str1)
    print is_palindrome2(str1)

    is_palindrome(str2, str2)
    print is_palindrome2(str2)

    is_palindrome(str3, str3)
    print is_palindrome2(str3)


if __name__ == '__main__':
    main()
