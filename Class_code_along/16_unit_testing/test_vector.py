from pytest import raises, approx
from vector import Vector
import math

def test_valid_init():
    v = Vector(1,2)
    assert v.numbers == (1,2)

def test_negative_valid_init():
    v = Vector(-1,-2)
    assert v.numbers == (-1,-2)

def test_string_in_init_fails():
    with raises(TypeError):
        Vector("1",2)

def test_different_legnths():
    vectors = (Vector(1,2), Vector(1,2,3), Vector(1), Vector(1,2,3,4))
    expected_lengths = (2,3,1,4)

    for vector, expected_length in zip(vectors, expected_lengths):
        assert len(vector) == expected_length

def test_vector_norm_valid():
    v = Vector(1,4)
    expected_norm = math.sqrt(1**2 + v[1]**2)

    assert abs(v) == approx(expected_norm)

def test_empty_value():
    with raises(ValueError):
        Vector()