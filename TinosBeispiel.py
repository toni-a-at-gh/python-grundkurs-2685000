# Veränderliche (mutable) Variablen in Python

# Hintergrund: Variablen sind in bestimmten Fällen nur änderbar.
# Zur Untersuchung kann die Funktion "id(meineListe)" genutzt werden, um die Speicheradresse
# einer Variablen meineListe zu bestimmen.

meineListe = [1, 2, 42] # Eine Variable vom Typ "Liste"
print("Variable meineListe vom Typ '" + str(type(meineListe)) + "': meineListe = " + str(meineListe) + ", Speicheradresse = " + str(id(meineListe)))
print(f"Variable meineListe: meineListe = {meineListe}, Speicheradresse = {id(meineListe)}")
meineListe.append(4)
print("Speicherardresse nach dem Hinzufügen eines Elements zu meineListe: " + str(id(meineListe)))
print("")

meinDict = {"a": 1, "b": 2} # Eine Variable vom Typ "Dictionary"
print("Variable meinDict vom Typ '" + str(type(meinDict)) + "': meinDict = " + str(meinDict) + ", Speicheradresse = " + str(id(meinDict)))
meinDict["c"] = 4
print("Variable meinDict nach dem Hinzufügen eines Elements': meinDict = " + str(meinDict) + ", Speicheradresse = " + str(id(meinDict)))

# Die Speicheradresse ist dann immer noch dieselbe!
# Dieses Verhalten trifft auf folgende Datentypen zu:
# - Listen (list)
# - Dictionaries (dict)
# - Mengen (set)
# - Bytearrays (bytearray)
# - Benutzerdefinierte Klassen