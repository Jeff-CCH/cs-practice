"""
Write a short recursive Python function that finds the minimum and maximum values in a sequence without using any loops.
"""

def find_max(in_list):
    if len(in_list) == 1:
        return in_list[0]
    else:
        return max(in_list[0], find_max(in_list[1:]))

def find_min(in_list):
    if len(in_list) == 1:
        return in_list[0]
    else:
        return min(in_list[0], find_max(in_list[1:]))

def find_max_min(in_list):
    return find_max(in_list), find_min(in_list)


def find_max_min2(in_list):
    if len(in_list) == 1:
        return in_list[0], in_list[0]
    else:
        return max(in_list[0], find_max_min2(in_list[1:])[0]), min(in_list[0], find_max_min2(in_list[1:])[1])


def main():
    data_list = [1,2,3,4,5,6,7,8,9,10]
    max_val, min_val = find_max_min2(data_list)
    print "Max: {0} min: {1}".format(max_val, min_val)

if __name__ == '__main__':
    main()
