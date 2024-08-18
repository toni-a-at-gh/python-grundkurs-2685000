def addition(a, b):
    return a + b

def subtraktion(a, b):
    return a - b

def multiplikation(a, b):
    return a * b

def division(a, b):
    if b != 0:
        return a / b
    else:
        raise ZeroDivisionError("Division durch Null ist nicht erlaubt.")

