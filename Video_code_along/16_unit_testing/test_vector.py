from vector import Vector
from pytest import raises

def test_valid_init():
    v = Vector(1,2,3)
    assert v.numbers == (1,2,3)

def test_invalid_init():
    with raises(TypeError):
        Vector(1,2,"3")

    with raises(ValueError):
        Vector()

def test_addition():
    v1 = Vector(1,2,3)
    v2 = Vector(4,5,6)
    result = v1+v2
    assert result.numbers == (5,7,9)

    with raises(TypeError):
        v1 + "not a vector"