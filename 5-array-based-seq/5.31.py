"""
Describe a way to use recursion to add all the numbers in an n * n data set, represented as a list of lists.
"""

def recursive_add(ds):
    if len(ds) == 1:
        return sum(i for i in ds[0])

    return recursive_add(ds[0:1]) + recursive_add(ds[1:])
    
def produce_n_n_ds(n):
    res = []
    for i in range(n):
        res.append([j for j in range(n)])
    return res

def main():
    n = 3
    nn_ds = produce_n_n_ds(n)
    print "data set: {0}".format(nn_ds)
    print "ds sum: {0}".format(recursive_add(nn_ds))

if __name__ == '__main__':
    main()
