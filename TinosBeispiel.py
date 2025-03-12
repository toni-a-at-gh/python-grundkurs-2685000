#!/usr/bin/env python3

# Beispiel für das Verhalten von mutable und immutable Variablen bei der Übergabe an Funktionen

def aendere_immutable_variable(x: int): # Die Funktion hier hat keinen Rückgabewert
    """Versucht, den Wert einer immutable Variablen zu ändern."""
    print(f"Ursprünglicher Wert in der Funktion (immutable): {x}")
    print(f"    Speicheradresse: {id(x)}")
    
    # Nun könnte man meinen, dass mit der folgenden Zeile der Wert von x, der als Argument
    # der Funktion verwendet wurde, auch der Wert x im Funktionsaufruf erhöht wird:
    x += 10  # Bei immutable Variablen wie int wird eine neue Speicheradresse verwendet
    
    print(f"Geänderter Wert in der Funktion (immutable): {x}")
    print(f"    Speicheradresse: {id(x)}")


# Beispiel mit einer immutable Variable
zahl = 20
print(f"Vor Funktionsaufruf (immutable): {zahl}")
print(f"    Speicheradresse: {id(zahl)}")
print ("")
print ("Nun der Funktionsaufruf ....")
aendere_immutable_variable(zahl)
print("")
print(f"Nach Funktionsaufruf (immutable): {zahl}, Speicheradresse: {id(zahl)}")
print(f"    Speicheradresse: {id(zahl)}")

# Der Wert von Zahl wird hierbei NICHT erhöht! Die Zahl bleibt unverändert. Und das, obwohl es keine
# Warung bei der Ausführung des Skripts gibt. Will man mit der Funktion "aendere_immutable_variable"
# den Wert von zahl erhöhen, dann muss dieser Funktion ein Rückgabewert spendiert werden.
