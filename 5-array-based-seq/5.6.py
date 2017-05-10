"""
Our implementation of insert for the DynamicArray class, as given in Code Fragment 5.5, has the following inefficiency. In the case when a re- size occurs, the resize operation takes time to copy all the elements from an old array to a new array, and then the subsequent loop in the body of insert shifts many of those elements. Give an improved implementation of the insert method, so that, in the case of a resize, the elements are shifted into their final position during that operation, thereby avoiding the subsequent shifting
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

    def insert(self, k, value):
        if self._n == self._capacity:
            c= self._capacity * 2
            new_array = self._make_array(c)
            for j in range(k):
               new_array[j] = self._A[j]
            new_array[k] = value
            for j in range(k, self._n):
                new_array[j+1] = self._A[j]
            self._capacity = c
            self._A = new_array
        else:    
            for j in range(self._n, k, -1):
                self._A[j] = self._A[j-1]
            self._A[k] = value
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
    for data in d:
        print data

    d2 = DynamicArray()
    d2.insert(0, '1')
    d2.insert(1, '2')
    d2.insert(2, '3')
    d2.insert(3, '4')
    for data in d2:
        print data

    d3 = DynamicArray()
    d3.insert(0, '1')
    d3.insert(0, '2')
    d3.insert(0, '3')
    d3.insert(0, '4')
    for data in d3:
        print data
    



if __name__ == '__main__':
    main()
