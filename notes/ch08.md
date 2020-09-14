# Chapter 8

Theme: distinction between objects and their names

## What is a variable
- Variables in Python are labels, not boxes
- Think of a variable as being assigned to an object
- Multiple variables can be assigned to the same object, which is called aliasing
    - Read assignments from right to left. Object is created first, then assignment is made
    - Ex: 
        ```python
            d1 = d2 = {}
            d2['a'] = 'b'
            print(d1)  # {'a': 'b'}
            print(d2)  # {'a': 'b'} 
        ```
- Variables are assigned to objects after the object is created.
    - Meant to reinforce the idea that objects exist independent of the variables assigned to them.
## Difference between `==` and `is`
- The `__eq__` operator compares the values of two variables, whereas the `is` operator compares their identities.
- The `is` operator is faster than `__eq__`, because it cannot be overloaded, so no special methods need to be invoked to evaluate it.
    - `equals_vs_is.py` has a contrived example

## Immutability
- Immutable objects like tuples contain references to other objects. If the reference points to a mutable object, then it may appear that the object is mutated when in actuality the variable is contains remains the same, and the object the variable points to is what actually changes.


## Copying
- *Shallow copy*: Duplicates the outer container, but the elements of this container are references to the same object held by the original. 
- Can make shallow copies of mutable objects by calling using the constructor
```python
x = [1, 2, 3]
x_copy = list(x)
print(x == x_copy)  # True
print(x is x_copy)  # False
```
- Can use `[:]` with lists to make a shallow copy
- *Deep copy*: Duplicate object that does not share references of embedded objects.
- ```python
    from copy import copy
    from copy import deepcopy
```
- can override the behavior of `copy` and `deepcopy` by implementing the `__copy__` and `__deepcopy__` magic methods.


## Mutable arguments to functions
- *Call by sharing*: Parameters in a Python function are aliases of the actual arguements.
    - Functions can change the data of any mutable object passed as a parameter, but cannot change the identity of that object.
- Mutable types as parameters defaults are usually a bad idea.
    - When used in `__init__` methods on a class the default object is shared between all instances of the class
    - Haunted Bus example
- Another gotcha: be careful not to alias mutable objects with an instance variable inside of a class.
    - Twilight bus example: an instance of `TwilightBus` changes the contents of `basketball_team`, even though logically it should not have
    acceess.
    - Workaround: make sure mutable arguments are copied at the begining of the function

## Garbage collection
- Objects that are referenced by no variables may be garbage collected.
    - The specific garbage collection algorithm depends on the implementation of python
    - [PyPy, Garbage Collection, and a Deadlock](https://emptysqua.re/blog/pypy-garbage-collection-and-a-deadlock/)
- The `del` keyword removes references to an object, not the object itself.


## Weak References
- *Weak Reference*: Reference to an object that does not increase its reference count for the purpose of garbage collection.
- Implemented in Python as a callable that returns the referenced object if it still exists in memory, and `None` otherwise.
- ```python
    import weakref
    x = {0, 1}
    wref = weakref.ref(x)
    ```
- Use weakref collections instead of directly instantiating weak referenece
    - `WeakValueDictionary`: mutable mapping where the values are weak references to objects.
        - Automatically removes keys from the dictionary when referenced objects are deleted elsewhere in the program.
        - commonly used for caching

- Many built-in python objects, like lists and dictionaries cannot be the target of a weak reference
    - workaround is to subclass these objects

## Python optimizations with immutables
- *Interning*: Sharing of string literals and small integers to avoid unnecessary duplication of objects in memory. 


# Discussion Questions:
1. Example 8-2 (with the Gizmos) worked for me in a terminal session, but not when I tried to write a test for it. Does anyone know what is going on? In brief, the following function returns `['a']` instead of what is shown in the terminal session. This is likely an issue with what the local scope is when `dir` is called.
    ```python
    def instantiate_gizmos():
        a = Gizmo()
        try:
            b = Gizmo() * 10
        except TypeError:
            return dir()
    ```
2. How would weak references be used in caching applications?
3. Got an error trying to add an int object to a `WeakValueDictionary`. What's going on here?
    - Second response to this [SO thread](https://stackoverflow.com/questions/9908013/weak-references-in-python) has the answer.