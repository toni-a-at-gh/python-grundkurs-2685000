from aufgaben_package.rechen_operation import erhoehe_um_zwei, multipliziere_mit_drei, subtrahiere_zehn, teile_durch_vier
import pytest

def test_erhoehe_um_zwei():
    assert erhoehe_um_zwei(3) == 5 # Dieser Testfall sollte "passieren"
    assert erhoehe_um_zwei(3) == 6 # Dieser Testfall sollte "durchfallen", da er hier absichtlich falsch definiert wurde

def test_multipliziere_mit_drei():
    assert multipliziere_mit_drei(2) == 6 # Dieser Testfall sollte "passieren"
    assert multipliziere_mit_drei(3) == 9 # Dieser Testfall sollte "durchfallen"

def test_teile_durch_vier():
    with pytest.raises(ValueError):
        teile_durch_vier(5)               # Dieser Testfall sollte "passieren", da hier ein Rest bei der Division durch vier bleibt