"""
Write a short recursive Python function that takes a character string s and outputs its reverse. For example, the reverse of pots&pans would be
snap&stop.
"""

def reverse(in_str):
    if len(in_str) == 1:
        return in_str
    else:
        return in_str[-1] + reverse(in_str[:len(in_str)-1])
    

def main():
    str1 = "pots&pans"
    str2 = "!dlrow olleH"
    print reverse(str1)
    print reverse(str2)

if __name__ == '__main__':
    main()
