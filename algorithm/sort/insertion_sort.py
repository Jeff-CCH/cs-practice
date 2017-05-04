class InsertionSort(object):
    def __init__(self, seq_list):
        self._data = seq_list

    def sort(self):
        for i in range(len(self._data)):
            j = i
            while j > 0:
                if self._data[j] < self._data[j-1]:
                    self._data[j-1], self._data[j] = self._data[j], self._data[j-1]
                j -= 1

    def result(self):
        return self._data


def main():
    i1 = InsertionSort([1,2,3,4,5])
    i1.sort()
    print i1.result()

    i2 = InsertionSort([10, 9, 8, 7, 6])
    i2.sort()
    print i2.result()


if __name__ == '__main__':
    main()
