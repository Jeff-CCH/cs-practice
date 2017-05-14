"""
Thesyntaxdata.remove(value)forPythonlistdataremovesonlythefirst occurrence of element value from the list. Give an implementation of a function, with signature remove all(data, value), that removes all occur- rences of value from the given list, such that the worst-case running time of the function is O(n) on a list with n elements. Not that it is not efficient enough in general to rely on repeated calls to remove.
"""

def remove_all(data, value):
    return [d for d in data if d != value]

def main():
    print remove_all([1,2,3,4,5,5], 5)
    print remove_all([1,2,3,4,4,4], 4)
    print remove_all([1,1,101,202,2,1], 1)

if __name__ == '__main__':
    main()
