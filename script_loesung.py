#!/usr/bin/env python3

# Aufgabe: Erstellen Sie eine Klasse 'BankAccount', die ein einfaches Bankkonto repräsentiert.

# 1. Die Klasse soll die folgenden Attribute (Member-Variablen) haben:
#    - Inhaber: Der Name des Kontoinhabers (öffentlich).
#    - Kontonummer: Eine eindeutige Kontonummer (öffentlich).
#    - __kontostand: Der aktuelle Kontostand (nicht öffentlich).

# 2. Implementieren Sie die folgenden Methoden:
#    - __init__: Initialisiert den Kontoinhaber, die Kontonummer und den anfänglichen Kontostand.
#    - einzahlen: Erhöht den Kontostand um einen bestimmten Betrag.
#    - abheben: Verringert den Kontostand um einen bestimmten Betrag, wenn genügend Guthaben vorhanden ist.
#    - get_kontostand: Gibt den aktuellen Kontostand zurück.

# 3. Implementieren Sie außerdem eine Methode __str__, die eine benutzerfreundliche Darstellung des Kontos zurückgibt.

# 4. Die Ein-/Auszahlungs-Methoden sollen sicherstellen:
#    - Es kann kein negativer Betrag eingezahlt oder abgehoben werden.
#    - Bei einem Abhebevorgang darf der Kontostand nicht negativ werden (Überziehung nicht erlaubt).

# Optional:
# - Erstellen Sie eine Methode, die Transaktionen protokolliert und eine Liste von Ein- und Auszahlungen ausgibt.

#!/usr/bin/env python3

from typing import List, Tuple

class BankAccount:
    """Eine Klasse zur Darstellung eines einfachen Bankkontos."""

    def __init__(self, inhaber: str, kontonummer: str, start_kontostand: float = 0.0):
        """Initialisiert den Kontoinhaber, die Kontonummer und den anfänglichen Kontostand."""
        self.inhaber = inhaber
        self.kontonummer = kontonummer
        self._kontostand = start_kontostand
        self._transaktionen: List[Tuple[str, float]] = []

    def einzahlen(self, betrag: float) -> None:
        """Erhöht den Kontostand um den eingezahlten Betrag."""
        if betrag > 0:
            self._kontostand += betrag
            self._transaktionen.append(("Einzahlung", betrag))
            print(f"{betrag} EUR wurden eingezahlt.")
        else:
            print("Einzahlung fehlgeschlagen: Betrag muss positiv sein.")

    def abheben(self, betrag: float) -> None:
        """Verringert den Kontostand um den abgehobenen Betrag, wenn genügend Guthaben vorhanden ist."""
        if betrag > 0:
            if self._kontostand >= betrag:
                self._kontostand -= betrag
                self._transaktionen.append(("Abhebung", betrag))
                print(f"{betrag} EUR wurden abgehoben.")
            else:
                print("Abhebung fehlgeschlagen: Unzureichendes Guthaben.")
        else:
            print("Abhebung fehlgeschlagen: Betrag muss positiv sein.")

    def get_kontostand(self) -> float:
        """Gibt den aktuellen Kontostand zurück."""
        return self._kontostand

    def get_transaktionen(self) -> List[Tuple[str, float]]:
        """Gibt eine Liste aller Transaktionen zurück."""
        return self._transaktionen

    def __str__(self) -> str:
        """Gibt eine benutzerfreundliche Darstellung des Kontos zurück."""
        return (
            f"Konto von {self.inhaber}\n"
            f"Kontonummer: {self.kontonummer}\n"
            f"Aktueller Kontostand: {self._kontostand:.2f} EUR"
        )

# Beispielverwendung
konto = BankAccount("Max Mustermann", "DE1234567890", 100.0)

print(konto)

konto.einzahlen(50)
konto.abheben(30)

print(f"Aktueller Kontostand: {konto.get_kontostand()} EUR")

# Transaktionen anzeigen
print("Transaktionsverlauf:")
for transaktion in konto.get_transaktionen():
    print(f"{transaktion[0]}: {transaktion[1]:.2f} EUR")
