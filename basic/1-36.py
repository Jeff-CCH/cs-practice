"""
Write a Python program that inputs a list of words, separated by white space, and outputs how many times each word appears in the list. You need not worry about efficiency at this point, however, as this topic is something that will be addressed later in this book.
"""

def count_word(w_list):
    w_set = set(w_list)
    for v in w_set:
        print v, w_list.count(v)


def main():
    while True:
        words = input("Please input a list of words separated by white space: ")
        word_list = words.split()
        count_word(word_list)
        con = input("Continue? [y/n]: ")
        if con != 'y':
            break

if __name__ == '__main__':
    main()
