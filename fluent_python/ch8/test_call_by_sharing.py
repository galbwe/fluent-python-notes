from .call_by_sharing import append_three

def test_append_three():
    x = [1, 2]
    append_three(x)
    assert x == [1, 2, 3]
