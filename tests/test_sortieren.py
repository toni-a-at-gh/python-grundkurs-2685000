from python_grund_kurs.utils.sortieren import sortiere_nach_prio
from python_grund_kurs.aufgaben import Aufgabe

# FILEPATH: /home/julia/linkedin/python-grundkurs-2685000/tests/test_sortieren.py


def test_sortiere_nach_prio():
    # Test case 1: Empty list
    assert sortiere_nach_prio([]) == []

    # Test case 2: List with one Aufgabe
    aufgaben = [Aufgabe("Aufgabe1", "Beschreibung 1", "Kat 1", 10, "2022-01-01")]
    assert sortiere_nach_prio(aufgaben) == [Aufgabe("Aufgabe1", "Beschreibung 1", "Kat 1", 10, "2022-01-01")]

    # Test case 3: List with multiple Aufgaben
    aufgaben = [
        Aufgabe("Aufgabe1", "Beschreibung 1", "Kat 1", 2, "2022-01-01"),
        Aufgabe("Aufgabe2", "Beschreibung 2", "Kat 1", 1, "2022-01-01"),
        Aufgabe("Aufgabe3", "Beschreibung 3", "Kat 1", 3, "2022-01-01")
    ]
    assert sortiere_nach_prio(aufgaben) == [
        Aufgabe("Aufgabe2", "Beschreibung 2", "Kat 1", 1, "2022-01-01"),
        Aufgabe("Aufgabe1", "Beschreibung 1", "Kat 1", 2, "2022-01-01"),
        Aufgabe("Aufgabe3", "Beschreibung 3", "Kat 1", 3, "2022-01-01")
    ]