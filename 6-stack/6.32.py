"""
Give a complete ArrayDeque implementation of the double-ended queue ADT as sketched in Section 6.3.2.
"""

class Deque(object):
    def __init__(self):
        self._capacity = 10
        self._deque = [None] * self._capacity
        self._front = 0
        self._size = 0

    def add_first(self, e):
        if self._size == self._capacity:
            resize(self._capacity * 2)
        self._front = (self._front + self._capacity - 1) % self._capacity
        self._deque[self._front] = e
        self._size += 1

    def add_last(self, e):
        if self._size == self._capacity:
            resize(self._capacity * 2)
        self._deque[(self._front + self._size) % self._capacity] = e
        self._size += 1
        
    def delete_first(self):
        val = self._deque[self._front]
        self._deque[self._front] = None
        self._front = (self._front + 1) % self._capacity
        self._size -= 1
        return val

    def delete_last(self):
        last_i = (self._front + self._size - 1) % self._capacity
        val = self._deque[last_i]
        self._deque[last_i] = None
        self._size -= 1
        return val

    def first(self):
        return self._deque[self._front]

    def last(self):
        last_i = (self._front + self._size - 1) % self._capacity
        return self._deque[last_i]

    def is_empty(self):
        return self._size == 0

    def __iter__(self):
        for i in range(self._size):
            yield self._deque[(self._front + i) % self._capacity]

    def __len__(self):
        return self._size

    def __resize__(self, n):
        new_deque = [None] * n
        for i in range(self._size):
            new_deque.append(self._deque[(self._front + i) % self._capacity])
        self._deque = new_deque
        self._front = 0
        self._capacity = n

def main():
    d = Deque()
    d.add_last(5)
    print "add last 5 to the q. Q: {0}".format(', '.join(str(e) for e in d))
    d.add_first(3)
    print "add first 3 to the q. Q: {0}".format(', '.join(str(e) for e in d))
    d.add_first(7)
    print "add first 7 to the q. Q: {0}".format(', '.join(str(e) for e in d))
    print "Q first: {0}".format(d.first())
    d.delete_last()
    print "delete last from the q. Q: {0}".format(', '.join(str(e) for e in d))
    print "Q length: {0}.".format(len(d))
    d.delete_last()
    print "delete last from the q. Q: {0}".format(', '.join(str(e) for e in d))
    d.delete_last()
    print "delete last from the q. Q: {0}".format(', '.join(str(e) for e in d))
    d.add_first(6)
    print "add first 6 to the q. Q: {0}".format(', '.join(str(e) for e in d))
    print "q.last: {0}".format(d.last())
    d.add_first(8)
    print "add first 8 to the q. Q: {0}".format(', '.join(str(e) for e in d))
    print "Q is empty: {0}".format(d.is_empty())
    print "q.last: {0}".format(d.last())


if __name__ == '__main__':
    main()
