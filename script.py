#!/usr/bin/env python3

# Einführung in das Memory Management bei mutable Variablen in Python. Mutable
# Das bedeutet, dass ihre Inhalte nach der Erstellung geändert werden können, 
# ohne dass eine neue Speicheradresse verwendet wird.

# Erstellen einer Liste
liste = [1, 2, 3]
print(f"Liste: {liste}, Speicheradresse: {id(liste)}")

# Änderung der Liste: Einfügen eines Elements
liste.append(4)
print(f"Liste nach Änderung: {liste}, Speicheradresse: {id(liste)}")

# Erstellen eines Dictionaries
dictionary = {"a": 1, "b": 2}
print(f"Dictionary: {dictionary}, Speicheradresse: {id(dictionary)}")

# Änderung des Dictionaries: Hinzufügen eines neuen Schlüssels
dictionary["c"] = 3
print(f"Dictionary nach Änderung: {dictionary}, Speicheradresse: {id(dictionary)}")

# Mutable Datentypen:
# - Listen (list)
# - Dictionaries (dict)
# - Mengen (set)
# - Bytearrays (bytearray)
# - Benutzerdefinierte Klassen