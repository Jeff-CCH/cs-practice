"""
Describe a nonrecursive algorithm for enumerating all permutations of the numbers {1,2,...,n} using an explicit stack.
"""

def enumerate_permu_list(n):
    res = [[] for i in range(n)]
    for i in range(n):
        res[0].append(str(i+1))


    for i in range(1, n+1):
        for v in res[i-1]:
            for j in range(1,n+1):
                if str(j) not in v:
                    res[i].append(v+str(j))
    return res

def enumnerate_permu_stack(n):
    cnt = n-1
    stack.push([str(i+1) for i in range(n)])

    while cnt > 0:
        tmp = []
        for v in stack.pop():
            for j in range(1, n+1):
                if str(j) not in v:
                    tmp.append(v+str(j))
        stack.push(tmp)
        cnt -=1

def main():
    print enumerate_permu_list(2)
    print enumerate_permu_list(4)
    print enumerate_permu_list(9)

if __name__ == '__main__':
    main()
