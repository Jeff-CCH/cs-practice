"""
Given a Python list L of n positive integers, each represented with k = |-logn-|+ 1 bits, describe an O(n)-time method for finding a k-bit integer not in L.
"""

def find_non_exist_integer(data):
    tt_list = [None] * len(data) * 2
    # put n integers in a list, cost O(n)
    for v in data:
        tt_list[v] = v

    # scan the list to find the first None, cost O(n)
    for i in range(len(tt_list)):
        if tt_list[i] is None:
            return i
    
def main():
    print find_non_exist_integer([1,2,0,4])
    print find_non_exist_integer([2,0,3,1])
    print find_non_exist_integer([0,1,4,3])

if __name__ == '__main__':
    main()
