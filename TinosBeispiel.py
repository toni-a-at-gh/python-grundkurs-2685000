#!/usr/bin/env python3

import os  # Wird gebraucht, um "clear screen" in der Kommandozeile durch das Skript hier selber auszuführen

# Aufgabe:
# Erstellen Sie eine Klasse 'Ebike', die die Eigenschaften 'marke', 'modell' und 'reichweite' hat.
# - Implementieren Sie eine Methode 'tanken', die die Reichweite um einen gegebenen Wert erhöht.
# - Stellen Sie sicher, dass der Tankinhalt privat ist und nur über eine Methode abgefragt werden kann.
# - Instanzieren Sie ein Elektrofahrrad und testen Sie die Methoden.


class EBike:
    # Initialisierungsfunktion: damit werden die Attribute der Klasse definiert. Ein "_"im Namen des
    # Attributs gibt an, dass es sich um ein private Attribut handelt. Fehlt das Zeichen, handelt es
    # sich um ein publich Attribut
    def __init__(self, marke: str, modell: str, reichweite: int):
        """Initialisierung eines EBikes mit Marke, Modell, Reichweite und Akkustand"""
        self.marke = marke  # Public Attribut: Übernimmt den angegebenen Namen der Marke bei Instanziierung der Klasse
        self.modell = modell  # Public Attribut: Übernimmt den angegebenen Namen des Modells bei Instanziierung der Klasse
        self.reichweite = reichweite  # Public Attribut: Übernimmt die angegebene Reichweite bei Instanziierung der Klasse
        self._akkustand = 12  # Private Attribut: Akkustand in %
        return

    def Aufladen(self, wert: int):
        """Methode zum Aufladen des Akkus um den Wert 'wert'"""
        self._akkustand += wert
        return

    def get_Akkustand(self) -> int:
        """Methode gibt aktuellen Akkustand zurück"""
        return self._akkustand


# Instanziierung eines EBikes:
os.system("cls")  # Löscht die Kommandozeile
print("EBIKE-SIMULATION")
print("Ihr E-Bike wird nun erzeugt.")
Marke = str(input("Bitte geben Sie die gewünschte Marke an: "))
Modell = str(input("Bitte geben sie das gewünschte Modell an: "))
Reichweite = str(input("Bitte geben sie die gewünschte Reichweite in km ein: "))
MeinEbike = EBike(Marke, Modell, Reichweite)
print(
    "Sie besitzen nun E-Bike der Marke '"
    + Marke
    + "', Modell '"
    + Modell
    + "' mit einer Reichweite von "
    + Reichweite
    + " km."
)
print(
    "Ihr E-Bike hat aktuell einen Akkustand von "
    + str(MeinEbike.get_Akkustand())
    + " %."
)
Aufladewunsch = str(input("Möchten Sie den Akku aufladen? [y, n]"))
if Aufladewunsch == "y":
    try:
        Aufladewert = int(
            input(
                "Ok. Dann geben Sie bitte einen ganzzahligen Aufladewert in % an, der aufgeladen werden soll: "
            )
        )
    except ValueError:
        print("Sorry, das ist kein gültiger Wert. Auf Wiedersehen.")
    else:
        MeinEbike.Aufladen(Aufladewert)
        print(
            "Ihr E-Bike hat nun einen Akkustand von "
            + str(MeinEbike.get_Akkustand())
            + " %. Auf Wiedersehen."
        )
elif Aufladewunsch == "n":
    print("Ok. Dann haben Sie noch einen schönen Tag.")
else:
    print("Sorry, ich habe ihre Eingabe nicht verstanden. Auf Wiedersehen.")
