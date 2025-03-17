class BankAccount:
    def __init__(
        self, Name: str, Vorname: str, Kontonummer: str, KontostandInitial: int
    ):
        """Initialisierungsfunktion zur Anlage eines neuen Bankkontos"""
        self.name = Name
        self.vorname = Vorname
        self.kontonummer = Kontonummer
        self._kontostand = KontostandInitial
        return

    def einzahlen(self, betrag: int):
        """Einzahlen eines Betrags auf das Bankkonto"""
        self._kontostand += betrag
        return

    def abheben(self, betrag: int) -> int:
        """Abheben eines Betrags vom Bankkonto"""
        self._kontostand -= betrag
        return betrag

    def get_Kontostand(self) -> int:
        """Aktuellen Kontostand zurückgeben"""
        return self._kontostand

    def __str__(self) -> str:
        """Gibt Kurzinfo zu Konto wieder."""
        return f"Bankkonto von ' {self.vorname} {self.name}', IBAN '{self.kontonummer}'"