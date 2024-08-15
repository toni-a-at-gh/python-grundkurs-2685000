#!/usr/bin/env python3

from typing import List, Tuple

class BankAccount:
    """Eine Klasse zur Darstellung eines einfachen Bankkontos."""

    def __init__(self, inhaber: str, kontonummer: str, start_kontostand: float = 0.0):
        """Initialisiert den Kontoinhaber, die Kontonummer und den anfänglichen Kontostand."""
        self.inhaber = inhaber
        self.kontonummer = kontonummer
        self.__kontostand = start_kontostand
        self.__transaktionen: List[Tuple[str, float]] = []

    def einzahlen(self, betrag: float) -> None:
        """Erhöht den Kontostand um den eingezahlten Betrag."""
        if betrag > 0:
            self.__kontostand += betrag
            self.__transaktionen.append(("Einzahlung", betrag))
            print(f"{betrag} EUR wurden eingezahlt.")
        else:
            raise ValueError("Einzahlung fehlgeschlagen: Betrag muss positiv sein.")

    def abheben(self, betrag: float) -> None:
        """Verringert den Kontostand um den abgehobenen Betrag, wenn genügend Guthaben vorhanden ist."""
        if betrag > 0:
            if self.__kontostand >= betrag:
                self.__kontostand -= betrag
                self.__transaktionen.append(("Abhebung", betrag))
                print(f"{betrag} EUR wurden abgehoben.")
            else:
                raise ValueError("Abhebung fehlgeschlagen: Unzureichendes Guthaben.")
        else:
            raise ValueError("Abhebung fehlgeschlagen: Betrag muss positiv sein.")

    def get_kontostand(self) -> float:
        """Gibt den aktuellen Kontostand zurück."""
        return self.__kontostand

    def get_transaktionen(self) -> List[Tuple[str, float]]:
        """Gibt eine Liste aller Transaktionen zurück."""
        return self.__transaktionen

    def __str__(self) -> str:
        """Gibt eine benutzerfreundliche Darstellung des Kontos zurück."""
        return (
            f"Konto von {self.inhaber}\n"
            f"Kontonummer: {self.kontonummer}\n"
            f"Aktueller Kontostand: {self.__kontostand:.2f} EUR"
        )
    
# Aufgabe: Erstellen Sie ein neues Jugendbankkonto, dass von der Klasse 
# BankAccount erbt und beschränken sie die Abhebungen auf maximal 25€.
