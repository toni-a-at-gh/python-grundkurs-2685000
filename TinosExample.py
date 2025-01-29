#!/usr/bin/env python3

# Importieren des Moduls argparse, das das Verarbeiten von Argumenten ermöglicht:
import argparse

# Name des Skripts in eine Variable schreiben
scriptName = "TinosExample.py"

# Start des Skripts
print("Start von " + scriptName)

# Anlegen eines neuen ArgumentParser-Objekts:

# Hinweis: der String in "description" wird als Hilfe angezeigt, wenn das Skript
# mittels "-h" Argument aufgerufen wird
parser = argparse.ArgumentParser(description="Dies ist eine einfache Taschenrechner-App")

# Definieren von sog. "Pflichtparametern":
parser.add_argument()

# Einlesen der Argumente bei Skriptstart:
args = parser.parse_args()

# Ergebnis ausgeben:
print("Ende von " + scriptName)
