#!/usr/bin/env python3

# Die Aufgabenstellung:

# Aufgabe: Programmieren Sie einen Taschenrechner mit ausgelagerten Funktionen.

# 1. Erstellen Sie für jede der Grundrechenarten (Addition, Subtraktion, Multiplikation, Division) eine separate Funktion.
#    - Jede Funktion sollte zwei Argumente (Zahlen) als Eingabe akzeptieren und das Ergebnis der Berechnung zurückgeben.
#    - Die Funktionen sollten klar benannt und gemäß PEP8 formatiert sein.

# 2. Implementieren Sie eine Hauptfunktion (main), die:
#    - Den Benutzer auffordert, zwei Zahlen einzugeben.
#    - Den Benutzer auffordert, die gewünschte Operation auszuwählen (Addition, Subtraktion, Multiplikation, Division).
#    - Die entsprechende Rechenfunktion aufruft und das Ergebnis ausgibt.
#    - Eine Fehlerbehandlung integriert, um ungültige Eingaben und Division durch Null zu vermeiden.

# 3. Stellen Sie sicher, dass Ihr Code PEP8-konform ist:
#    - Verwenden Sie vier Leerzeichen für Einrückungen.
#    - Fügen Sie Leerzeichen um Operatoren ein.
#    - Halten Sie Zeilenlängen unter 79 Zeichen.
#    - Schreiben Sie geeignete Kommentare und verwenden Sie docstrings für Funktionen.

# Beispielablauf:
# - Der Benutzer gibt die Zahlen 10 und 5 ein.
# - Der Benutzer wählt die Operation 'Multiplikation'.
# - Die Funktion zur Multiplikation wird aufgerufen und das Ergebnis (50) wird ausgegeben.

# Optional:
# - Fügen Sie weitere Funktionen hinzu, wie z.B. Potenzierung oder Modulo.
# - Implementieren Sie eine Schleife, um mehrere Berechnungen hintereinander durchzuführen, bis der Benutzer das Programm beendet.

# Gewollte Änderungen im Vergleich zur Lösung:
# Es wurde nicht "Pylint" laufen gelassen, um auf PEP8 zu prüfen, sondern, es wurde RUFF nebenher laufen gelassen. Grund:
# das nutzen wir auch im CAS-Projekt.

import os  # Wird gebraucht, um die Konsole leeren zu können


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
        operator = str(input("Bitte den Operator wählen ('+', '-', '*', '/')"))
        if operator == "+":
            ergebnis, istOk = Addieren(number1, number2)
            print(
                "Ergebnis: "
                + str(number1)
                + " + "
                + str(number2)
                + " = "
                + str(ergebnis)
            )
        elif operator == "-":
            ergebnis, istOk = Subtrahieren(number1, number2)
            print(
                "Ergebnis: "
                + str(number1)
                + " - "
                + str(number2)
                + " = "
                + str(ergebnis)
            )
        elif operator == "*":
            ergebnis, istOk = Multiplizieren(number1, number2)
            print(
                "Ergebnis: "
                + str(number1)
                + " * "
                + str(number2)
                + " = "
                + str(ergebnis)
            )
        elif operator == "/":
            ergebnis, istOk = Dividieren(number1, number2)
            if istOk:
                print(
                    "Ergebnis: "
                    + str(number1)
                    + " / "
                    + str(number2)
                    + " = "
                    + str(ergebnis)
                )
            else:
                print("Division durch Null ist nicht erlaubt!")
        else:
            print("Bitte gültigen Operator angeben!")
    finally:
        return


# Hier ist der Code, der eigentlich bei Aufruf des Skripts ausgewertet wird.
# Das folgende Konstrukt soll sicherstellen, dass die Funktion main() aufgerufen wird,
# wenn das Skript direkt ausgeführt wird und nicht als Modul eingebunden wird. Die Variable
# __name__ ist eine spezielle Variable in Python. Sie erhält automatisch den Wert "__main__",
# sobald das Skript direkt aufgerufen wird. Wird jedoch das Skript als Modul in einem anderen
# Skript eingebunden, hat sie den Wert des Namens des Moduls, also (wahrscheinlich?)
# "TinosBeispiel"
if __name__ == "__main__":
    main()
