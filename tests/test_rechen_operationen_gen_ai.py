# Prompteingabe: 1
# Ich habe folgende Python Funktionen:
# def erhoehe_um_zwei(zahl):
#     return zahl + 2

# def multipliziere_mit_drei(zahl):
#     return zahl * 3

# def subtrahiere_zehn(zahl):
#     return zahl - 10

# def teile_durch_vier(zahl):
#     if zahl == 0:
#         raise ZeroDivisionError("Zahl darf nicht 0 sein")
#     if zahl % 4 != 0:
#         raise ValueError("Zahl muss durch 4 teilbar sein")
#     return zahl / 4
# Erstelle mir dafür im Framework pytest jeweils 5 unit tests. Überprüfe im 
# Speziellen mögliche Fehlerfälle. Teste sowohl integer als auch float eingaben. 
# Beachte dass man float nicht direkt vergleichen kann.

import pytest
from aufgaben_package.rechen_operation import erhoehe_um_zwei, multipliziere_mit_drei, subtrahiere_zehn, teile_durch_vier


def test_erhoehe_um_zwei():
    # Teste mit integer
    assert erhoehe_um_zwei(3) == 5
    assert erhoehe_um_zwei(-2) == 0
    assert erhoehe_um_zwei(0) == 2
    # Teste mit float (unter Berücksichtigung der Toleranz)
    assert pytest.approx(erhoehe_um_zwei(2.5), 0.01) == 4.5
    assert pytest.approx(erhoehe_um_zwei(-3.7), 0.01) == -1.7

def test_multipliziere_mit_drei():
    # Teste mit integer
    assert multipliziere_mit_drei(3) == 9
    assert multipliziere_mit_drei(-2) == -6
    assert multipliziere_mit_drei(0) == 0
    # Teste mit float
    assert pytest.approx(multipliziere_mit_drei(2.5), 0.01) == 7.5
    assert pytest.approx(multipliziere_mit_drei(-3.7), 0.01) == -11.1

def test_subtrahiere_zehn():
    # Teste mit integer
    assert subtrahiere_zehn(20) == 10
    assert subtrahiere_zehn(0) == -10
    assert subtrahiere_zehn(-5) == -15
    # Teste mit float
    assert pytest.approx(subtrahiere_zehn(10.5), 0.01) == 0.5
    assert pytest.approx(subtrahiere_zehn(-9.2), 0.01) == -19.2

def test_teile_durch_vier():
    # Teste mit integer
    assert teile_durch_vier(8) == 2
    assert teile_durch_vier(-4) == -1
    assert teile_durch_vier(16) == 4
    # Teste mit float
    assert pytest.approx(teile_durch_vier(8.0), 0.01) == 2.0
    assert pytest.approx(teile_durch_vier(-12.0), 0.01) == -3.0
    # Fehlerfälle
    with pytest.raises(ZeroDivisionError):
        teile_durch_vier(0)
    with pytest.raises(ValueError):
        teile_durch_vier(5)
    with pytest.raises(ValueError):
        teile_durch_vier(10)

def test_teile_durch_vier_floats_mit_fehler():
    # Teste, dass bei nicht durch 4 teilbaren Floats eine ValueError geworfen wird
    with pytest.raises(ValueError):
        teile_durch_vier(5.5)
    with pytest.raises(ValueError):
        teile_durch_vier(3.7)

