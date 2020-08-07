from collections import defaultdict
from itertools import chain
import functools


def count_calls(dictionary):
    """Decorator that registers function calls in a dictionary"""
    def decorator(f):
        if f.__name__ not in dictionary:
            dictionary[f.__name__] = 0
        functools.wraps(f)
        def call(*args, **kwargs): 
            dictionary[f.__name__] += 1 
            return f(*args, **kwargs)
        return call
    return decorator


def count_calls_by_signature(dictionary):
    def decorator(f):
        if f.__name__ not in dictionary:
            dictionary[f.__name__] = defaultdict(lambda: 0)
        functools.wraps(f)
        def call(*args, **kwargs):
            key = '(' + ', '.join(chain((str(arg) for arg in args), sorted(f'{k}={v}' for k, v in kwargs.items()))) + ')'
            dictionary[f.__name__][key] += 1
            return f(*args, **kwargs)
        return call
    return decorator
