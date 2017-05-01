"""
Exercise R-2.12usesthe __mul__ method tosupport multiplyingaVector by a number, while Exercise R-2.14 uses the __mul__ method to support computing a dot product of two vectors. Give a single implementation of Vector. __mul__ that uses run-time type checking to support both syntaxes u*v and u*k, where u and v designate vector instances and k represents a number.
"""

class Vector:
    def __init__(self, d):
        if isinstance(d, list):
            self._coords = d
        else:
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

    def __mul__(self, other):
        if isinstance(other, Vector):
            if len(self) != len(other):
                raise ValueError('dimensions must agree')
            result = 0
            for i in range(len(self)):
                result += self[i] * other[i]
        elif isinstance(other, int):
            result = Vector(len(self))
            for i in range(len(self)):
                result[i] = self[i] * other
        else:
            raise TypeError('Unknown type')
        return result

    def __eq__(self, other):
        return self._coords == other._coords

    def __str__(self):
        return '<' + str(self._coords)[1:-1] + '>'

def main():
    print Vector([1,2,3,4,5]) * Vector([1,2,3,4,5])
    print Vector([1,2,3,4,5]) * 5

if __name__ == '__main__':
    main()
