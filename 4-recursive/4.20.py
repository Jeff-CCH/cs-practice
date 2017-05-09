"""
Given an unsorted sequence, S, of integers and an integer k, describe a recursive algorithm for rearranging the elements in S so that all elements less than or equal to k come before any elements larger than k. What is the running time of your algorithm on a sequence of n values?
"""

def rearrange(data, k, word=''):
    if len(data) == 0: print word
    else:
        if int(data[0]) <= k: rearrange(data[1:], k, data[0] + word)
        else: rearrange(data[1:], k, word + data[0])

def main():
    rearrange('54321', 3)
    rearrange('71892', 1)
    rearrange('128740', 4)

if __name__ == '__main__':
    main()
