"""
Write a short Python function that takes a string s, representing a sentence,
and returns a copy of the string with all punctuation removed. For example,
if given the string "Let's try, Mike.", this function would return
"Lets try Mike".
"""

def remove_punctuation(string):
    out_list = []
    for c in string:
        if 65 <= ord(c) <= 90 or 97 <= ord(c) <= 122 or ord(c) == 32:
            out_list.append(c)
    return ''.join(out_list)

def main():
    while True:
        string = input("Please input a string: ")
        print remove_punctuation(string)
        con = input("Continue? [y/n]: ")
        if con != 'y':
            break
    
if __name__ == '__main__':
    main()