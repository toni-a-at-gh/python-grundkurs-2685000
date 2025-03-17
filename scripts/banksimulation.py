# Die folgende Aufgabenstellung ist die gleiche wie die aus # "03_12-Bankkonto-Bsp-mit-Vererbg".
# Im Gegensatzu zum Code in Branch "03_12-Bankkonto-Bsp-mit-Vererbg" ist hier eine Projektstruktur
# eingebaut worden. Der Code ist daher in verschiedenen Modulen gelandet, die Funktionalität ist
# aber noch identisch.

# Die urprüngliche Aufgabenstellung:

# Aufgabe: Erstellen Sie ein neues Jugendbankkonto, dass von der Klasse
# BankAccount erbt und beschränken sie die Abhebungen auf maximal 25€.

# ******************************************************************************************
# HINWEIS: 
#
# Das Skript "scr/banksimulation.py" ist nur lauffähig, wenn zuvor das Projekt 
# "bank_account" per "pip install ." auf Ebene, in der sich die "pyproject.toml" befindet,
# installiert wurde.
#
# ******************************************************************************************


import os  # Wird gebraucht, um "clear screen" in der Kommandozeile durch das Skript hier selber auszuführen

# Importieren der Klasse "BankAccount" aus dem Modul "bankAccount", das wiederum Teil des Packages
# "bank_account" ist:
from bank_account.bankAccount import BankAccount

# Importieren der Klasse "Jugendkonto" aus dem Modul "bankAccount", das wiederum Teil des Packages
# "bank_account" ist:
from bank_account.jugendkonto import Jugendkonto 

# Die Hauptfunktion des Skripts:
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