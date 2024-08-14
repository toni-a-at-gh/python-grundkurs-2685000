#!/usr/bin/env python3

# Schleifen in Python

# for-Schleife: Iteration über eine Liste von Zahlen
zahlen = [1, 2, 3, 4, 5]
for zahl in zahlen:
    print("Zahl aus der Liste:", zahl)

# for-Schleife: Iteration über einen Bereich (range)
for i in range(1, 6):
    print("Aktueller Wert von i:", i)

# while-Schleife: Solange eine Bedingung wahr ist
count = 0
while count < 5:
    print("count ist:", count)
    count = count + 1  # oder: count += 1

# while-Schleife mit einer Bedingung
n = 10
while n > 0:
    print("n ist:", n)
    n -= 2  # n um 2 verringern

# Aufgabe:
# Schreiben Sie eine for-Schleife, die über die Zahlen von 1 bis 10 iteriert 
# und jede Zahl ausgibt.

# Schreiben Sie außerdem eine while-Schleife, die bei 10 beginnt und 
# jede Zahl bis 1 ausgibt.
