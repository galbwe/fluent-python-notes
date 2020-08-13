import weakref
from weakref import WeakValueDictionary

import pytest


def test_weak_reference_to_deleted_object():
    x = {0, 1}
    wref = weakref.ref(x)
    assert wref() is x
    x = (2, 3)
    assert wref() is None 


def test_weak_reference_to_live_object():
    x = {0, 1}
    wref = weakref.ref(x)
    y = x
    x = (2, 3)
    assert wref() is y
    del y
    assert wref() is None


def test_weak_value_dictionary():
    class Person:
        def __init__(self, name):
            self.name=name

        def __repr__(self):
            return self.name
        
    a, b, c, = Person('Alice'), Person('Bob'), Person('Charlie')
    wvd = WeakValueDictionary()
    wvd[str(a)] = a
    wvd[str(b)] = b
    wvd[str(c)] = c
    assert sorted(wvd.keys()) == sorted(['Alice', 'Bob', 'Charlie'])
    del a
    assert sorted(wvd.keys()) == sorted(['Bob', 'Charlie'])


def test_weak_dictionary_does_not_work_with_list():
    wvd = WeakValueDictionary
    x = [1, 2, 3]
    with pytest.raises(TypeError):
        wvd[str(x)] = x