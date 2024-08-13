#!/usr/bin/env python3

# Bedingte Anweisungen in Python

# Variablen
x = 10
y = 5

# Einfache if-Bedingung
if x > y:
    print("x ist größer als y")

# if-else-Bedingung
if x <= y:
    print("x ist kleiner als y")
else:
    print("x ist nicht kleiner als y")

# if-elif-else-Bedingung
if x == y:
    print("x ist gleich y")
elif x > y:
    print("x ist größer als y")
else:
    print("x ist kleiner als y")

# Aufgabe:
# Legen Sie zwei Variablen mit verschiedenen float Zahlenwerten an.
# Schreiben Sie eine if-else-Bedingung, die prüft, ob die erste Zahl 
# größer gleich oder kleiner der zweiten Zahl ist, und geben Sie das 
# entsprechende Ergebnis aus.

z = 15
# and-Verknüpfung: Beide Bedingungen müssen wahr sein
if x > y and x < z:
    print("x ist größer als y und kleiner als z")

# or-Verknüpfung: Eine der beiden Bedingungen muss wahr sein
if x < y or x < z:
    print("x ist entweder kleiner als y oder kleiner als z")

# Aufgabe:
# Legen Sie drei Variablen mit verschiedenen Zahlenwerten an.
# Schreiben Sie eine if-Bedingung mit einer and-Verknüpfung und eine mit einer or-Verknüpfung,
# die bestimmte Bedingungen überprüft und entsprechende Nachrichten ausgibt.
