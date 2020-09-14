import math
import itertools
from array import array
from functools import reduce
from operator import xor
from typing import Iterable, Union
import numbers


class Vector:
    typecode = 'd'  # needed to convert to/from bytes
    shortcut_names = 'xyzt'

    def __init__(self, components: Iterable):
        self._components = array(self.typecode, components)

    def __repr__(self):
        return f'{self.__class__.__name__}(' + ', '.join((str(c) for c in self._components)) + ')'

    def __str__(self):
        return f'<' + ', '.join((str(c) for c in self._components)) + '>'

    def __iter__(self):
        return iter(self._components)

    def __bytes__(self):
        return (bytes([ord(self.typecode)]) +
            bytes(array(self.typecode, self)))

    def __eq__(self, other: 'Vector2d'):
        return all(c1 == c2 for (c1, c2) in zip(self._components, other._components))

    def __hash__(self):
        hashes = map(hash, self._components)
        return reduce(xor, hashes, 0)

    def __abs__(self):
        return math.sqrt(sum(e**2 for e in self))

    def __bool__(self):
        return abs(self) > 0

    def __len__(self):
        return len(self._components)

    def __getitem__(self, index: Union[numbers.Integral, slice]):
        if isinstance(index, numbers.Integral):
            return self._components[index]
        elif isinstance(index, slice):
            return Vector(self._components[index])
        else:
            raise TypeError(f'Invalid input to __getitem__ {index} of type {type(index)}.')

    @property
    def _lookup_index(self):
        return dict(
            zip(self.shortcut_names, range(len(self._components))))

    def __getattr__(self, attr: str) -> float:
        cls = type(self)
        if attr in set(cls.shortcut_names):
            try:
                return self._components[self._lookup_index[attr]]
            except KeyError:
                raise AttributeError
        return super().__getattr__(attr)

    def __setattr__(self, attr: str, value) -> None:
        cls = type(self)
        if attr in set(cls.shortcut_names):
            self._components[self._lookup_index[attr]] = value
        else:
            super().__setattr__(attr, value)

    # unary operators
    def __pos__(self):
        return Vector(self)

    def __neg__(self):
        return Vector(-x for x in self)

    # infix operators
    def __add__(self, other):
        # return self._add_fluent_python_version(other)
        try:
            return self._add_my_version(other)
        except TypeError:
            return NotImplemented

    def _add_my_version(self, other):
        return Vector([
            x + y
            for (x,y) in zip(self, other)
        ] + [
            y for y in other[len(self):]
        ] + [
            x for x in self[len(other):]
        ])

    def _add_fluent_python_version(self, other):
        pairs = itertools.zip_longest(self, other, fillvalue=0.0)
        return Vector(a + b for (a, b) in pairs)

    def __radd__(self, other):
        return self + other

    def __mul__(self, scalar):
        if not isinstance(scalar, numbers.Real):
            return NotImplemented
        return Vector([x * scalar for x in self])

    def __rmul__(self, scalar):
        return self * scalar





    @classmethod
    def frombytes(cls, octets):
        typecode = chr(octets[0])
        memv = memoryview(octets[1:]).cast(typecode)
        return cls(memv)


class ShortVector(Vector):
    typecode = 'f'