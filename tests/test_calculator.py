import calclator


class TestCalculator:
    def test_addition(self):
        assert calclator.add(2, 2) == 4

    def test_subtraction(self):
        assert calclator.subtract(3, 1) == 2
