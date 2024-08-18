from aufgaben_package.personen import Person

def test_person_init():
    person = Person("Alice", 25)
    assert person.name == "Alice"
    assert person.alter == 25

def test_person_str():
    person = Person("Bob", 30)
    assert str(person) == "Bob (30)"