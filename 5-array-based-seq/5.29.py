"""
A useful operation in databases is the natural join. If we view a database as a list of ordered pairs of objects, then the natural join of databases A and B is the list of all ordered triples (x,y,z) such that the pair (x,y) is in A and the pair (y,z) is in B. Describe and analyze an efficient algorithm for computing the natural join of a list A of n pairs and a list B of m pairs.
"""

# cost O(len(A) + len(B))

def natural_join(A, B):
    max_v = -1
    for v in A:
        if v[1] > max_v:
            max_v = v[1]

    joined = [None] * (max_v + 1)
    # use index instead of hash
    for v in A:
        joined[v[1]] = v
    for v in B:
        if joined[v[0]] is not None:
            print '({0}, {1}, {2})'.format(joined[v[0]][0],
                                           joined[v[0]][1],
                                           v[1])

def main():
    print natural_join([(0,1),(2,3),(4,5)], [(1,3), (3,9), (5,0)])


if __name__ == '__main__':
    main()
