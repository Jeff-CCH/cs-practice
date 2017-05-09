"""
Use recursion to write a Python function for determining if a string s has
more vowels than consonants.
"""

vowel = ['a', 'e', 'i', 'o', 'u']

def determine(str_in, count=0):
    if len(str_in) == 0:
        if count > 0: print '#vowel > #consonants'
        elif count == 0: print '#vowel == #consonants'
        else: print '#vowel < #cosonants'
    else:
        if str_in[0] in vowel: return determine(str_in[1:], count+1)
        else: return determine(str_in[1:], count-1)
    

def main():
    determine('apple')
    determine('moon')
    determine('yooo')

if __name__ == '__main__':
    main()
