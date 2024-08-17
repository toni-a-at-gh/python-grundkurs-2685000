class KategorieManager:
    """ 
    Verwaltet Kategorien von Aufgaben
    """
    def __init__(self):
        self.kategorien = []

    def fuege_kategorie_hinzu(self, kategorie_name: str):
        if kategorie_name not in self.kategorien:
            self.kategorien.append(kategorie_name)
    
    def loesche_kategorie(self, kategorie_name: str):
        if kategorie_name in self.kategorien:
            self.kategorien.remove(kategorie_name)

    def get_kategorien(self):
        return self.kategorien
    
    def __str__(self):
        return f"Kategorien: {self.kategorien}"
    