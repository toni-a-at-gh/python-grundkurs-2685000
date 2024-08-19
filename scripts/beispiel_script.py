# Implementierung eines Schere Stein Papier Spiels. Ein User spielt gegen den 
# Computer. Der Computer wählt zufällig ein Element. Der User wird aufgefordert
# ein Element zu wählen. Das Spiel läuft einmal durch. Dannach wird der Gewinner
# bekannt gegeben.
import random

def main():
    print("Willkommen beim Schere Stein Papier Spiel!")
    print("Wähle ein Element: Schere, Stein oder Papier.")
    user_choice = input("Deine Wahl: ")
    computer_choice = random.choice(["Schere", "Stein", "Papier"])
    print(f"Der Computer hat {computer_choice} gewählt.")
    if user_choice == computer_choice:
        print("Unentschieden!")
    elif user_choice == "Schere":
        if computer_choice == "Stein":
            print("Computer gewinnt!")
        else:
            print("Du gewinnst!")
    elif user_choice == "Stein":
        if computer_choice == "Papier":
            print("Computer gewinnt!")
        else:
            print("Du gewinnst!")
    elif user_choice == "Papier":
        if computer_choice == "Schere":
            print("Computer gewinnt!")
        else:
            print("Du gewinnst!")
    else:
        print("Ungültige Eingabe! Bitte wähle Schere, Stein oder Papier.")

if __name__ == "__main__":
    main()