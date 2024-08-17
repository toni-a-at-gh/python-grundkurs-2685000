import pytest
from python_grund_kurs.kategorien import KategorieManager

@pytest.fixture
def kategorie_manager():
    # Create an instance of KategorieManager for testing
    return KategorieManager()

def test_kategorie_manager_fuege_kategorie_hinzu(kategorie_manager):
    # Test adding a new kategorie
    kategorie_manager.fuege_kategorie_hinzu("Category 1")
    assert "Category 1" in kategorie_manager.kategorien

def test_kategorie_manager_loesche_kategorie(kategorie_manager):
    # Test removing an existing kategorie
    kategorie_manager.fuege_kategorie_hinzu("Category 2")
    kategorie_manager.loesche_kategorie("Category 2")
    assert "Category 2" not in kategorie_manager.kategorien

def test_kategorie_manager_get_kategorien(kategorie_manager):
    # Test getting all kategorien
    kategorie_manager.fuege_kategorie_hinzu("Category 3")
    kategorie_manager.fuege_kategorie_hinzu("Category 4")
    assert len(kategorie_manager.get_kategorien()) == 2