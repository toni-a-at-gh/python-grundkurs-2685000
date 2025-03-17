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

# Ab der folgenden Codezeile steht deshalb u.U. noch originaler Code aus dem Branch
# "03_12-Bankkonto-Bsp-mit-Vererbg".

# Die Aufgabenstellung:

# Aufgabe: Erstellen Sie ein neues Jugendbankkonto, dass von der Klasse
# BankAccount erbt und beschränken sie die Abhebungen auf maximal 25€.

# Hinweis in eigener Sache: für dieses Beispiel erweitere ich die von mir erstellte Klasse
# (siehe Branch 03_08-Bankkonto-Bsp), nicht die von der Trainingsleiterin. Grund: ich hatte schon
# einiges mehr ergänzt, z.B. Kommandozeile leeren


