#!/usr/bin/env python3

# Die Aufgabenstellung in Branch "05_05-Bankkt-Bsp-mit-Vererb-als-Prj":

# Das Ergebnis aus Branch "03_12-Bankkonto-Bsp-mit-Vererbg" soll so umgebaut werden,
# dass es ein strukturiertes Projekt ergibt. Dort enthielt die Datei "TinosBeispiel.py"
# alles: die Klassendefinitionen "BankAccount" und "Jugendkonto", sowie die Hauptfunktion
# "main()". Dieser Spaghetticode soll in ein strukturiertes Projekt überführt werden.
# Das heißt:
# - Es soll ein Package "src/bank_account" erstellt werden
# - Dieses Package soll zwei Module beinhalten:
#   + M1: Implementierung der Klasse "BankAccount"
#   + M2: Implementierung der Klasse "Jugendkonto"
# - Dieses Package soll außerdem ein Skript beinhalten, das die Hauptfunktion enthält
# - Es soll auch die "pyproject.toml" enthalten

# ******************************************************************************************
# HINWEIS: 
#
# Das Skript "scr/banksimulation.py" ist das eigentliche Hauptskript, das aufgerufen werden
# muss. Es ist nur aber lauffähig, wenn zuvor das Projekt "bank_account" per "pip install ." 
# auf Ebene, in der sich die "pyproject.toml" befindet, installiert wurde. Das wurde getestet.
#
# ******************************************************************************************


