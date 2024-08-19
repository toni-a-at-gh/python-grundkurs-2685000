# Implementiere pytest tests für genai_beispiele.taschen_rechner.Taschenrechner

import pytest

from genai_beispiele.taschen_rechner import Taschenrechner



def test_add():
    calculator = Taschenrechner()
    result = calculator.add(2, 3)
    assert result == 5

def test_sub():
    calculator = Taschenrechner()
    result = calculator.sub(5, 2)
    assert result == 3

def test_mul():
    calculator = Taschenrechner()
    result = calculator.mul(4, 3)
    assert result == 12

def test_div():
    calculator = Taschenrechner()
    result = calculator.div(10, 2)
    assert result == 5

def test_div_by_zero():
    calculator = Taschenrechner()
    with pytest.raises(ZeroDivisionError):
        calculator.div(10, 0)

def test_get_memory():
    calculator = Taschenrechner()
    ergebnis_1 = calculator.add(2, 3)
    ergebnis_2 = calculator.sub(5, 2)
    ergebnis_3 = calculator.mul(4, 3)
    ergebnis_4 = calculator.div(10, 2)

    erwartete_antwort = [f"5 - 2 = {ergebnis_2}", f"4 * 3 = {ergebnis_3}", f"10 / 2 = {ergebnis_4}"]

    memory = calculator.get_memory()
    assert memory == erwartete_antwort