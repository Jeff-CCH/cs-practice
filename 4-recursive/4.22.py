"""
Develop a nonrecursive implementation of the version of power from Code Fragment 4.12 that uses repeated squaring.
"""

def power(x,n, seq=''):
    if n == 0:
        return 1

    while n > 0:
        if n % 2 == 1:
            n = n - 1
            seq = "+" + seq
        else:
            seq = "*" + seq
            n = n // 2

    result = 1
    for s in seq:
        if s == '+': result = result * x
        else: result = result * result
    
    return result


def main():
    print power(2,1)
    print power(2,5)
    print power(2,10)

if __name__ == '__main__':
    main()
