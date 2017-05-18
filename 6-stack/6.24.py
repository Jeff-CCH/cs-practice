"""
implement a stack ADT by using a single queue and a constant additional local memory
"""

class stack:
    def __init__(self):
        self._q = queue()

    def push(self, e): # O(1)
        self._q.enque(e)

    def pop(self): # O(n)
        for i in range(len(self._q-1)):
            self.enque(self._q.deque())
        return self._q.deque()

    def top(self): # O(n)
        val = None
        for i in range(len(self._q)):
            if i == self._q - 1:
                val = self._q.first()
            self.enque(self._q.deque())
        return val
