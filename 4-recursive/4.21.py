"""
Suppose you are given an n element sequence, S, containing distinct integers that are listed in increasing order. Given a number k, describe a recursive algorithm to find two integers in S that sum to k, if such a pair exists. What is the running time of your algorithm?
"""

def find_sum(s, k):
    if len(s) == 1: return None
    else:
        if int(s[0]) + int(s[-1]) > k: return find_sum(s[:len(s)-1], k)
        elif int(s[0]) + int(s[-1]) == k: return '{0} + {1} == {2}'.format(s[0], s[-1], k)
        else: return find_sum(s[1:], k)

def main():
    print find_sum('24689', 12)
    print find_sum('13579', 8)
    print find_sum('13579', 7)

if __name__ == '__main__':
    main()
