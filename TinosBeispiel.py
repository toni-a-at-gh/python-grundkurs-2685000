import sys  # Wird gebraucht, um den Reference Counter ausgeben lassen zu können

# Der Reference Counter
# =====================

print("REFRENCE COUNTER:")
print("")

x = [1, 2, 3] # Eine Variable vom Typ "Liste"
print("Liste x: " + str(x))
print("Wert des Reference Counters für x: " + str(sys.getrefcount(x)))
# Hinweis: der Wert des Counters ist nicht 1, wie vielleich zu erwarten wäre, weil ja nur ein Objekt 'x'
# angelegt wurde. Er hat den Wert 2, was durch den Funktionsaufruf 'sys.getrefcount(x)' kommt

print("")
y = [4, 5, 6]
print("Liste y: " + str(y))
print("Wert des Reference Counters für y: " + str(sys.getrefcount(y)))
y.append(x) # Fügt die Liste x an das Ende von Liste y an
print("Liste x wurde Liste y hinzugefügt. Wert von Liste y nun: " + str(y))
print("Wert des Reference Counters für Liste x nun: " + str(sys.getrefcount(x)))
print("Wert des Reference Counters für Liste y nun: " + str(sys.getrefcount(y)))

print("")
del y
print("Liste y wurde gelöscht. Wert des Reference Counters für Liste x nun: " + str(sys.getrefcount(x)))

print("")

# Der Garbage Collector
# =====================

print("GARBAGE COLLECTOR:")
print("")

import gc # Wird gebraucht, um auf den Garbage Collector zugreifen zu können

x = 2
del x
print(f"Garbage collector nach Erstellen und Löschen von Variable x: {gc.collect()} Objekte.")

class Node:
    def __init__(self):
        self.ref = None # Public Attribut der Klasse

# Erstellen zweier Objekte der Klasse 'Node':
obj1 = Node()
obj2 = Node()

# Create a cyclic reference
obj1.ref = obj2
obj2.ref = obj1

print(f"Garbage collector nach Anlegen der zwei Objekte mit gegenseitiger Referenzierung: {gc.collect()} Objekte.")

del obj1
del obj2

collected = gc.collect()
print(f"Garbage collector nach dem Löschen dieser beiden Objekte: {collected} Objekte.")