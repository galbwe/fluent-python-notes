import math
from time import sleep

from utils import average_runtime


@average_runtime(1000)
def compare_is(a, b):
    return a is b


@average_runtime(1000)
def compare_equals(a, b):
    return a == b


class BinaryOperationGrid:
    def __init__(self, operation, objects):
        self.operation = operation
        self.objects = objects
        self.grid = [[None] * len(objects) for _ in objects]

    def populate(self):
        for i, x in enumerate(self.objects):
            for j, y in enumerate(self.objects):
                self.grid[i][j] = self.operation(x, y)

    def mean(self):
        return sum(sum(row) for row in self.grid) / len(self.grid) ** 2

    def stdev(self):
        n = len(self.grid) ** 2
        mean = self.mean() 
        return math.sqrt(sum(sum((x - mean) ** 2 for x in row) for row in self.grid) / (n - 1))

    def __repr__(self):
        return f'{self.__class__.__name__}(operation={self.operation})'

    def __str__(self):
        n = len(self.grid)
        return '\n'.join(' '.join(['{:>25}'] * n).format(*row) for row in self.grid)


class SlowEquals:
    def __init__(self, x):
        self.x = x

    def __eq__(self, other):
        sleep(0.001)
        return self.x == other.x


if __name__ == '__main__':
    a = b = SlowEquals(1)
    objects = [a, b, SlowEquals(2), SlowEquals(3), SlowEquals(3)]
    grid_1 = BinaryOperationGrid(compare_is, objects)
    grid_1.populate()
    print(str(grid_1))
    grid_2 = BinaryOperationGrid(compare_equals, objects)
    grid_2.populate()
    print(str(grid_2))
    print(grid_1.mean())
    print(grid_1.stdev())
    print(grid_2.mean())
    print(grid_2.stdev())
    