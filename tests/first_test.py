import pytest
from app.calculator import Calculator


class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_multiply_calculate_correctly(self):
        assert self.calc.multiply(self, 2, 2) == 4

    def test_division_calulate_correctly(self):
        assert self.calc.division(self, 4, 2) == 2

    def test_subtract_calulate_correctly(self):
        assert self.calc.subtraction(self, 4, 2) == 2

    def test_adding_calulate_correctly(self):
        assert self.calc.adding(self, 2, 2) == 4

 # def test_multipyl_calculation_failed(self):
 #     assert self.calc.multiply(self, 2, 2) == 5




