# Uveränderliche (immutable) Variablen in Python

# Hintergrund: Variablen sind manchmal nur zum Schein änderbar.
# Zur Untersuchung kann die Funktion "id(x)" genutzt werden, um die Speicheradresse
# einer Variablen x zu bestimmen.

x = 10
print("Variable x: x = " + str(x) + ", Speicheradresse = " + str(id(x)))
print(f"Variable x: x = {x}, Speicheradresse = {id(x)}")
x = x + 5
print("Speicherardresse nach dem Addieren x = x + 5: " + str(id(x)))

# Die Speicheradresse ist dann eine andere!
# Dieses Verhalten trifft auf folgende Datentypen zu:
# - Integer 
# - Float 
# - String
# - Tuple 
# - Bytes
# - Frozenset 
