"""
implement queue ADT by using two stacks. all queue operations execute in amortized O(1)
"""

class StackQueue():
    def __init__(self):
        self._stack1 = stack()
        self._stack2 = stack()

    def enque(self, e): # O(1)
        self._stack1.push(e)

    def deque(self): # O(n) / n deque operations = amortized O(1)
        if len(self._stack2) == 0:
            if len(self._stack1) == 0:
                raise Exception('no elements')

            for i in range(len(self._stack1)):
                self._stack2.push(self._stack1.pop())
        return self._stack2.pop()
