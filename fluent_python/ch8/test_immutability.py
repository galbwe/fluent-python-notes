import pytest


def test_assignment_to_tuple_element_raises_error():
    t = ('a', 'b', 'c', [1, 2])
    with pytest.raises(TypeError):
        t[3] = [*t[3], 4]
    with pytest.raises(TypeError):
        t[0] = 1


def test_mutating_tuple_element_is_fine():
    t = ('a', 'b', 'c', [1, 2])
    id_before_appending = id(t[-1])
    t[3].append(4)
    assert t == ('a', 'b', 'c', [1, 2, 4])
    assert id(t[-1]) == id_before_appending


def test_spread_operator_copies_list():
    x = [1, 2, 3]
    y = x[:]
    assert x == y
    assert x is not y


