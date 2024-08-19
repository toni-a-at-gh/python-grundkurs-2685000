# Implementiert die Usereingabe und die Ausgabe der Ergebnisse in der Konsole
# für den Taschenrechner in der Klasse TasschenRechner. Das Script soll dauerhaft
# laufen und der User soll kann die Rechenoperationen und zwei Eingabewerte wählen.
# Der User das Script über den Befehlt "exit" beenden. Der User kann den Speicher
# des Taschenrechners über den Befehlt "memory" ausgeben lassen.

from genai_beispiele.taschen_rechner import Taschenrechner

def main():
    calculator = Taschenrechner()
    while True:
        user_input = input("Bitte geben Sie 'exit', 'memory', oder eine Rechenoperation und zwei Zahlen ein: ")
        if user_input == "exit":
            break
        elif user_input == "memory":
            for memory_entry in calculator.get_memory():
                print(memory_entry)
        else:
            try:
                a, operation, b = user_input.split()
                a = float(a)
                b = float(b)
                if operation == "+":
                    result = calculator.add(a, b)
                    print(f"{a} + {b} = {result}")
                elif operation == "-":
                    result = calculator.sub(a, b)
                    print(f"{a} - {b} = {result}")
                elif operation == "*":
                    result = calculator.mul(a, b)
                    print(f"{a} * {b} = {result}")
                elif operation == "/":
                    result = calculator.div(a, b)
                    print(f"{a} / {b} = {result}")
                else:
                    print("Ungültige Rechenoperation! Bitte wählen Sie +, -, * oder /.")
            except ValueError:
                print("Ungültige Eingabe! Bitte geben Sie eine Rechenoperation und zwei Zahlen ein.")


if __name__ == "__main__":
    main()