#!/usr/bin/env python3

# Die Aufgabenstellung:

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

# Optional:
# - Erstellen Sie eine Methode, die Transaktionen protokolliert und eine Liste von Ein- und Auszahlungen ausgibt.

import os  # Wird gebraucht, um "clear screen" in der Kommandozeile durch das Skript hier selber auszuführen


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


def main():
    # Kommandozeile löschen:
    os.system("cls")

    print("BANKSIMULATOR")
    willKonto = str(input("Guten Tag. Möchte Sie ein Bankkonto eröffnen? [y/n] "))
    if willKonto == "y":
        # Konto anlegen
        vorname = str(input("Gut. Wie lautet ihr Vorname? "))
        name = str(input("Wie lautet ihr Nachname? "))
        IBAN = "DE 12345"  # Kontonr. wird hier der Einfachheit halber festgelegt
        try:
            initial = int(
                input("Welchen Betrag in Euro möchten Sie initial einzahlen? ")
            )
        except ValueError:
            print("Entschuldigung, Ihre Eingabe ist ungülitg. Auf Wiedersehen.")
            return
        else:
            if initial < 0:
                print(
                    "Entschuldigung, aber Sie können kein Konto gleich mit Schulden eröffnen. Auf Wiedersehen."
                )
                return
            konto = BankAccount(name, vorname, IBAN, initial)
            print("Vielen Dank. Wir haben nun folgendes Konto angelegt: " + str(konto))
            auswahl = str(input("Möchten Sie gleich wieder Geld abheben? [y/n] "))
            if auswahl == "y":
                try:
                    betrag = int(input("Welchen Betrag möchten Sie abheben? "))
                except ValueError:
                    print(
                        "Entschuldigung. Das war keine gültige Eingabe. Auf Wiedersehen."
                    )
                else:
                    konto.abheben(betrag)
                    print(
                        "Ihr Kontostand lautet nun "
                        + str(konto.get_Kontostand())
                        + " €. Auf Wiedersehen."
                    )
                    return
            elif auswahl == "n":
                print("Na gut. Dann auf Wiedersehen.")
                return
            else:
                print("Ich konnte Sie leider nicht mehr verstehen. Auf Wiedersehen.")
                return
    elif willKonto == "n":
        print("Ok. Dann auf Wiedersehen und noch einen schönen Tag.")
        return
    else:
        print("Entschuldigung, ich konnte Sie nicht verstehen. Auf Wiedersehen.")
    return


if __name__ == "__main__":
    main()
