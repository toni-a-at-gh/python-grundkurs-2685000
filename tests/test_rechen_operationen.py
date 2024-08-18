import pytest
from example_package.rechen_operationen import addition, subtraktion, multiplikation, division

def test_addition():
    assert addition(2, 3) == 5
    assert addition(-5, 10) == 5
    assert addition(0, 0) == 0

def test_subtraktion():
    assert subtraktion(5, 3) == 2
    assert subtraktion(10, -5) == 15
    assert subtraktion(0, 0) == 0

def test_multiplikation():
    assert multiplikation(2, 3) == 6
    assert multiplikation(-5, 10) == -50
    assert multiplikation(0, 5) == 0

def test_division():
    assert division(6, 2) == 3
    assert division(-10, 5) == -2
    assert division(0, 5) == 0

def test_division_by_zero():
    with pytest.raises(ZeroDivisionError):
        division(2, 0)