from array import array
import math


class Vector:
    typecode = 'd'  # needed to convert to/from bytes

    def __init__(self, x, y):
        self.__x = float(x)
        self.__y = float(y)

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    def __repr__(self):
        return f'{self.__class__.__name__}(x={self.x},y={self.y})'

    def __str__(self):
        return f'<{self.x}, {self.y}>'

    def __hash__(self):
        return hash(self.x) ^ hash(self.y)

    def __iter__(self):
        return (element for element in (self.x, self.y))
    
    def __bytes__(self):
        return (bytes([ord(self.typecode)]) +
            bytes(array(self.typecode, self)))

    def __eq__(self, other: 'Vector2d'):
        return self.x == other.x and self.y == other.y

    def __abs__(self):
        return math.sqrt(sum(e**2 for e in self))

    def __bool__(self):
        return abs(self) > 0

    @classmethod
    def frombytes(cls, octets):
        typecode = chr(octets[0])
        memv = memoryview(octets[1:]).cast(typecode)
        return cls(*memv)


class ShortVector(Vector):
    typecode = 'f'