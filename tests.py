import unittest
from format_price import format_price


class FormatPriceTest(unittest.TestCase):
    def test_price_none(self):
        self.assertIsNone(format_price(None))

    def test_price_empty(self):
        self.assertIsNone(format_price(''))

    def test_price_space(self):
        self.assertIsNone(format_price(' '))

    def test_price_chars_in_string(self):
        self.assertIsNone(format_price('90O'))

    def test_price_comma_in_string(self):
        self.assertIsNone(format_price('10.0,0'))

    def test_price_digits_int_formatting(self):
        self.assertEqual(format_price(100), '100')

    def test_price_digits_float_formatting(self):
        self.assertEqual(format_price(100.), '100')

    def test_price_digits_exp_formatting(self):
        self.assertEqual(format_price(1e2), '100')

    def test_price_strings_formatting_int(self):
        self.assertEqual(format_price('100'), '100')

    def test_price_strings_formatting_fract(self):
        self.assertEqual(format_price('100.10'), '100.10')

    def test_price_strings_formatting_float(self):
        self.assertEqual(format_price('100.00'), '100')

    def test_price_strings_formatting_digit_dense(self):
        self.assertEqual(format_price('100000'), '100 000')

    def test_price_strings_formatting_digit_sparse(self):
        self.assertEqual(format_price('100 000'), '100 000')

    def test_price_strings_formatting_digit_exp(self):
        self.assertEqual(format_price('25e-1'), '2.50')

    def test_price_string_bool(self):
        self.assertIsNone(format_price('True'))

    def test_price_bool(self):
        self.assertIsNone(format_price(True))


if __name__ == '__main__':
    unittest.main()
