import math


class Vector2d:
    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)

    def __repr__(self):
        return f'{self.__class__.__name__}(x={self.x},y={self.y})'

    def __str__(self):
        return f'<{self.x}, {self.y}>'

    def __iter__(self):
        return (element for element in (self.x, self.y))
    
    def __bytes__(self):
        pass

    def __eq__(self, other: 'Vector2d'):
        return self.x == other.x and self.y == other.y

    def __abs__(self):
        return math.sqrt(sum(e**2 for e in self))

    def __bool__(self):
        return abs(self) > 0