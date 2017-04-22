"""
Write a Python program that outputs all possible strings formed by using thecharacters c , a , t , d , o ,and g exactlyonce.
"""

def possible_str(str_set, word=''):
    if not str_set:
        print word
    for str_v in str_set:
        possible_str(str_set - {str_v}, word + str_v)

def main():
    possible_str(set('catdog'))

if __name__ == '__main__':
    main()
