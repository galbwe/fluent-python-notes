# Fluent Python Chapter 7
All about decorators
## Chapter Summary
### Intro
A decorator is shorthand for applying a higher order function that takes a function as an argument.
Ex: 
```python
@decorator
def func(*args, **kwargs):
    return "something"
```

is the same as 

```python
def func(*args, **kwargs):
    return "something"

func = decorator(func)
```
Decorators are run at *import time*, before any other functions are executed.
### Applications
#### Registries and composite strategy patterns
- Registry: a collection of funcions.
    - ex: views in a web framework
- Decorators can be used on functions to add them to a registry.
- Ex: best_promo strategy
    - Each promotion in a module is just a plain old python function. The func in a module is added to a registry
#### Memoization
- Use `@lru_cache` to cache arguments passed to a function and their returns values
- Useful when writing recursive functions with identical calls
- Small example: computing fibonnaci numbers
```python
    @functools.lru_cache()
    def fib(n):
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        return fib(n - 2) + fib(n - 1)
```
Calling without `lru_cache`, `fib(5)` makes the following number of calls with each argument:

| n | # calls to `fib(n)` |
|---|---------------------|
| 5 | 1                   |
| 4 | 1                   |
| 3 | 2                   |
| 2 | 3                   |
| 1 | 5                   |
| 1 | 3                   |

The duplicated calls use extra time. Using memoization, `fib` is called once with each argument, the result is stored in a dictionary (?), and an O(1) lookup is performed for each subsequent function call instead of calling `fib` again.

#### Generic Functions
- **Generic function**: a function whose implementation depends on the type of the argument passed


### Creating Your own decorators
#### Preliminaries
##### Variable scope rules
##### Closures
##### `nonlocal` keyword
#### Simple Decorator



## Discussion Questions
1. Anyone understand the quote at the beginning of the chapter about decorators deriving their names from compilers rather than the gang of four design pattern?
1. Where have people seen decorators used in practice?
    1. Memoizing recursive algorithms with `@lru_cache`
        - from the chapter
        - used in many places in math engine
    1. Implementing a dispatch function to simulate an overridden method with `@single_dispatch`. 
        - from math engine
        - used in math engine's `serialize.py`
    1. Binding views to urls in web frameworks
        - Ex: in flask you might see:
        ```python
        @app.get('/kittens', methods=['GET'])
        def get_kittens():
            <serve up some cute kittens>
        ```
    1. Patching using `unittest.mock`
    ```python
        @patch('views.get_kittens')
        def test_get_kittens_error_response(self, mock_get_kittens):
            mock_get_kittens.return_value = Response(400, ...)
            <handle the mocked error response>
    ```
    1. parametrizing tests in `pytest`
        ```python
        @pytest.mark.parametrize('arg1, arg2, arg3', [
            (1, 2, 3),
            (4, 5, 6), 
            (7, 8, 9)
        ])
        def test_something(arg1, arg2, arg3);
            <do the testing>
        ```
    1. Blanket error handling and logging on methods
        - *Disclaimer*: I'm not saying this is necessarily a good practice in all scenarios. 
        ```python
        def log_and_suppress_errors(f):
            @functools.wraps(f)
            def inner(*args, **kwargs):
                try:
                    return f(*args, **kwargs)
                except Exception as e:
                    logger.error(str(e))
            return inner

        @log_and_suppress_errors
        def some_function_without_error_handling(arg1, arg2):
            <do something without handling errors>
        ```
1. At a high level, how would you go about implementing each of the previous examples?
1. A point the author makes is that the decorators are run at import time, but he didn't really explain why this is significant. Does anyone have insights to add here?