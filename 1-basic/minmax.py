"""
Write a short Python function, minmax(data), that takes a sequence of one or more numbers, and returns the smallest and largest numbers, in the form of a tuple of length two. Do not use the built-in functions min or max in implementing your solution.
"""

def minmax(data):
    min_v = data[0]
    max_v = data[0]
    for d in data:
        if d > max_v:
            max_v = d
        elif d < min_v:
            min_v = d

    return min_v, max_v

def main():
    while True:
        data = input("Please input a sequence of number separated by comma: ")
        print minmax(data)
        con = input("Continue? [y/n]: ")
        if con != 'y':
            break

if __name__ == '__main__':
    main()
