import pytest
from .variable_assignment import instantiate_gizmos

def test_instantiate_gizmo():
    d = instantiate_gizmos()
    assert 'a' in d
    assert 'Gizmo' in d # this fails
    assert 'b' not in d # this also fails


def test_aliases_have_same_id():
    a = b = []
    assert id(a) == id(b)
    assert a is b


def test_comparators_for_distinct_objects_with_same_data():
    a = {'name': 'Edgar', 'age': 34}
    b = {'name': 'Edgar', 'age': 34}
    assert a == b
    assert a is not b
    assert id(a) != id(b) 