"""
Our Dynamic Arrayclass, as given in Code Fragment 5.3, does not support use of negative indices with get item. Update that method to better match the semantics of a Python list
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
    print d[0], d[1], d[2], d[3], d[-1], d[-2], d[-3], d[-4]

if __name__ == '__main__':
    main()
