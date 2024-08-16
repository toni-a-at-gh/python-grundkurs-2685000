#!/usr/bin/env python3

class Buch:
    """Eine erweiterte Klasse zur Darstellung eines Buches im Bücherregal."""

    def __init__(self, titel: str, autor: str):
        """Initialisiert das Buch mit einem Titel und einem Autor."""
        self.titel = titel
        self.autor = autor
        self._status = "verfügbar"

    def __str__(self) -> str:
        """Gibt eine benutzerfreundliche Darstellung des Buches zurück."""
        return f"'{self.titel}' von {self.autor}"

    def __repr__(self) -> str:
        """Gibt eine technische Darstellung des Buches zurück, nützlich für Debugging."""
        return f"Buch(titel='{self.titel}', autor='{self.autor}', status='{self._status}')"

    def __call__(self) -> str:
        """Macht die Instanz aufrufbar und gibt eine Statusmeldung zurück."""
        return f"Das Buch '{self.titel}' ist aktuell {self._status}."

    def ausleihen(self):
        """Markiert das Buch als ausgeliehen, wenn es verfügbar ist."""
        if self._status == "verfügbar":
            self._status = "ausgeliehen"
            print(f"Das Buch '{self.titel}' wurde ausgeliehen.")
        else:
            print(f"Das Buch '{self.titel}' ist bereits ausgeliehen.")

    def zurückgeben(self):
        """Markiert das Buch als verfügbar."""
        if self._status == "ausgeliehen":
            self._status = "verfügbar"
            print(f"Das Buch '{self.titel}' wurde zurückgegeben.")
        else:
            print(f"Das Buch '{self.titel}' ist bereits verfügbar.")

    def get_status(self) -> str:
        """Gibt den aktuellen Ausleihstatus des Buches zurück."""
        return self._status

# Erstellung und Nutzung der erweiterten Buch-Klasse
buch = Buch("Der Herr der Ringe", "J.R.R. Tolkien")

# __str__ wird aufgerufen, wenn ein Buch mit print ausgegeben wird
print(buch)

# __repr__ wird aufgerufen, wenn ein Buch im Debugging-Kontext ausgegeben wird
print(repr(buch))

# __call__ macht die Instanz aufrufbar wie eine Funktion
print(buch())  # Ähnlich wie ein Funktionsaufruf

# Standardoperationen wie Ausleihen und Zurückgeben
buch.ausleihen()
print(buch())  # Zeigt den aktuellen Status nach dem Ausleihen
buch.zurückgeben()
print(buch())  # Zeigt den aktuellen Status nach der Rückgabe
