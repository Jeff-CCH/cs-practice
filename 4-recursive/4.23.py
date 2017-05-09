"""
Implement a recursive function with signature find(path, filename) that reports all entries of the file system rooted at the given path having the given file name
"""

import os

def find(path, filename):
    print filename
    if os.path.isdir(path+filename) is False:
        return

    for entry in os.listdir(path+filename):
        find(path+filename+"/", entry)


def main():
    find("/home/ubuntu/cs-practice/4-recursive/", "4.23.py")
    find("/home/ubuntu/cs-practice/", "4-recursive")
    find("/home/ubuntu/", "cs-practice")

if __name__ == '__main__':
    main()
