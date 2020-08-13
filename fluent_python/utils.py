from functools import wraps
from time import perf_counter


def average_runtime(n_trials):
    def decorator(f):
        @wraps(f)
        def inner(*args, **kwargs):
            nonlocal n_trials
            start = perf_counter()
            for _ in range(n_trials):
                f(*args, **kwargs)
            end = perf_counter()
            return (end - start) / n_trials
        return inner
    return decorator
        