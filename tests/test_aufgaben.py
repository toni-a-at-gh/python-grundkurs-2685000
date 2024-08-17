from python_grund_kurs.aufgaben import Aufgabe

def test_aufgabe_init():
    aufgabe = Aufgabe("Aufgabe1", "Beschreibung 1", "Kat 1", 1, "2022-01-01")
    assert aufgabe.titel == "Aufgabe1"
    assert aufgabe.beschreibung == "Beschreibung 1"
    assert aufgabe.kategorie == "Kat 1"
    assert aufgabe.prio == 1
    assert aufgabe.datum == "2022-01-01"

def test_aufgabe_str():
    aufgabe = Aufgabe("Aufgabe2", "Beschreibung 2", "Kat 2", 2, "2022-02-02")
    assert str(aufgabe) == "Aufgabe: Aufgabe2 (Kat 2), Prio: 2, Fällig: 2022-02-02"