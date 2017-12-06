from ..brewer.strike_temp_calculator import calc_strike_temp
import unittest

class StrikeTempCalculator(unittest.TestCase):

    def test_calc_strike_temp(self):
        assert calc_strike_temp(14, 8, 89, 150) == 157.0
        assert not calc_strike_temp(14, 8, 89, 150) == 162.0

    def test_calc_strike_temp_with_wrong_args(self):
        with self.assertRaises(TypeError):
            calc_strike_temp(50, 25)
            calc_strike_temp(50, 25, 150, "string")
