#!/usr/bin/env python3

# Die Aufgabenstellung:

# Aufgabe: Ändern Sie den Code aus dem vorherigen Beispiel mit dem Bankkonto so
# ab, dass eine Exception ausgelöst wird, wenn der einzahlende Betrag negativ
# ist, oder das Bankkonto negative Beträge enthält.

# Hinweis: Unten wurde zu diesem Zweck der Code aus
# https://github.com/toni-a-at-gh/python-grundkurs-2685000/blob/03_08-Bankkonto-Bsp/TinosBeispiel.py
# kopiert und entsprechend angepasst


import os  # Wird gebraucht, um "clear screen" in der Kommandozeile durch das Skript hier selber auszuführen


class BankAccount:
    def __init__(
        self, Name: str, Vorname: str, Kontonummer: str, KontostandInitial: int
    ):
        """Initialisierungsfunktion zur Anlage eines neuen Bankkontos"""
        self.name = Name
        self.vorname = Vorname
        self.kontonummer = Kontonummer

        # Eingebaute Abfrage auf negativen initial gewünschten Kontostand durch Werfen der Exception
        # ValueError
        if KontostandInitial < 0:
            raise ValueError(
                "Entschuldigung, aber Sie können kein Konto gleich mit Schulden eröffnen."
            )
        else:
            self._kontostand = KontostandInitial
        return

    def einzahlen(self, betrag: int):
        """Einzahlen eines Betrags auf das Bankkonto"""
        if betrag < 0:
            raise ValueError("Der einzuzahlende Betrag darf nicht negativ sein!")
        return
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
            # Der folgende Code wurde durch das Werfen der ValueError Excception in der
            # Methode def __init__() abgelöst, wenn ein negativer Betrag angegeben wurde:
            # if initial < 0:
            #    print(
            #        "Entschuldigung, aber Sie können kein Konto gleich mit Schulden eröffnen. Auf Wiedersehen."
            #    )
            #    return
            try:
                konto = BankAccount(name, vorname, IBAN, initial)
            except ValueError as e:
                print(str(e) + " Auf Wiedersehen.")
                return
            else:
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
                    print(
                        "Ich konnte Sie leider nicht mehr verstehen. Auf Wiedersehen."
                    )
                    return
    elif willKonto == "n":
        print("Ok. Dann auf Wiedersehen und noch einen schönen Tag.")
        return
    else:
        print("Entschuldigung, ich konnte Sie nicht verstehen. Auf Wiedersehen.")
    return


if __name__ == "__main__":
    main()
