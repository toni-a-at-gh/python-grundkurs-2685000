# Implementiere einige pytest tests für genai_beispiele.funktionen_module.ping_pong
# Implementiere einige pytest tests für genai_beispiele.funktionen_module.invertiere_liste
# Implementiere einige pytest tests für genai_beispiele.funktionen_module.finde_hoechsten_zahlenwert_unabhaengig_vom_vorzeichen

import pytest
from genai_beispiele.funktionen_module import ping_pong, invertiere_liste, finde_hoechsten_zahlenwert_unabhaengig_vom_vorzeichen

def test_ping_pong():
    assert ping_pong(3) == "Ping"
    assert ping_pong(5) == "Pong"
    assert ping_pong(15) == "Ping Pong"
    assert ping_pong(7) == "7"

def test_invertiere_liste():
    assert invertiere_liste([1, 2, 3]) == [3, 2, 1]
    assert invertiere_liste([1, 2, 3, 4]) == [4, 3, 2, 1]
    assert invertiere_liste([1, 2]) == [2, 1]

def test_finde_hoechsten_zahlenwert_unabhaengig_vom_vorzeichen():
    assert finde_hoechsten_zahlenwert_unabhaengig_vom_vorzeichen([1, -2, 3, -4]) == 4
    assert finde_hoechsten_zahlenwert_unabhaengig_vom_vorzeichen([1, -2, 3, -4, 5]) == 5
    assert finde_hoechsten_zahlenwert_unabhaengig_vom_vorzeichen([1, -2, 3, -4, 5, -6]) == 6


