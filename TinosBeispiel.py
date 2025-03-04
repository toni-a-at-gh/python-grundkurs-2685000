#!/usr/bin/env python3

import os


# Definition der Funktionen:
def Subtrahieren(op1: float, op2: float) -> (float, bool):
    """Subtraktion von zwei Operatoren"""
    return (op1 - op2), True


def Addieren(op1: float, op2: float) -> (float, bool):
    """Addition von zwei Operatoren"""
    return (op1 + op2), True


def Multiplizieren(op1: float, op2: float) -> (float, bool):
    """Multiplikation von zwei Opertoren"""
    return (op1 * op2), True


def Dividieren(op1: float, op2: float) -> (float, bool):
    """Dividieren von zwei Operatoren"""
    ValideOperation = True
    try:
        # Code, der potenziell zu einem Problem führen könnte
        # (hier: Division durch Null):
        Ergebnis = op1 / op2
    except ZeroDivisionError:
        # Code, der ausgeführt wird, wenn der Fehler "ZeroDivisionError"
        # geworfen wird:
        ValideOperation = False
        Ergebnis = 0
    else:
        # Code, der ausgeführt wird, wenn kein Fehler auftritt:
        ValideOperation = True
    finally:
        # Code, der immer ausgeführt wird
        return Ergebnis, ValideOperation


def main():
    """Hauptfunktion des Taschenrechners"""
    os.system("cls")  # löscht den Konsoleninhalt für ein besseres User Experience
    print("TASCHENRECHNER")
    try:
        number1 = float(input("Geben Sie die erste Zahl ein: "))
        number2 = float(input("Geben Sie die zweite Zahl ein: "))
    except ValueError:
        # Exception wird geworfen, wenn die eingegebenen Zahlen nicht in Float
        # umgewandelt werden können
        print("Bitte Zahlen eingeben!")
    else:
        print("Sie haben " + str(number1) + " und " + str(number2) + " eingegeben.")


# Sicherstellen, dass die Funktion main() aufgerufen wird, wenn das Skript direkt ausgeführt
# wird und nicht als Modul eingebunden wird. Die Variable __name__ ist eine spezielle Variable
# in Python. Sie erhält automatisch den Wert "__main__", sobald das Skript direkt aufgerufen
# wird. Wird jedoch das Skript als Modul in einem anderen Skript eingebunden, hat sie den Wert
# des Namens des Moduls, also (wahrscheinlich?) "TinosBeispiel"
if __name__ == "__main__":
    main()
