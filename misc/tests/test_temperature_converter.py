# test for misc.temperature_converter module
from misc.temperature_converter import TemperatureConverter
import unittest

class TestTemperatureConverter(unittest.TestCase):

    def test_celsius_to_fahrenheit(self):
        self.assertEqual(TemperatureConverter.celsius_to_fahrenheit(0), 32)
        self.assertEqual(TemperatureConverter.celsius_to_fahrenheit(100), 212)

    def test_fahrenheit_to_celsius(self):
        self.assertEqual(TemperatureConverter.fahrenheit_to_celsius(32), 0)
        self.assertEqual(TemperatureConverter.fahrenheit_to_celsius(212), 100)
