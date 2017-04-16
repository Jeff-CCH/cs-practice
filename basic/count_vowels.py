"""
Write a short Python function that counts the number of vowels in a given
character string.
"""

def count_vowel(string):
    cnt = 0
    vowel = ['a','e','i','o','u']
    for c in string:
        if c in vowel:
            cnt += 1
    return cnt

def main():
    while True:
        string = input("Please input a string: ")
        print count_vowel(string)
        con = input("Continue? [y/n]: ")
        if con != 'y':
            break
    
if __name__ == '__main__':
    main()