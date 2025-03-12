import sys # Wird gebraucht, um den Reference Counter ausgeben lassen zu können

# Der Reference Counter
# =====================

x = [1, 2, 3] # Eine Variable vom Typ "Liste"
print("Liste x: " + str(x))
print("Wert des Reference Counters für x: " + str(sys.getrefcount(x)))
# Hinweis: der Wert des Counters ist nicht 1, wie vielleich zu erwarten wäre, weil ja nur ein Objekt 'x'
# angelegt wurde. Er hat den Wert 2, was durch den Funktionsaufruf 'sys.getrefcount(x)' kommt

print("")
y = [4, 5, 6]
print("Liste y: " + str(y))
y.append(x) # Fügt die Liste x an das Ende von Liste y an
print("Liste x nach dem Hizufügen von Liste y: " + str(y))

# HIER WEITERMACHEN