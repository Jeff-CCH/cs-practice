"""
Describe an efficient recursive function for solving the element uniqueness problem, which runs in time that is at most O(n^2) in the worst case without using sorting.
"""

def is_uniq(data_list):
    if len(data_list) == 1:
        return True
    else:
        if is_uniq(data_list[1:]) is not True:
            return False
        for i in range(len(data_list)):
            if i == 0:
                continue
            if data_list[0] == data_list[i]:
                return False
        return True

def is_uniq2(data_list):
    if len(data_list) == 1:
        return True
    else:
        if is_uniq2(data_list[1:]) is not True:
            return False
        return data_list[0] not in data_list[1:]

def main():
    d_list = [1,2,3,4,5]
    d_list2 = [1,1,2,3,4]
    str1 = "Hello"
    str2 = "World"
    print is_uniq(d_list)
    print is_uniq2(d_list)
    print "---"

    print is_uniq(d_list2)
    print is_uniq2(d_list2)
    print "---"
    
    print is_uniq(str1)
    print is_uniq2(str1)
    print "---"
    
    print is_uniq(str2)
    print is_uniq2(str2)
    print "---"

if __name__ == '__main__':
    main()
