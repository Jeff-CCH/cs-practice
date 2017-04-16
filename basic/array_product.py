"""
Write a short Python program that takes two arrays a and b of length n
storing int values, and returns the dot product of a and b. That is, it returns
an array c of length n such that c[i] = a[i] * b[i], for i = 0, ... , n-1
"""

def array_product(a,b):
    for i in range(len(a)):
        yield a[i]*b[i]
    
def main():
    a = [1,2,3,4,5]
    b = [5,4,3,2,1]

    print [k for k in array_product(a,b)]
    
if __name__ == '__main__':
    main()