import math
import pytest

from .vector import Vector, ShortVector


class TestVector:
    @pytest.fixture
    def vec_1(self):
        return Vector([3, 4])
    @pytest.fixture
    def vec_2(self):
        return Vector([3, 4])
    @pytest.fixture
    def vec_3(self):
        return Vector([5, 12])
    @pytest.fixture
    def vec_len_3(self):
        return Vector([1, 2, 3])
    @pytest.fixture
    def zero_vec(self):
        return Vector([0, 0])
    @pytest.fixture
    def null_vec(self):
        return Vector([])

    def test_iter(self, vec_1, vec_len_3):
        assert [e for e in vec_1] == [3, 4]
        assert [e for e in vec_len_3] == [1, 2, 3]

    def test_abs(self, vec_1, vec_len_3):
        assert abs(vec_1) == 5.0
        assert abs(vec_len_3) == math.sqrt(14)

    def test_eq(self, vec_1, vec_2, vec_3, vec_len_3):
        assert vec_1 is not vec_2
        assert vec_1 == vec_2
        assert vec_1 != vec_3
        assert vec_len_3 == vec_len_3
        assert vec_1 != vec_len_3

    def test_bool(self, vec_1, zero_vec, vec_len_3):
        assert bool(vec_1) is True
        assert bool(zero_vec) is False
        assert bool(vec_len_3) is True

    def test_frombytes(self, vec_1, vec_len_3):
        octets = bytes(vec_1)
        v2 = Vector.frombytes(octets)
        assert v2 == vec_1

        octets = bytes(vec_len_3)
        vl3 = Vector.frombytes(octets)
        assert vl3 == vec_len_3

    def test_len(self, vec_1, vec_len_3, null_vec):
        assert len(vec_1) == 2
        assert len(vec_len_3) == 3
        assert len(null_vec) == 0

    def test_get_item_by_index(self, vec_1):
        assert vec_1[0] == 3
        assert vec_1[1] == 4
        assert vec_1[-1] == 4
        assert vec_1 [-2] == 3
        with pytest.raises(IndexError):
            vec_1[2]

    def test_slicing(self, vec_len_3):
        assert vec_len_3[:-1] == Vector([1, 2])
        assert vec_len_3[1:] == Vector([2, 3])
        assert vec_len_3[:] == Vector([1, 2, 3])
        assert vec_len_3[1:-1] == Vector([2])
        assert vec_len_3[1:1] == Vector([])
        assert vec_len_3[1:4] == Vector([2, 3])
        with pytest.raises(TypeError):
            vec_len_3['index']


class TestShortVector:
    @pytest.fixture
    def short_vec_1(self):
        return ShortVector([1/11, 1/27])
    
    def test_bytes(self, short_vec_1):
        assert len(bytes(short_vec_1)) == 9

