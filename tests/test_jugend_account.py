import pytest
from bank_account.jugend_account import JugendBankAccount

@pytest.fixture
def jugend_konto():
    return JugendBankAccount("Max Mustermann", "DE1234567890", 100.0)

def test_abheben_max_25_euro(jugend_konto):
    jugend_konto.abheben(25.0)
    assert jugend_konto.get_kontostand() == 75.0
    assert ("Abhebung", 25.0) in jugend_konto.get_transaktionen()

def test_abheben_ueber_25_euro(jugend_konto):
    with pytest.raises(ValueError, match="Maximalbetrag von 25 EUR überschritten"):
        jugend_konto.abheben(30.0)

def test_abheben_ohne_ausreichendes_guthaben(jugend_konto):
    jugend_konto.abheben(25.0)
    jugend_konto.abheben(25.0)
    jugend_konto.abheben(25.0)
    jugend_konto.abheben(20.0)
    with pytest.raises(ValueError, match="Abhebung fehlgeschlagen: Unzureichendes Guthaben."):
        jugend_konto.abheben(20.0)
