"""
In Section 1.8, we provided three different implementations of a generator
that computes factors of a given integer. The third of those implementations,
from page 41, was the most efficient, but we noted that it did not
yield the factors in increasing order. Modify the generator so that it reports
factors in increasing order, while maintaining its general performance advantages.
"""

def factors(n):
    k = 1
    big_factors = []
    while k * k < n:
        if n % k == 0:
            yield k
            big_factors.append(n // k)
        k += 1
    if k * k == n:
        yield k

    for i in range(-1, (-1)*len(big_factors) -1, -1):
        yield big_factors[i]
        
def main():
    while True:
        n = input("Please insert an integer: ")
        print [k for k in factors(n)]
        con = input("Continue? [y/n]: ")
        if con != 'y':
            break

if __name__ == '__main__':
    main()