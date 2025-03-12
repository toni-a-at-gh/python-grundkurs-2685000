# Beispiel das demonstriert, dass manche Variablen (nämlich die änderbaren) doch
# per Funktion änderbar sind

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
print ("")
print("Nun folgt der Funktionsaufruf ...")
print("")
aendere_mutable_variable(meine_liste)
print(f"Nach Funktionsaufruf (mutable): {meine_liste}")
print(f"    Speicheradresse: {id(meine_liste)}")

# Hier wird "meine_liste" tatsächlich den Wert 100 hinzugefügt bekommen haben, obwohl
# in der Funktion "aendere_mutable_variable" NICHT mit einem Rückgabewert gearbeitet wurde.
# Grund ist, dass eine Variable vom Typ "List" eine veränderliche (mutable) Variable ist.