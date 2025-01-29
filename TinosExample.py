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
parser.add_argument("linkerOperator", help="Linker Operator", type=float)
parser.add_argument("rechterOperator", help="Rechter Operator", type=float)
parser.add_argument("Operand", help="Operand ('+', '-', '*' oder '/')", choices=["+", "-", "*","/"])

# Definieren von optionalen Parametern:
parser.add_argument("--GleichungSchreiben", help="True: Gleichung wird ausgegeben. False: Nur Ergebnis wird ausgegeben.", type=int)

# Einlesen der Argumente bei Skriptstart:
args = parser.parse_args()

# Ausgeben der eingegeben Argumente:
print("Die folgenden Argumente wurden eingegeben: " + str(args.linkerOperator) + " " + str(args.rechterOperator) + " " + str(args.Operand) + " " + str(args.GleichungSchreiben))

# Berechnen und ausgeben:
if args.Operand == "+":
  if bool(args.GleichungSchreiben) == True:
    print("Das Ergebnis lautet: " + str(float(args.linkerOperator))+ " + " + str(float (args.rechterOperator)) + " = " + str(float(args.linkerOperator) + float (args.rechterOperator)))
  else:
    print("Das Ergebnis lautet " + str(float(args.linkerOperator) + float (args.rechterOperator)))
elif args.Operand == "-":
  if bool(args.GleichungSchreiben) == True:
   print("Das Ergebnis lautet: " + str(float(args.linkerOperator))+ " - " + str(float (args.rechterOperator)) + " = " + str(float(args.linkerOperator) - float (args.rechterOperator)))
  else:
   print("Das Ergebnis lautet " + str(float(args.linkerOperator) - float (args.rechterOperator)))
elif args.Operand == "*":
  if bool(args.GleichungSchreiben) == True:
    print("Das Ergebnis lautet: " + str(float(args.linkerOperator))+ " * " + str(float (args.rechterOperator)) + " = " + str(float(args.linkerOperator) * float (args.rechterOperator)))
  else:
   print("Das Ergebnis lautet " + str(float(args.linkerOperator) * float (args.rechterOperator)))
elif args.Operand == "/":
   if bool(args.GleichungSchreiben) == True:
    print("Das Ergebnis lautet: " + str(float(args.linkerOperator))+ " / " + str(float (args.rechterOperator)) + " = " + str(float(args.linkerOperator) / float (args.rechterOperator)))
   else:
    print("Das Ergebnis lautet " + str(float(args.linkerOperator) / float (args.rechterOperator)))
else:
  print("Der Operator wird nicht untersützt.")

# Ergebnis ausgeben:
print("Ende von " + scriptName)

# 2025-01-29: HIER WEITERMACHEN: Das optionale Argument wird nicht erkannt als bool
