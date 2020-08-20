import math
import pytest

from .vector import Vector2d, ShortVector2d


class TestVector2d:
    @pytest.fixture
    def vec_1(self):
        return Vector2d(3, 4)
    @pytest.fixture
    def vec_2(self):
        return Vector2d(3, 4)
    @pytest.fixture
    def vec_3(self):
        return Vector2d(5, 12)
    @pytest.fixture
    def zero_vec(self):
        return Vector2d(0, 0)

    def test_iter(self, vec_1):
        assert [e for e in vec_1] == [3, 4]

    def test_abs(self, vec_1):
        assert abs(vec_1) == 5.0

    def test_eq(self, vec_1, vec_2, vec_3):
        assert vec_1 is not vec_2
        assert vec_1 == vec_2
        assert vec_1 != vec_3

    def test_bool(self, vec_1, zero_vec):
        assert bool(vec_1) is True
        assert bool(zero_vec) is False

    def test_frombytes(self, vec_1):
        octets = bytes(vec_1)
        v2 = Vector2d.frombytes(octets)
        assert v2 == vec_1


class TestShortVector2d:
    @pytest.fixture
    def short_vec_1(self):
        return ShortVector2d(1/11, 1/27)
    
    def test_bytes(self, short_vec_1):
        assert len(bytes(short_vec_1)) == 9

