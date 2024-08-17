import pytest
from bank_account.account import BankAccount

@pytest.fixture
def bank_konto():
    return BankAccount("Max Mustermann", "DE1234567890", 100.0)

def test_einzahlen_positive_amount(bank_konto):
    bank_konto.einzahlen(50.0)
    assert bank_konto.get_kontostand() == 150.0
    assert ("Einzahlung", 50.0) in bank_konto.get_transaktionen()

def test_abheben_within_balance(bank_konto):
    bank_konto.abheben(40.0)
    assert bank_konto.get_kontostand() == 60.0
    assert ("Abhebung", 40.0) in bank_konto.get_transaktionen()

def test_abheben_insufficient_funds(bank_konto):
    with pytest.raises(ValueError, match="Unzureichendes Guthaben"):
        bank_konto.abheben(150.0)
