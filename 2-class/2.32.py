"""
Write a Python class that extends the Progression class so that each value in the progression is the square root of the previous value. (Note that you can no longer represent each value with an integer.) Your constructor should accept an optional parameter specifying the start value, using 65,536 as a default
"""

import math

class Progression(object):
    def __init__(self, start=0):
        self._current = start

    def _advance(self):
        self._current += 1

    def next(self):
        if self._current is None:
            raise StopIteration()
        else:
            answer = self._current
            self._advance()
            return answer

    def __iter__(self):
        return self

    def print_progression(self, n):
        print(' '.join(str(next(self)) for j in range(n)))

class SquareRootProgression(Progression):
    def __init__(self, start=65536):
        super(SquareRootProgression, self).__init__(start)

    def _advance(self):
        self._current = math.sqrt(self._current)

def main():
    d = SquareRootProgression()
    d.print_progression(5)

if __name__ == '__main__':
    main()
