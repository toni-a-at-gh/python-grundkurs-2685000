from bank_account.aufgaben import Aufgabe
from bank_account.account import KategorieManager

from bank_account.utils.sortieren import sortiere_nach_prio

def main():
    kategorie_manager = KategorieManager()
    kategorie_manager.fuege_kategorie_hinzu("Privat")
    kategorie_manager.fuege_kategorie_hinzu("Arbeit")
    print("Verfügbare Kategorien", kategorie_manager)

    
    aufgabe_1 = Aufgabe("Vertraulich", "Gehaltsverhandlung mit dem Chef", "Arbeit", 20, "2025-10-02")
    aufgabe_2 = Aufgabe("Projekt X", "Überraschungsparty für Lena planen", "Privat", 100, "2025-09-03")
    aufgabe_3 = Aufgabe("Einkaufen", "Einkaufen gehen", "Privat", 30, "2025-10-01")
    
    aufgaben = [aufgabe_1, aufgabe_2, aufgabe_3]
    print("Unsortierte Aufgaben:", aufgaben)

    aufgaben = sortiere_nach_prio(aufgaben)
    print("Sortierte Aufgaben:", aufgaben)


if __name__ == "__main__":
    main()