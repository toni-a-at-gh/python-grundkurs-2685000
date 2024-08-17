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