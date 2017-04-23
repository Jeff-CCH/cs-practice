"""
In Section 2.3.3, we note that our Vector class supports a syntax such as
v = u + [5,3,10,-2,1], in which the sum of a vector and list returns a new vector. However, the syntax v = [5,3,10,-2,1] + u is illegal.
Explain how the Vector class definition can be revised so that this syntax gener
ates a new vector
"""

class Vector:
    def __init__(self, d):
        self._coords = [0] * d

    def __len__(self):
        return len(self._coords)

    def __getitem__(self, j):
        return self._coords[j]

    def __setitem__(self, j, val):
        self._coords[j] = val

    def __add__(self, other):
        if len(self) != len(other):
            raise ValueError('dimensions must agree')
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] + other[j]
        return result

    def __radd__(self, other):
        if len(self) != len(other):
            raise ValueError('dimensions must agree')
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] + other[j]
        return result

    def __eq__(self, other):
        return self._coords == other._coords

    def __ne__(self, other):
        return not self == other

    def __str__(self):
        return '<' + str(self._coords)[1:-1] + '>'

def main():
    v1 = Vector(5)
    print v1 + [5,3,10,-2,1]
    print [5,3,10,-2,1] + v1

if __name__ == '__main__':
    main()
