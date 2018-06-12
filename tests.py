import unittest
from format_price import format_price


class FormatPriceTest(unittest.TestCase):
    def test_empty_price(self):
        self.assertIsNone(format_price(None))
        self.assertIsNone(format_price(''))
        self.assertIsNone(format_price(' '))

    def test_chars_in_string(self):
        self.assertIsNone(format_price('90O'))
        self.assertIsNone(format_price('100_0'))
        self.assertIsNone(format_price('10.0,0'))

    def test_digits_formatting(self):
        self.assertEqual(format_price(100), '100')
        self.assertEqual(format_price(100.), '100')
        self.assertEqual(format_price(1e2), '100')

    def test_strings_formatting(self):
        self.assertEqual(format_price('100'), '100')
        self.assertEqual(format_price('100.10'), '100.10')
        self.assertEqual(format_price('100,10'), '100.10')
        self.assertEqual(format_price('100.00'), '100')
        self.assertEqual(format_price('100000'), '100 000')
        self.assertEqual(format_price('100 000'), '100 000')
        self.assertEqual(format_price('25e-1'), '2.50')


if __name__ == '__main__':
    unittest.main()

