from bank_account.bankAccount import BankAccount

class Jugendkonto(BankAccount):
    """Klasse für einen eingeschränkten Bankaccount für Jugendliche."""

    def abheben(self, betrag):
        if betrag > 25:
            print(
                "Du hast ein Jugendkonto. Eine Abhebung über 25 € ist leider nicht möglich."
            )
            return 0
        else:
            self._kontostand -= betrag
            return betrag