#!/usr/bin/env python3

import argparse

parser = argparse.ArgumentParser(description="Beispiel für argparse")
parser.add_argument("pflicht_int", help="Integer der erforderlich ist", type=int)
parser.add_argument("--optional_int", help="Optionaler Integer", type=int)
parser.add_argument("--optional_str", help="Optionaler String")
parser.add_argument("--wahl", help="Meine Wahl", choices=["a", "b", "c", "d"])
args = parser.parse_args()

print("Integer:", args.pflicht_int, "- Typ:", type(args.pflicht_int))
print("Optional Integer:", args.optional_int)
print("Optional String:", args.optional_str, "- Type:", type(args.optional_str))
print("Wahl:", args.wahl)

# Aufgabe: Erstellen Sie ein Skript, das die Länge eines Textes analysiert und Informationen darüber liefert.

# Das Skript soll folgende Funktionalität bieten:
# 1. Ein Pflichtargument (positional argument), das einen Text entgegennimmt.
# 2. Ein optionales Argument --details, das zusätzliche Informationen liefert:
#    - Anzahl der Zeichen
#    - Anzahl der Wörter
# 3. Wenn das Argument --details nicht angegeben wird, soll nur die Anzahl der Zeichen ausgegeben werden.

# Beispiel:
# python3 script.py "Dies ist ein Beispieltext." --details
# Ausgabe:
# Zeichen: 27
# Wörter: 5

# Optional: Erweitern Sie das Skript, um auch die Anzahl der Vokale und Konsonanten zu zählen.
