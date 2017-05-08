"""
output a subset of a list
"""

def output_subset(data_s, tt_set, word=''):
    tt_set.append(word)
    for s in data_s:
        output_subset(data_s - {s}, tt_set, word + s)


def main():
    data = set('12345')
    data_tt_set = []
    output_subset(data, data_tt_set)
    print data_tt_set

    str1 = set('string')
    str_tt_set = []
    output_subset(str1, str_tt_set)
    print str_tt_set

if __name__ == '__main__':
    main()
