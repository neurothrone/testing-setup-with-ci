import pytest

import calculator


class TestCalculator:
    def test_addition(self):
        assert calculator.add(2, 2) == 4

    def test_subtraction(self):
        assert calculator.subtract(3, 1) == 2

    def test_division(self):
        assert calculator.divide(5, 5) == 1.0

    def test_division_division_by_zero(self):
        with pytest.raises(ZeroDivisionError):
            calculator.divide(5, 0)

    def test_multiplication(self):
        assert calculator.multiply(3, 5) == 15
