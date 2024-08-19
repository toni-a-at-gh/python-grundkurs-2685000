# Ping Pong Funktion
# Erstelle eine Funktion die als Parameter eine Zahl erhält.
# Ist die Zahl ein Vielfaches von 3, so soll die Funktion "Ping" zurückgeben. Ist
# die Zahl ein Vielfaches von 5, so soll die Funktion "Pong" zurückgeben. Ist die
# Zahl ein Vielfaches von 3 und 5, so soll die Funktion "Ping Pong" zurückgeben.
# Ansonsten gibt die Zahl zurück. Erstelle Unit Tests für die Funktion.
def ping_pong(zahl: int) -> str:
    """
    Überprüft, ob eine gegebene Zahl ein Vielfaches von 3, 5 oder beidem ist.
    Args:
        zahl (int): Die zu überprüfende Zahl.
    Returns:
        str: "Ping Pong", wenn die Zahl ein Vielfaches von 3 und 5 ist.
             "Ping", wenn die Zahl ein Vielfaches von 3 ist.
             "Pong", wenn die Zahl ein Vielfaches von 5 ist.
             Die Zahl als String, wenn sie kein Vielfaches von 3 oder 5 ist.
    """
    if zahl % 3 == 0 and zahl % 5 == 0:
        return "Ping Pong"
    elif zahl % 3 == 0:
        return "Ping"
    elif zahl % 5 == 0:
        return "Pong"
    else:
        return str(zahl)


# Listen Invertieren
# Erstelle eine Funktion die als Parameter eine Liste erhält. Die Funktion soll
# die Liste invertieren und zurückgeben. Beispiel: [1, 2, 3] -> [3, 2, 1].
# Erstelle Unit Tests für die Funktion.
def invertiere_liste(liste: list) -> list:
    """
    Invertiert eine gegebene Liste.
    Args:
        liste (list): Die zu invertierende Liste.
    Returns:
        list: Die invertierte Liste.
    """
    inverted_list = []
    for i in range(len(liste)):
        inverted_list.append(liste[len(liste) - i - 1])
    return inverted_list

# Finde den Höchsten zahlenwert Unabhängig vom Vorzeichen
# Erstelle eine Funktion die als Parameter eine Liste erhält. Die Funktion soll
# das Element mit dem größten Zahlenwert zurückgeben. Dabei soll der Vorzeichen
# nicht berücksichtigt werden. Beispiel: [1, -2, 3, -4] -> 4. Erstelle Unit Tests.
def finde_hoechsten_zahlenwert_unabhaengig_vom_vorzeichen(liste: list) -> int:
    """
    Findet das Element mit dem größten Zahlenwert in einer gegebenen Liste.
    Args:
        liste (list): Die Liste, in der das Element gefunden werden soll.
    Returns:
        int: Das Element mit dem größten Zahlenwert.
    """
    max_value = 0
    for element in liste:
        if abs(element) > max_value:
            max_value = abs(element)
    return max_value