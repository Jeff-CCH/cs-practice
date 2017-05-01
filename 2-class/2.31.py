"""
Write a Python class that extends the Progression class so that each value in the progression is the absolute value of the difference between the pre- vious two values. You should include a constructor that accepts a pair of numbers as the first two values, using 2 and 200 as the defaults
"""

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

class DiffProgression(Progression):
    def __init__(self, start1=2, start2=200):
        super(DiffProgression, self).__init__(start1)
        self._current2 = start2

    def _advance(self):
        self._current, self._current2 = self._current + self._current2, self._current

def main():
    d = DiffProgression()
    d.print_progression(5)

if __name__ == '__main__':
    main()
