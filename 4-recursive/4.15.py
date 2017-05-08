"""
Write a recursive function that will output all the subsets of a set of n
elements (without repeating any subsets.
"""

import copy

def output_subset(s, total_set, tt_set=set()):
    if len(s) == 0:
        total_set.add(frozenset(set()))
    else:
        for v in s:
            t1 = copy.deepcopy(tt_set)
            t1.add(v)
            total_set.add(frozenset(t1))
            output_subset(s-{v}, total_set, copy.deepcopy(t1))


def main():
    s = {1,2,3}
    tt_set = set()
    output_subset(s, tt_set)
    print tt_set

if __name__ == '__main__':
    main()
