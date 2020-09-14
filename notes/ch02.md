# Overview of Built in sequences
## Two was to categorize sequences
### flat sequences vs. container sequences
The elements of a flat sequence are of a uniform datatype. The directly store their elements in their allocated memory.
    - ex: `str`, `byte`, `bytearray`, 'memoryview`, `array.array`
Container sequences can hold elements of different types. They do not hold their elements, but instead hold references to their elements.
    - ex: `list`, `tuple`, `collections.deque`
### Mutable vs. Immutable sequences
Mutable sequences can be modified in place
## Sequence class hierarchy
(not actual source code)
```python
class Container:
    def __contains__(self):
        '''implements the 'in' keyword'''
        pass

class Iterable:
    def __iter__(self):
        '''implements iteration (for loops, list comprehensions, etc)'''

class Sized:
    def __len__(self):
        '''returns the number elements of a sequence'''

class Sequence(Container, Iterable, Sized):
    def __getitem__(self, i):
        '''returns item at an index'''
    
    def __reversed__(self):

    def index(self, x):
        '''returns first index of the given element'''

    def count(self, x):
        '''returns number of occurences of x in sequence'''

class MutableSequence(Sequence):
    def __setitem___(self, i):
        '''allows assignment to an index'''

    def __delitem___(self, i):
        '''removes an item at an index from memory using 'del' keyword'''

    def insert(self, i, x):
        '''inserts element x at index i'''

    def append(self, x):
        '''appends x to end of sequence'''

    def reverse(self, x):
        '''reverses sequence in place'''

    def extend(self, other):
        '''appends elements of other to the end of sequence'''

    def pop(self):
        '''removes last element of sequence and returns it'''

    def remove(self):
        '''removes last element of the sequence'''

    def __iadd__(self):
        '''concatenates two sequences'''
```

# Comprehensions
## motivation
 - listcomps are arguable more readable than their for loop equivalents
 - they are definitely more readable than map and filter
## nested loop equivalents in comprehensions
 - multiple for clauses in a comprehension appear in the same order that they would in a for loop
## Generator expressions
 - genexps yield one element at a time instead of building an entire list before using its entries one by one. This can save memory.
 - they can be passed to a contstructor without parenthesis if they are the only argument. Otherwise, parenthesis are required.
    `tuple(x**2 for x in range(3))` vs `array.array('I', (x**2 for x in range(3)))`

# Uses for tuples
## records
 - tuples can be used as records without keys
 ### named tuples
 - lightweight record class
 - field names are stored in the class, so they take up the same amount of memory as a tuple
 - methods
   - `_fields` : tuple of field names
   - `_make` : instantiate from an iterable
   - `_asdict` : convert to ordered dict

## tuple unpacking
```python
a, b = (1, 2)
a, b, *rest = (1, 2, 3, 4, 5)
```
### nested tuple unpacking
```python
t = (1, 2, (3, 4))
a, b, (c, d) = t
```

## comparisons between tuples and lists
- rule of thumb: a tuple has any method a list has which does not involve inserting or deleting elements
- exception: `tuple` has not `__reversed__` method, but `__reversed__` can still be called on it

# Slicing
## Reasons slices exclude the element at the last index
- easy to compute length of the sequence from the indices
    - literally the last index when it is the only thing given
    - `stop - start` when both specified
- it makes it easier to split a sequence at an index
    ```python
        left, right = sequence[:i], sequence[i:]
    ```
## Slice Objects
- slice syntax is supported by `slice` objects behind the scenes
    - trick: use named slices to index into a sequence
    ```python
        >>> t = (0, 1, 2, 3, 4, 5)
        >>> evens = slice(0, len(t), 2)
        >>> t[evens]
        (0, 2, 4) 
    ```
## Multidimensional slicing
- syntax: `a[i:j, k:l]`
- implemented by passing a tuple to `__getitem__` and `__setitem__`
- elipsis: shorthand for "use full in the remaining dimensions"
    - `a[1:2, ...] == a[1:2, :, :, :]` if a is 4 dimensional
    - `...` is created with the `Ellipsis` singleton object
## Assigning to slices
- can overwrite an entire slice of a sequence by assigning an iterable
    - `l[3:5] = [7]`
    - iterable does not have to be the same length as the slice, unless a stride parameter is used
# Concatenation operators with sequences
- the * operator
    - the `*` operator concatenates multiple copies of the *same object*
    - it creates a new sequence
    - tic tac toe board example
        - implementation 1:
        ```python
            board = [['_'] * 3 for i in range(3)]
        ```
        - implementation 2:
        ```python
            board = [['_'] * 3] * 3
        ```
        - in implementation 2, all of the elements of the outer list are references to the same innner list.
        - implementation 1 on the other hand uses a list comprehension, which creates a new list instance for each element of the outer list
# Augmented assignment operators with sequences
- `+=` is implemented with `__iadd__`, and uses `__add__` as a fallback
- whether or not the operation is performed in place depends on whether `__iadd__` is implemented
    - if `__iadd__` implemented, then object modified in place
    - if `__add__` used as fallback, then the operation is not done in place. `a += b` does:
        1. compute `a + b` and assign it to a new object
        2. bind the new object to `a`
- synonomous with `*=` and `__imul__`
- mutable sequences implement `__imul__`, so do in place concatenation
- immutable sequences do not implement `__imul__`, so `*=` is not an inplace operation
```python
>>> l = [1, 2, 3]
>>> id(l)
4365065104
>>> l *= 2
>>> l
[1, 2, 3, 1, 2, 3]
>>> id(l)
4365065104
>>> t = (1, 2, 3)
>>> id(t)
4364359792
>>> t *= 2
>>> t
(1, 2, 3, 1, 2, 3)
>>> id(t)
4365104976
```

# Sorting
- ```sorted``` magic method returns a new sorted sequence
- ```sort``` method operates in place and returns `None`
- two important parameter are `key` and `reverse`

# Searching
- `bisect.bisect` searces a sorted sequence using binary search.
- returns an index where the element can be inserted to maintain the sequence in sorted order
    - by default, `bisect` inserts at the largest available index`
    - `bisect.bisect_left` inserts at the smallest available index
        - consequently, `l[bisect.bisect_left(l, x)] == x`
- application, assign numerical elements of a list to a category
- `bisect.insort` inserts an element into a sorted list while maintaining the sorted order of its elements

# Other sequences
There are other sequence types which are more memory efficient than a list, or offer more efficient append and pop operations
## Arrays
- More memory efficient than a list because they contain the bytes representations of their elements directly in their allocated memory.
- Arrays have a typecode, which is a string representing the uniform data type of its elements
    - ex: 'f' is for double precision float
## Memory Views
- Sequence that allows slicing without copying elements from the original array into the slice.
- Important for large datasets
- `memoryview.cast` method returns a new memoryview which shares the same memory
- inspired by numpy and scipy
## Numpy / Scipy
- Numpy and scipy are built on top of optimized C and Fortran libraries from the Netlib repository
## Deques
- lists `pop` and `append` operations can be inefficient because the array may need to be reindexed
- `deque`s are double ended queues optimized for inserting and removing from the ends
- they are thread safe
- from `collections` module
- `maxlen` parameter to constructor sets maximum number of elements
- implements most list methods, but adds methods like `rotate, popleft, extendleft, appendleft`
### other queue sequences
- `queue` contains synchronized, blocking versions of a `deque`. 
    - classes: `Queue`, `LifoQueue`, `PriorityQueue`
    - when shared between threads and at max length, insertion operation on one thread will block until another thread removes an element 
- `multiprocessing` and `asyncio` implement their own `Queue` classes
- `heapq` implements a heap
    - a *heap* is a tree datastructure that always stores the element with the minimum (maximum) value at the root
    - They are used to implement *priority queues*, where the first element out has the highest priority

# Things to discuss
- Point about tuple not having a `reversed` method
> `tuple` supports all `list` methods that do not involve adding or removing items, with one exception- tuple lacks the `__reversed__` method. However that is just for optimization; `reversed(my_tuple)` works without it
- naming slices and then using them was really cool
- tic tac toe board example
- assignment puzzle

        ```python
        t = (1, 2, [3, 4])
        t[2] += [50,60]
        ```

    - why does the last line both raise a type error and perform the assignment?
    - takeaways:
        1. putting mutable items in tuples is not a good idea
        2. Augmented assignment is not an atomic operation
- difference between `bisect` and `bisect_left`
- binning application for `bisect`
- question for the group: has anyone ever actually had to use an array or a memoryview?
    - where might they be useful in data science?
- there is a comment about deques being thread safe. Is this a concern with lists?
- anyone know what a heap is?