#!/usr/bin/env python3

# Einführung in das Memory Management bei immutable Variablen in Python
# Das bedeutet, dass bei einer Änderung des Wertes eine neue Speicheradresse für
# die Variable verwendet wird, anstatt des ursprünglichen Speicherplatzes.

# Integer sind unveränderlich (immutable) in Python
x = 10  # Erstellen einer Integer-Variable
print(f"x: {x}, Speicheradresse: {id(x)}")
x = x + 5  # Da Integer unveränderlich (immutable) sind, wird eine neue Speicheradresse verwendet
print(f"x nach Änderung: {x}, Speicheradresse: {id(x)}")

# Strings sind unveränderlich (immutable) in Python
s = "Hallo"  # Erstellen einer String-Variable
print(f"s: {s}, Speicheradresse: {id(s)}")
s = s + " Welt"  # Da Strings unveränderlich (immutable) sind, wird eine neue Speicheradresse verwendet
print(f"s nach Änderung: {s}, Speicheradresse: {id(s)}")

# Immutable Variablen: 
# - Integer 
# - Float 
# - String
# - Tuple 
# - Bytes
# - Frozenset 



