from app.calculator import sum, resta, mult

def test_sum() -> None:
    assert sum(2, 3) == 5

# Introducir un fallo premeditado!
def test_resta() -> None:
    assert resta(5, 3) == 2

def test_mult() -> None:
    assert mult(2, 3) == 6