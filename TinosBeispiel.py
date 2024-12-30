#!/usr/bin/env python3

# Tinos Taschenrechner

# Aufgabenbeschreibung:
# Der Benutzer sollte aufgefordert werden, zwei Zahlen einzugeben.
# Anschließend sollte der Benutzer die gewünschte Operation wählen können.

# Beispielablauf:
# 1. Benutzer gibt die erste Zahl ein.
# 2. Benutzer gibt die zweite Zahl ein.
# 3. Benutzer wählt die Operation (+, -, *, /).
# 4. Das Programm führt die Berechnung durch und gibt das Ergebnis aus.

# Optional: Erweitern Sie den Taschenrechner um weitere Funktionen wie Potenzierung oder Modulo.

a = input("Bitte geben Sie den linken Operanden ein: ")
b = input("Bitte geben Sie den rechten Operanden ein: ")
Operator = input("Bitte geben Sie einen der folgenden Operatoren ein: '+', '-', '*', '/', 'mod': ")
if Operator == "+":
  print("Das Ergebnis lautet " + str(float(a) + float (b)))
elif Operator == "-":
  print("Das Ergebnis lautet " + str(float(a) - float(b)))
elif Operator == "*":
  print("Das Ergebnis lautet " + str(float(a) * float (b)))
elif Operator == "/":
  print("Das Ergebnis lautet " + str(float(a)/ float(b)))
elif Operator == "mod":
  print("Das Ergebnis lautet " + str(float(a) % float(b)))
else:
  print("Der Operator wird nicht untersützt.")