import pytest
from aufgaben_package.rechen_operation import erhoehe_um_zwei, multipliziere_mit_drei, subtrahiere_zehn, teile_durch_vier


def test_erhoehe_um_zwei_positive():
    assert erhoehe_um_zwei(5) == 7

def test_erhoehe_um_zwei_negative():
    assert erhoehe_um_zwei(-5) == -3

def test_multipliziere_mit_drei_positive():
    assert multipliziere_mit_drei(4) == 12

def test_multipliziere_mit_drei_negative():
    assert multipliziere_mit_drei(-4) == -12

def test_subtrahiere_zehn_positive():
    assert subtrahiere_zehn(15) == 5

def test_subtrahiere_zehn_negative():
    assert subtrahiere_zehn(-15) == -25

def test_teile_durch_vier_positive():
    assert teile_durch_vier(16) == 4

def test_teile_durch_vier_zero_div():
    with pytest.raises(ZeroDivisionError):
        teile_durch_vier(0)

def test_teile_durch_vier_not_divisible():
    with pytest.raises(ValueError):
        teile_durch_vier(5)