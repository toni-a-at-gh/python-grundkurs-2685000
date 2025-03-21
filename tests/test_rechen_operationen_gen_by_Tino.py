# Der folgende Code wurde vom Microsoft Copilot vorgeschlagen, nachdem folgende Anfrage
# gestellt wurde:

# Ich habe folgende Funktionen im Modul "rechen_operation.py" meines Python-Projekts "aufgaben_package" erstellt:
# 
# def erhoehe_um_zwei(zahl):
#     return zahl + 2
# 
# def multipliziere_mit_drei(zahl):
#     return zahl * 3
# 
# def subtrahiere_zehn(zahl):
#     return zahl - 10
# 
# def teile_durch_vier(zahl):
#     if zahl == 0:
#         raise ZeroDivisionError("Zahl darf nicht 0 sein")
#     if zahl % 4 != 0:
#         raise ValueError("Zahl muss durch 4 teilbar sein")
#     return zahl / 4
# 
# Bitte erstelle mir für jede Funktion drei Testfälle im Python-Framework "pytest". Dabei sollen ganzzahlige Werte und auch Fließommazahlen verwendet werden. Beachte, dass man Fließkommazahlen nicht direkt vergleichen kann.

import pytest
import math
from aufgaben_package.rechen_operation import erhoehe_um_zwei, multipliziere_mit_drei, subtrahiere_zehn, teile_durch_vier

def test_erhoehe_um_zwei():
    assert erhoehe_um_zwei(5) == 7
    assert erhoehe_um_zwei(-3) == -1
    assert math.isclose(erhoehe_um_zwei(2.5), 4.5)

def test_multipliziere_mit_drei():
    assert multipliziere_mit_drei(4) == 12
    assert multipliziere_mit_drei(-2) == -6
    assert math.isclose(multipliziere_mit_drei(3.3), 9.9)

def test_subtrahiere_zehn():
    assert subtrahiere_zehn(15) == 5
    assert subtrahiere_zehn(-5) == -15
    assert math.isclose(subtrahiere_zehn(10.5), 0.5)

def test_teile_durch_vier():
    assert teile_durch_vier(8) == 2
    assert teile_durch_vier(16) == 4
    assert math.isclose(teile_durch_vier(8.0), 2.0)
    
    with pytest.raises(ZeroDivisionError):
        teile_durch_vier(0)
    
    with pytest.raises(ValueError):
        teile_durch_vier(7)