from python_grund_kurs.aufgaben import Aufgabe

def sortiere_nach_prio(aufgaben: list[Aufgabe]) -> list[Aufgabe]:
    """
    Sortiert die übergebenen Aufgaben nach ihrer Priorität und gibt sie zurück.
    - aufgaben (list[Aufgabe]): Die Liste der Aufgaben.
    """
    aufgaben.sort(key=lambda x: x.prio)
    return aufgaben