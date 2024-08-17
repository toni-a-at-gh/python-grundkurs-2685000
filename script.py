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
