#!/usr/bin/env python3

# Die Aufgabenstellung in Branch "05_05-Bankkt-Bsp-mit-Vererb-als-Prj":

# Das Ergebnis aus Branch "03_12-Bankkonto-Bsp-mit-Vererbg" soll so umgebaut werden,
# dass es ein strukturiertes Projekt ergibt. Dort enthielt die Datei "TinosBeispiel.py"
# alles: die Klassendefinitionen "BankAccount" und "Jugendkonto", sowie die Hauptfunktion
# "main()". Dieser Spaghetticode soll in ein strukturiertes Projekt überführt werden.
# Das heißt:
# - Es soll ein Package "src/bank_account" erstellt werden
# - Dieses Package soll zwei Module beinhalten:
#   + M1: Implementierung der Klasse "BankAccount"
#   + M2: Implementierung der Klasse "Jugendkonto"
# - Dieses Package soll außerdem ein Skript beinhalten, das die Hauptfunktion enthält
# - Es soll auch die "pyproject.toml" enthalten

# Die Aufgabenstellung:

# Aufgabe: Erstellen Sie ein neues Jugendbankkonto, dass von der Klasse
# BankAccount erbt und beschränken sie die Abhebungen auf maximal 25€.

# Hinweis in eigener Sache: für dieses Beispiel erweitere ich die von mir erstellte Klasse
# (siehe Branch 03_08-Bankkonto-Bsp), nicht die von der Trainingsleiterin. Grund: ich hatte schon
# einiges mehr ergänzt, z.B. Kommandozeile leeren

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


def main():
    # Kommandozeile löschen:
    os.system("cls")

    print("BANKSIMULATOR")
    willKonto = str(input("Guten Tag. Möchte Sie ein Bankkonto eröffnen? [y/n] "))
    if willKonto == "y":
        # Konto anlegen
        vorname = str(input("Gut. Wie lautet ihr Vorname? "))
        name = str(input("Wie lautet ihr Nachname? "))
        try:
            alter = int(input("Wie alt sind Sie? "))
        except ValueError:
            print("Entschuldigung, Ihre Eingabe ist ungülitg. Auf Wiedersehen.")
            return
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
            if alter < 18:
                konto = Jugendkonto(name, vorname, IBAN, initial)
                print(
                    "Vielen Dank. Wir haben nun folgendes Jugendkonto angelegt: "
                    + str(konto)
                )
            else:
                konto = BankAccount(name, vorname, IBAN, initial)
                print(
                    "Vielen Dank. Wir haben nun folgendes Konto angelegt: " + str(konto)
                )
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
