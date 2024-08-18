def erhoehen_um_eins(x):
    return x + 1

def test_erhoehen_um_eins_correct():
    assert erhoehen_um_eins(3) == 4

def test_erhoehen_um_eins_incorrect():
    assert erhoehen_um_eins(3) == 5
    