#!usr/bin/env python3

#Schleifen in Python

#for-Schleife: Iteration über ein List von Zahlen:
zahlen = [1, 2, 3, 4, 5]
for zahl in zahlen:
  print("Zahl aus der Liste:", zahl)

#for-Schleife: Iteration über einen Bereich (range)
for i in range (1,6):
  print("Aktuelle Zahl: ", i)

#While-Schleife: Iterieren, solange eine Bedingung wahr ist
count = 0
while count < 5:
  print("Schleifenvariablenwert: ", count)
  count = count + 1

count =10
while count > 0:
    print("Schleifenvariablenwert: ", count)
    count -=2
