import pytest
from aufgaben_package.personen import Person

def test_personen_init():
    Bob = Person("Bob", 34)     # Das Obekt (vom Typ "Person") anlegen
    assert Bob.name == "Bob"    # Prüfen, ob beim Anlegen der Person der Name "Bob" wirklich vergeben wurde
    assert Bob.alter == 34      # Prüfen, ob beim Anlegen der Person das Alter tatsächlich übernommen wurde

def test_personen_string():
    Ina = Person("Ina", 33)         # Das Objekt vom Typ "Person" anlegen
    assert str(Ina) == "Ina (33)"   # Testen, ob der Description-String, so, wie er sein sollte, zurückgegeben wurde

