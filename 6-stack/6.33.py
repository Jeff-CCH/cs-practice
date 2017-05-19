"""
Give an array-based implementation of a double-ended queue supporting all of the public behaviors shown in Table 6.4 for the collections.deque class, including use of the maxlen optional parameter. When a length- limited deque is full, provide semantics similar to the collections.deque class, whereby a call to insert an element on one end of a deque causes an element to be lost from the opposite side
"""

class Deque(object):
    def __init__(self, max_len=10):
        self._capacity = max_len
        self._deque = [None] * self._capacity
        self._front = 0
        self._size = 0

    def appendleft(self, e):
        self._front = (self._front + self._capacity - 1) % self._capacity
        self._deque[self._front] = e
        if self._size < self._capacity:
            self._size += 1

    def append(self, e):
        self._deque[(self._front + self._size) % self._capacity] = e
        if self._size == self._capacity:
            self._front = (self._front + self._size + 1) % self._capacity
        else:
            self._size += 1
        
    def popleft(self):
        val = self._deque[self._front]
        self._deque[self._front] = None
        self._front = (self._front + 1) % self._capacity
        self._size -= 1
        return val

    def pop(self):
        last_i = (self._front + self._size - 1) % self._capacity
        val = self._deque[last_i]
        self._deque[last_i] = None
        self._size -= 1
        return val

    def clear(self):
        self.__init__(max_len=self._capacity)

    def rotate(self, k):
        new_deque = [None] * self._capacity
        self._front = (self._front + self._size - k) % self._capacity
        num = 0
        i = -1
        while num < self._capacity:
            i += 1
            if self._deque[(self._front + i) % self._capacity] is None:
                continue
            new_deque[num] = self._deque[(self._front + i) % self._capacity]
            num += 1

        self._deque = new_deque
        self._front = 0

    def remove(self, e):
        for i in range(self._size):
            if self._deque[(self._front + i) % self._capacity] == e:
                del self._deque[(self._front + i) % self._capacity]
                self._size -= 1
                break
                
    def count(self, e):
        cnt = 0
        for i in range(self._size):
            if self._deque[(self._front + i) % self._capacity] == e:
                cnt += 1
        return cnt

    def __getitem__(self, i):
        if i < 0:
            i = i + self._size
        return self._deque[(self._front + i) % self._capacity]

    def __setitem__(self, i, e):
        if i < 0:
            i = i + self._size
        self._deque[(self._front + i) % self._capacity] = e

    def is_empty(self):
        return self._size == 0

    def __iter__(self):
        for i in range(self._size):
            yield self._deque[(self._front + i) % self._capacity]

    def __len__(self):
        return self._size

def main():
    d = Deque()
    d.append(5)
    print "add last 5 to the q. Q: {0}".format(', '.join(str(e) for e in d))
    d.appendleft(3)
    print "add first 3 to the q. Q: {0}".format(', '.join(str(e) for e in d))
    d.appendleft(7)
    print "add first 7 to the q. Q: {0}".format(', '.join(str(e) for e in d))
    print "Q first: {0}".format(d[0])
    d.rotate(2)
    print "shift q elements for 2 steps. Q: {0}".format(', '.join(str(e) for e in d))
    d.pop()
    print "delete last from the q. Q: {0}".format(', '.join(str(e) for e in d))
    print "Q length: {0}.".format(len(d))
    d.pop()
    print "delete last from the q. Q: {0}".format(', '.join(str(e) for e in d))
    d.pop()
    print "delete last from the q. Q: {0}".format(', '.join(str(e) for e in d))
    d.appendleft(6)
    print "add first 6 to the q. Q: {0}".format(', '.join(str(e) for e in d))
    print "q.last: {0}".format(d[-1])
    d.appendleft(8)
    print "add first 8 to the q. Q: {0}".format(', '.join(str(e) for e in d))
    print "Q is empty: {0}".format(d.is_empty())
    print "q.last: {0}".format(d[-1])


if __name__ == '__main__':
    main()
