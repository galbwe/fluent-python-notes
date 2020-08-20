# Chapter 9: Pythonic objects

## Class and static methods
- `@classmethod`: method of a class that depends on class attributes, but not instance attributes
    - can be used to create alternative constructors
        - `frombytes`, `fromdict`, etc.
- `@staticmethod`: method of a class that is independent of all class and instance attributes
    - Luciano doesn't like staticmethod

## Private and protected attributes
- variable/method names with a leading underscore are understood to be private
- a double underscore in a variable name *mangles* that variable name
    - Ex: `__x` and `__y` are instance variables of the `Vector2d` class
    - ```python
        In [6]: from ch9.vector import Vector2d
        In [7]: v = Vector2d(3, 4)
        In [8]: dir(v)
        Out[8]: 
            ['_Vector2d__x',
            '_Vector2d__y',...]    
    ```
    Internally, these variables names are changed to reflect the class that defined them.
- Prevents a programmer from accidentally clobbering a variable name
- Does not prevent a programmer from intentionally changing a variable name by using the mangled name

## `__format__` magic method
    - two ways to use `format` method:
        - `format(obj, format_spec)`
        - `str.format`
    - [Format specification mini language](https://docs.python.org/3/library/string.html#formatspec)
    - [Format string syntax](https://docs.python.org/3.8/library/string.html#format-string-syntax)
    - Each class can extend the format specification mini language

## `__hash__` method and immutability
    - to make an object immutable, thus making it possible to hash it, make its attributes read only properties
        ```python
        @property
        def x(self):
            return self.__x
        ```
    - when defining a `__hash__` method on an object with multiple attributes, combine the hashes of the individual attributes with the bitwise or operator `^`
        ```python
        def __hash__(self):
            return hash(self.x) ^ hash(self.y)
        ```

## `__slots__` magic method
    - `__slots__` allows instance variables to be stored as a tuple istead of dictionary
    - sequence of strings with the names of the variables to be stored
    - must declare every instance variable in slots
        - passing `"__dict__"` to slots will store other instance variables in a dictionary
    - Must declare `"__weakref__"` for instances to be targets of weak references
    - Pros:
        - Saves memory
        - Makes programs faster
    - Cons:
        - Must redeclare `__slots__` in every subclass, it is not inherited
        - must duplicate declaration of instance variables in slots and assignment of instance variables
    - `__slots__` is an optimization, and should only be used once performance has been benchmarked to validate using it


## Overriding class attributes
    - In python, class attributes can be used as default values for instance attributes
    - Can change the behavior of a subclass by overriding class variables
    - Often, this is the only thing a subclass does
    - Example from [Django docs](https://docs.djangoproject.com/en/3.1/topics/class-based-views/#subclassing-generic-views)
        - ```python
        from django.views.generic import TemplateView

        class AboutView(TemplateView):
            template_name = "about.html"
        ```

## Reading Questions
1. What is going on with the implementation of `__bytes__` for the `Vector2d` class?
    `ord` : converts a single unicode character into an integer representation
2. Luciano says that if you are using a static method on a class, then you may as well have defined it as a module level function. Is there another way to view static methods that makes is reasonable to include them in the body of a class?
    - from footnote: [blog post](https://julien.danjou.info/guide-python-static-class-abstract-methods/)