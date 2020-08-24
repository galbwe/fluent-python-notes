import math
from array import array
from functools import reduce
from operator import or_
from typing import Iterable


class Vector:
    typecode = 'd'  # needed to convert to/from bytes

    def __init__(self, components: Iterable):
        self._components = array(self.typecode, components)

    def __repr__(self):
        return f'{self.__class__.__name__}(' + ','.join(iter(self._components)) + ')'

    def __str__(self):
        return f'<' + ','.join(iter(self._components)) + '>'

    def __hash__(self):
        hashes = [hash(c) for c in self._components]
        return reduce(or_, hashes)

    def __iter__(self):
        return iter(self._components)
    
    def __bytes__(self):
        return (bytes([ord(self.typecode)]) +
            bytes(array(self.typecode, self)))

    def __eq__(self, other: 'Vector2d'):
        return all(c1 == c2 for (c1, c2) in zip(self._components, other._components)) 

    def __abs__(self):
        return math.sqrt(sum(e**2 for e in self))

    def __bool__(self):
        return abs(self) > 0

    @classmethod
    def frombytes(cls, octets):
        typecode = chr(octets[0])
        memv = memoryview(octets[1:]).cast(typecode)
        return cls(memv)


class ShortVector(Vector):
    typecode = 'f'