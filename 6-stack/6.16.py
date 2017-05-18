"""
Modify the ArrayStack implementation so that the stack's capacity is limited to maxlen elements, where maxlen is an optional parameter to the constructor (that defaults to None). If push is called when the stack is at full capacity, throw a Full exception (defined similarly to Empty)
"""

class ArrayStack:
    def __init__(self, max_len=None):
        self._data = []
        self._max_len = max_len

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return len(self._data) == 0

    def push(self, e):
        if self._max_len is not None:
            if self._max_len == len(self):
                raise Exception('stack is full')
        self._data.append(e)

    def otp(self):
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data[-1]

    def pop(self):
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data.pop()

def main():
    try:
        a = ArrayStack(max_len=10)
        for i in range(11):
            a.push(i)
            print 'push {0}'.format(i)
    except Exception, e:
        print e

if __name__ == '__main__':
    main()
