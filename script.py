#!/usr/bin/env python3

# Beispiel für das Verhalten von mutable und immutable Variablen bei der Übergabe an Funktionen

def aendere_immutable_variable(x: int):
    """Versucht, den Wert einer immutable Variablen zu ändern."""
    print(f"Ursprünglicher Wert in der Funktion (immutable): {x}")
    print(f"    Speicheradresse: {id(x)}")
    x += 10  # Bei immutable Variablen wie int wird eine neue Speicheradresse verwendet
    print(f"Geänderter Wert in der Funktion (immutable): {x}")
    print(f"    Speicheradresse: {id(x)}")


# Beispiel mit einer immutable Variable
zahl = 20
print(f"Vor Funktionsaufruf (immutable): {zahl}")
print(f"    Speicheradresse: {id(zahl)}")
aendere_immutable_variable(zahl)
print(f"Nach Funktionsaufruf (immutable): {zahl}, Speicheradresse: {id(zahl)}")
print(f"    Speicheradresse: {id(zahl)}")



def aendere_mutable_variable(liste: list):
    """Ändert den Inhalt einer mutable Variablen."""
    print(f"Ursprüngliche Liste in der Funktion (mutable): {liste}")
    print(f"    Speicheradresse: {id(liste)}")
    liste.append(100)  # Mutable Variablen wie Listen werden im selben Speicherplatz verändert
    print(f"Geänderte Liste in der Funktion (mutable): {liste}")
    print(f"    Speicheradresse: {id(liste)}")

# Beispiel mit einer mutable Variable
meine_liste = [1, 2, 3]
print(f"Vor Funktionsaufruf (mutable): {meine_liste}")
print(f"    Speicheradresse: {id(meine_liste)}")
aendere_mutable_variable(meine_liste)
print(f"Nach Funktionsaufruf (mutable): {meine_liste}")
print(f"    Speicheradresse: {id(meine_liste)}")
