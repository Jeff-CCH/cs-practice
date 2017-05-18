"""
In the previous exercise, we assume that the underlying list is initially empty. Redo that exercise, this time preallocating an underlying list with length equal to the stack's maximum capacity.
"""

class ArrayStack:
    def __init__(self, max_len=1):
        self._data = [None for i in range(max_len)]
        self._max_len = max_len
        self._index = 0

    def __len__(self):
        return self._index + 1

    def is_empty(self):
        return self._index == 0

    def push(self, e):
        if self._index == self._max_len:
            raise Exception('stack is full')
        self._data[self._index] = e
        self._index += 1

    def top(self):
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data[self._index-1]

    def pop(self):
        if self.is_empty():
            raise Empty('Stack is empty')
        self._index -= 1
        val = self._data[self._index]
        self._data[self._index] = None
        return val

def main():
    try:
        max_len = 10
        a = ArrayStack(max_len=max_len)
        for i in range(max_len):
            a.push(i)
            print 'push {0}'.format(i)

        for i in range(max_len):
            print "top {0}".format(a.top())
            print "pop {0}".format(a.pop())

        for i in range(max_len+1):
            a.push(1) # oversize
    except Exception, e:
        print e

if __name__ == '__main__':
    main()
