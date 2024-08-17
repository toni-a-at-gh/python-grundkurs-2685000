from bank_account.account import BankAccount

class JugendBankAccount(BankAccount):
    def abheben(self, betrag: float) -> None:
        if betrag <= 25:
            super().abheben(betrag)
        else:
            raise ValueError("Abhebung fehlgeschlagen: Maximalbetrag von 25 EUR überschritten.")
