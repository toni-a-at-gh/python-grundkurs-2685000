import os  # Wird gebraucht, um "clear screen" in der Kommandozeile durch das Skript hier selber auszuführen


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