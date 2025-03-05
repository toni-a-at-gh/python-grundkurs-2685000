#!/usr/bin/env python3

# Aufgabe:
# Erstellen Sie eine weitere spezifische Klasse 'Vogel', die von der allgemeinen Klasse 'Tier' erbt.
# - Überschreiben Sie die Methode 'mache_geraeusch', sodass der Vogel ein typisches Geräusch wie "zwitschern" macht.
# - Erstellen Sie eine Instanz der Klasse 'Vogel' und rufen Sie die Methoden 'beschreibung' und 'mache_geraeusch' auf.

import os  # Wird gebraucht, um die Konsole zu leeren


class Tier:
    """Eine allgemeine Klasse für Tiere."""

    def __init__(self, name: str, alter: int):
        """Initialisiert das Tier mit einem Namen und einem Alter."""
        print("Ein neues Tier wurde erstellt.")
        self.name = name
        self.alter = alter

    def mache_geraeusch(self):
        """Gibt ein allgemeines Geräusch aus."""
        print(f"{self.name} macht ein Geräusch.")

    def beschreibung(self):
        """Gibt eine Beschreibung des Tieres aus."""
        print(f"Dies ist {self.name}, es ist {self.alter} Jahre alt.")

    def __str__(self) -> str:
        """Gibt eine Beschreibung des Tieres zurück."""
        return f"Name: {self.name}, Alter: {self.alter}"


# Hier ist eine von "Tier" abgeleitete Klasse "Hund". Es erbt alle Methoden
# und Attribute, solange sie nicht überschrieben (überladen) werden
class Hund(Tier):
    """Eine spezifische Klasse für Hunde, die von der allgemeinen Klasse Tier erbt."""

    # Die Methode "mache_geraeusch" wir hier überschrieben:
    def mache_geraeusch(self):
        """Überschreibt die Methode und gibt das typische Geräusch eines Hundes aus."""
        print(f"{self.name} bellt.")


# Hier ist die ebenfalls von "Tier" abgeleitete Klasse "Katze". Hier wird
# neben der "mache_geraeusche"-Methode auch die "__init__"-Methode überschrieben
# bzw. vielmehr ergänzt um die Meldung, dass eine Katze erstellt wurde.
class Katze(Tier):
    """Eine spezifische Klasse für Katzen, die von der allgemeinen Klasse Tier erbt."""

    def __init__(self, name: str, alter: int):
        super().__init__(name, alter)  # WICHTIG: mit angeben!
        print("Eine neue Katze wurde erstellt.")

    def mache_geraeusch(self):
        """Überschreibt die Methode und gibt das typische Geräusch einer Katze aus."""
        print(f"{self.name} miaut.")


class Vogel(Tier):
    """Eine spezifische Klasse für einen Vogel"""

    def __init__(self, name, alter):
        super().__init__(name, alter)
        print("Ein Vogel wurde erstellt.")

    def mache_geraeusch(self):
        """Überschreibt die Methode zum Machen eines Geräuschs"""
        print(self.name + " piept.")


def main():
    os.system("cls")  # Kommandozeile leeren
    print("ZOOSIMULATOR")
    hund = Hund("Rufus", 12)
    vogel = Vogel("Peppi", 2)
    print("Im Zoo gibt es einen Hund: " + str(hund))
    print("Im Zoo gibt es einen Vogel: " + str(vogel))
    print("Sie machen folgende Geräusche:")
    hund.mache_geraeusch()
    vogel.mache_geraeusch()
    return


if __name__ == "__main__":
    main()
