from copy import copy, deepcopy

import pytest


mutable_constructors = [
    (list, [1, 2, 3]),
    (dict, {'a': 1, 'b': 2}),
    (set, {1, 2, 3}),
]


@pytest.mark.parametrize('constructor, obj', mutable_constructors)
def test_mutable_constructors_create_different_object(constructor, obj):
    copy = constructor(obj)
    assert copy == obj
    assert copy is not obj


@pytest.mark.parametrize('constructor, obj', [
    (tuple, (1, 2, 3)),
    (tuple, (1, 2, ['a', 'b'])),
    (frozenset, frozenset([1, 2, 3]))
])
def test_immutable_constructors_create_identical_object(constructor, obj):
    copy = constructor(obj)
    assert copy == obj
    assert copy is obj
    assert id(copy) == id(obj)


def test_list_constructor_makes_shallow_copy():
    x = ['a', ['b']]
    y = list(x)
    assert x is not y
    assert x[1] is y[1]


def test_spread_operator_makes_shallow_copy():
    x = ['a', ['b']]
    y = x[:] 
    assert x is not y
    assert x[1] is y[1]


def test_shallow_copy_can_mutate_original_object():
    x = {'a': [1, 2, 3]}
    y = dict(x)
    y['a'].append(4)
    assert x == {'a': [1,2,3,4]}


def test_copy_makes_shallow_copy():
    x = ['a', {1, 2}]
    y = copy(x)
    assert x[1] is y[1]


def test_deepcopy_does_not_make_shallow_copy():
    x = ['a', {1, 2}]
    y = deepcopy(x)
    assert x[1] is not y[1]