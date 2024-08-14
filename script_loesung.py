#!/usr/bin/env python3

import argparse

# Verarbeiten von Befehlszeilenargumenten mit argparse

# ArgumentParser-Objekt erstellen
parser = argparse.ArgumentParser(description="Einfaches Beispiel für die Verwendung von argparse.")

# Argumente hinzufügen
parser.add_argument("--zahl1", type=float, help="Die erste Zahl", required=True)
parser.add_argument("--zahl2", type=float, help="Die zweite Zahl", required=True)
parser.add_argument("--operation", choices=["add", "sub", "mul", "div"], default="add", help="Die auszuführende Operation (add, sub, mul, div)")
parser.add_argument("--show_result", action="store_true", help="Flag damit Ergibnis ausgegeben wird")

# Argumente parsen
args = parser.parse_args()

# Berechnungen basierend auf den Argumenten
if args.operation == "add":
    result = args.zahl1 + args.zahl2
elif args.operation == "sub":
    result = args.zahl1 - args.zahl2
elif args.operation == "mul":
    result = args.zahl1 * args.zahl2
elif args.operation == "div":
    if args.zahl2 != 0:
        result = args.zahl1 / args.zahl2
    else:
        result = "Fehler: Division durch Null"
elif args.operation == "pow":
    result = args.zahl1 ** args.zahl2

# Ergebnis ausgeben
if args.show_result:
    print("Das Ergebnis ist:", result)

