"""
Implement a pop method for the DynamicArrayclass, given in CodeFragment 5.3, that removes the last element of the array, and that shrinks the capacity, N, of the array by half any time the number of elements in the array goes below N/4.
"""

import ctypes

class DynamicArray:
    def __init__(self):
        self._n = 0
        self._capacity = 1
        self._A = self._make_array(self._capacity)

    def __len__(self):
        return self._n

    def __getitem__(self, k):
        if not 0 <= k < self._n:
            k = k + self._n
        return self._A[k]

    def pop(self):
        if self._n < self._capacity/4:
            print 'shrink size from {0} to {1}'.format(self._capacity, self._capacity/2)
            self._resize(self._capacity/2)

        self._n -= 1
        return self._A[self._n]

    def append(self, obj):
        if self._n == self._capacity:
            self._resize(2 * self._capacity)
        self._A[self._n] = obj
        self._n += 1

    def _resize(self, c):
        B = self._make_array(c)
        for k in range(self._n):
            B[k] = self._A[k]
        self._A = B
        self._capacity = c

    def _make_array(self, c):
        return (c * ctypes.py_object)()

def main():
    d = DynamicArray()
    d.append('1')
    d.append('2')
    d.append('3')
    d.append('4')

    for i in range(len(d)):
        print d.pop()

if __name__ == '__main__':
    main()
