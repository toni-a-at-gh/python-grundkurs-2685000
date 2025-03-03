#!/usr/bin/env python3

# Definition der Funktion:
def Differenz(op1: int, op2: int) -> int:
    return op1 - op2


# Aufruf der Funktion mit Argumenten vom Typ int:
operator1: int = 23
operator2: int = 5
print(
    "Die Differenz von ",
    operator1,
    " und",
    operator2,
    " lautet ",
    Differenz(operator1, operator2),
)

# Aufruf der Funktion mit Argumenten vom Typ float:
operator3: float = 20
operator4: float = 6
print(
    "Die Differenz von ",
    operator3,
    " und",
    operator4,
    " lautet ",
    Differenz(operator3, operator4),
)
