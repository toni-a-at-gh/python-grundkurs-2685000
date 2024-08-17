class Aufgabe:
    """
    Hält Informationen zu einer Aufgabe.
    """
    def __init__(self, titel: str, beschreibung: str, kategorie: str, prio: int, datum: str):
        """
        Initialisiert eine Instanz der Klasse mit den angegebenen Parametern.
        - titel (str): Der Titel der Aufgabe.
        - beschreibung (str): Die Beschreibung der Aufgabe.
        - kategorie (str): Die Kategorie der Aufgabe.
        - prio (int): Die Priorität der Aufgabe.
        - datum (str): Das Datum der Aufgabe.
        """
    
        self.titel = titel
        self.beschreibung = beschreibung
        self.kategorie = kategorie
        self.prio = prio
        self.datum = datum

    def __repr__(self) -> str:
        return f"Aufgabe {self.titel} mit Prio: {self.prio}"

    def __str__(self):
        return f"Aufgabe: {self.titel} ({self.kategorie}), Prio: {self.prio}, Fällig: {self.datum}"
    
    def __eq__(self, other):
        """
        Überprüft, ob zwei Aufgaben gleich sind.
        """
        if isinstance(other, Aufgabe):
            return self.titel == other.titel and \
            self.beschreibung == other.beschreibung and \
            self.kategorie == other.kategorie and \
            self.prio == other.prio and self.datum == other.datum
        return False

   