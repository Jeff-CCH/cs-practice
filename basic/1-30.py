"""
Write a Python program that can take a positive integer greater than 2 as input and write out the number of times one must repeatedly divide this number by 2 before getting a value less than 2.
"""

def cnt_times(n):
    cnt = 0
    while n >= 2:
        n = n / 2
        cnt += 1
    return cnt

def main():
    while True:
        n = input("Please input an integer n: ")
        print cnt_times(n)
        con = input("Continue? [y/n]: ")
        if con != 'y':
            break

if __name__ == '__main__':
    main()
