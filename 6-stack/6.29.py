"""
add rotate function to class ArrayQueue
"""

class ArrayQueue():
    DEFAULT_CAPACITY = 10

    def __init__(self, max_len=None):
        if max_len is not None: self._capacity = max_len
        else: self._capacity = ArrayQueue.DEFAULT_CAPACITY
        self._data = [None] * self._capacity
        self._size = 0
        self._front = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def first(self):
        if self.is_empty():
            raise Empty('Q is empty')
        return self._data[self._front]

    def dequeue(self):
        if self.is_empty():
            raise Empty('Q is empty')
        answer = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % self._capacity
        self._size -= 1
        return answer

    def enque(self, e):
        if self._size == self._capacity:
            raise Exception('q is full')
        avail = (self._front + self._size) % self._capacity
        self._data[avail] = e
        self._size += 1

    def rotate(self):
        self._front = (self._front + 1) % self._capacity

def main():
    max_len = 10
    a = ArrayQueue(max_len=max_len)
    for i in range(max_len):
        a.enque(i)

    a.rotate()

    for i in range(max_len):
        print a.dequeue()

if __name__ == '__main__':
    main()
