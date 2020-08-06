# Overview of Mapping Types
## Generic Mapping Types
## What does Hashable Mean?
A class `Obj` is hashable if the following three conditions hold:
1. `Obj` has an `__eq__` method
1. `Obj` has a `__hash__` method
1. for any two instances `obj_1` and `obj_2`, `obj_1 == obj_2` implies `hash(obj_1) == hash(obj_2)`.

Only hashable types can be used as keys in a dictionary or set
### Examples of hashables:
- Strings
    ```python
    >>> s1 = 'Hello'
    >>> hash(s1)
    -5687802805300295550
    >>> s2 = 'Hello'
    >>> hash(s2)
    -5687802805300295550
    ```
- ints
    ```python
    >>> i1, i2 = 324, 324
    >>> hash(i1), hash(i2)
    (324, 324)
    ```
- tuples whose elements are hashable
    ```python
    >>> t1, t2 = (1, 2), (1, 2)
    >>> hash(t1), hash(t2)
    (3713081631934410656, 3713081631934410656)
    ```
- frozensets
    ```python
    >>> f1, f2 = frozenset({1, 2}), frozenset({1, 2})
    >>> hash(f1), hash(f2)
    (-1826646154956904602, -1826646154956904602)
    ```
- User defined types are (trivially) hashable by default because they have `__hash__` methods, and no two instances compare equal using the default `__eq__` method
    ```python
    >>> class A:
    ...     def __init__(self, a):
    ...             self.a = a
    ... 
    >>> a1, a2 = A(42), A(42)
    >>> a1 == a2
    False
    >>> hash(a1), hash(a2)
    (270728021, 270728029)
    ```
### Nonexamples
- lists
    ```python
    >>> hash([1,2,3])
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    TypeError: unhashable type: 'list'
    ```
- dicts
    ```python
    >>> hash({'a': 1, 'b': 2})
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    TypeError: unhashable type: 'dict'
    ```
- tuples that contain an unhashable element
    ```python
    >>> hash(('a', 1, [2, 3]))
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    TypeError: unhashable type: 'list'
    ```
- sets
    ```python
    >>> hash(set([1, 2]))
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    TypeError: unhashable type: 'set'
    ```
## Dict comprehensions
Yeah, these exist ...
# Common Dictionary Methods
- `__contains__` : `k in d`
- `__delitem__` : `del d[k]`
- `d.get`
- `__getitem__` : `d[k]`
- `d.items`
- `d.keys`
- `d.values`
- `__len__`
- `__setitem__` : `d[k] = v`
## Methods I don't frequently use or didn't know about
- `d.clear`
    ```python
    >>> d = {'a': 1, 'b': 2}
    >>> d.clear()
    >>> d
    {}
    ```
- `d.fromkeys`
    ```python
    >>> dict.fromkeys(['a', 'b', 'c'], 42)
    {'a': 42, 'b': 42, 'c': 42}
    ```
- `__missing__`
    - called whenever `__getitem__` cannot find a key 
    ```python
    >>> class MyDict(dict):
    ...     def __missing__(self, k):
    ...             self[k] = 'missing'
    ...             return 'missing'
    ... 
    >>> d = MyDict([('a', 1), ('b', 2)])
    >>> d
    {'a': 1, 'b': 2}
    >>> d['a']
    1
    >>> d['c']
    'missing'
    >>> d
    {'a': 1, 'b': 2, 'c': 'missing'}
    ```
- `d.update`
    ```python
    >>> d = {'a': 1, 'b': 2}
    >>> d.update({'c': 3})
    >>> d
    {'a': 1, 'b': 2, 'c': 3}
    >>> d.update([('d', 4)])
    >>> d
    {'a': 1, 'b': 2, 'c': 3, 'd': 4}
    ```
## Handling missing keys
### Setdefault method
- `dict.setdefault` looks for a key in `dict`. If it finds the key, it returns the corresponding dictionary value. If it does not find the key, it sets the key's value to a default value, and returns the default.
    ```python
    >>> d = {'a': 1, 'b': 2}
    >>> d
    {'a': 1, 'b': 2}
    >>> d.setdefault('b', 'X')
    2
    >>> d
    {'a': 1, 'b': 2}
    >>> d.setdefault('c', 'X')
    'X'
    >>> d
    {'a': 1, 'b': 2, 'c': 'X'}
    ```
### defaultdict
- `collections.defaultdict` achieves similar behavior to `setdefault`. The primary difference is in where the default return value is set. In `defaultdict`, it is set in the constructor by specifiying a factory method that is called with no arguments to fill in the missing value.
    ```python
    >>> import collections
    >>> d = collections.defaultdict(list)
    >>> d['a'].append(1)
    >>> d
    defaultdict(<class 'list'>, {'a': [1]})
    ```
### the __missing__ method
- `__missing__` is called whenever the key arguement to `__getitem__` cannot be found
- This method is overriden to give `defaultdict` its behavior
# Variations of `dict` in the Standard Library
## The collections module
### OrderedDict
A dictionary that imposes an ordering on the keys. Includes a `popitem` method.
- Use cases:
### ChainMap
- Holds a sequence of mappings that can be searched as one. If a key is found in multiple mappings, the corresponding value from the first mapping in the sequence is returned.

    ```python
    >>> cm = collections.ChainMap(
            {'a': 1, 'b': 2},
            {'b': 3, 'c': 4},
            {'c': 5, 'd': 6})
    >>> cm['a']
    1
    >>> cm['b']
    2
    >>> cm['c']
    4
    >>> cm['d']
    6
    ```
- Use cases:
    - scoping
        - rule prioritization from Pearson ME
### Counter
Holds an integer count for each key. Updating a key updates that key's count.
### UserDict
Preferable to subclass `collections.UserDict` over `dict`
- has a dict attribute called data
- kind of hand waived the explanation for now, said it 
## Immutable Mappings
`types.MappingProxyType` creates a proxy for a mapping which blocks direct use of `__setitem__`, effectively giving you an immutable dict
# Sets and frozensets
- Like dicts, but without the values. 
- Watch out when using literal syntax. Curly braces alone create a dict, not a set.
- frozenset is an immutable set
# Dict internals
- Dicts are hash tables
    - a dict hash table is a collection of buckets
    - each bucket has a reference to a key, and a reference to that item's valued = 
## Efficiency
On average constant time lookups
## Hash table implementation of dicts
## Practical consequences for working with dicts
### keys must be hashable
### dicts are memory heavy
### lookups in dicts is fast
### dict key ordering depends on insertion order
### adding items to a dict may change its ordering

# Questions and salient points
- Are there any built in types that have `__hash__` and `__eq__` methods, but are not hashable? (i.e. `a == b` but `hash(a) != hash(b)` for some instances)
- The statement that user defined objects have hashes that are equal to their id is not true:
    - How are default hashes actually computed for user defined objects?
- What are the drawbacks of using `collections.OrderedDict` all the time?
- What is the deal with `dis.dis`?