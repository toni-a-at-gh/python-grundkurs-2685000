# Klasse TasschenRechner
# Beispiel für eine Klasse, die eine einfache Taschenrechner-Funktionalität 
# bereitstellt. Die Klasse enthält die Methoden add, sub, mul und div. Bei
# der Division soll eine Division durch 0 abgefangen werden und eine Exception
# geworfen werden. Der Taschenrechner beinhaltet die letzeten drei Rechnungen
# Ergebnise in seinem Speicher und können abefragt werden.
# Die Klasse soll mit unit tests getestet werden.

class Taschenrechner:
    def __init__(self):
        self.memory = []

    def add_to_memory(self, result: str):
        if len(self.memory) >= 3:
            self.memory.pop(0)
        self.memory.append(result)

    def add(self, a: float, b: float) -> float:
        result = a + b
        self.add_to_memory(f"{a} + {b} = {result}")
        return result
    
    def sub(self, a: float, b: float) -> float:
        result = a - b
        self.add_to_memory(f"{a} - {b} = {result}")
        return result
    
    def mul(self, a: float, b: float) -> float:
        result = a * b
        self.add_to_memory(f"{a} * {b} = {result}")
        return result
    
    def div(self, a: float, b: float) -> float:
        if b == 0:
            raise ZeroDivisionError("Division durch 0 nicht möglich!")
        result = a / b
        self.add_to_memory(f"{a} / {b} = {result}")
        return result
    
    def get_memory(self) -> list:
        return self.memory