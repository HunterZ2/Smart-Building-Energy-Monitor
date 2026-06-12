from src.power import calculate_power

def test_power():
    assert calculate_power(220, 10) == 2200
