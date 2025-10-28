from vector import Vector
from pytest import raises

def test_valid_init():
    v = Vector(1,2,3)
    assert v.numbers == (1,2,3)