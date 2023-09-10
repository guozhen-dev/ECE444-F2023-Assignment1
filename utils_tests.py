import unittest
from utils import Utils

class TestUitls(unittest.TestCase):

    def test_reversed_int_positive(self):
        self.assertEqual(Utils.reversed(123456), 654321)
        self.assertEqual(Utils.reversed(123450), 54321)

    def test_reversed_int_negative(self):
        self.assertEqual(Utils.reversed(-123456), -654321)
        self.assertEqual(Utils.reversed(-123450), -54321)

    def test_reversed_int_zero(self):
        self.assertEqual(Utils.reversed(0), 0)
        self.assertEqual(Utils.reversed(-0), 0)

    def test_reversed_string_int(self):
        with self.assertRaises(AssertionError):
            Utils.reversed("123456")
        with self.assertRaises(AssertionError):
            Utils.reversed("-123456")
        with self.assertRaises(AssertionError):
            Utils.reversed("0")

    def test_reversed_string_float(self):
        with self.assertRaises(AssertionError):
            Utils.reversed("123.456")
        with self.assertRaises(AssertionError):
            Utils.reversed("-123.456")
        with self.assertRaises(AssertionError):
            Utils.reversed("0.00")

    def test_reversed_string_random(self):
        with self.assertRaises(AssertionError):
            Utils.reversed("Nv4Ug8WkY6")
        with self.assertRaises(AssertionError):
            Utils.reversed("7VesGwszfA")
        with self.assertRaises(AssertionError):
            Utils.reversed("ycfLooPAgz")

    def test_reversed_string_parseable(self):
        with self.assertRaises(AssertionError):
            Utils.reversed("0x123456")
        with self.assertRaises(AssertionError):
            Utils.reversed("0b101101")
        with self.assertRaises(AssertionError):
            Utils.reversed("01236613")

    def test_reversed_float(self):
        with self.assertRaises(AssertionError):
            Utils.reversed(123.456)
        with self.assertRaises(AssertionError):
            Utils.reversed(-123.456)
        with self.assertRaises(AssertionError):
            Utils.reversed(0.000)        
        with self.assertRaises(AssertionError):
            Utils.reversed(-0.000)

    def test_formatter_int_positive(self):
        self.assertEqual(Utils.formatter(123456), ('0b11110001001000000', '0o361100'))
        self.assertEqual(Utils.formatter(123450), ('0b11110001000111010', '0o361072'))

    def test_formatter_int_negative(self):
        self.assertEqual(Utils.formatter(-123456), ('-0b11110001001000000', '-0o361100'))
        self.assertEqual(Utils.formatter(-123450), ('-0b11110001000111010', '-0o361072'))

    def test_formatter_int_zero(self):
        self.assertEqual(Utils.formatter(0), ('0b0', '0o0'))
        self.assertEqual(Utils.formatter(-0), ('0b0', '0o0'))

    def test_formatter_string_int(self):
        with self.assertRaises(AssertionError):
            Utils.formatter("123456")
        with self.assertRaises(AssertionError):
            Utils.formatter("-123456")
        with self.assertRaises(AssertionError):
            Utils.formatter("0")

    def test_formatter_string_float(self):
        with self.assertRaises(AssertionError):
            Utils.formatter("123.456")
        with self.assertRaises(AssertionError):
            Utils.formatter("-123.456")
        with self.assertRaises(AssertionError):
            Utils.formatter("0.00")

    def test_formatter_string_random(self):
        with self.assertRaises(AssertionError):
            Utils.formatter("Nv4Ug8WkY6")
        with self.assertRaises(AssertionError):
            Utils.formatter("7VesGwszfA")
        with self.assertRaises(AssertionError):
            Utils.formatter("ycfLooPAgz")

    def test_formatter_string_parseable(self):
        with self.assertRaises(AssertionError):
            Utils.formatter("0x123456")
        with self.assertRaises(AssertionError):
            Utils.formatter("0b101101")
        with self.assertRaises(AssertionError):
            Utils.formatter("01236613")

    def test_formatter_float(self):
        with self.assertRaises(AssertionError):
            Utils.formatter(123.456)
        with self.assertRaises(AssertionError):
            Utils.formatter(-123.456)
        with self.assertRaises(AssertionError):
            Utils.formatter(0.000)        
        with self.assertRaises(AssertionError):
            Utils.formatter(-0.000)

if __name__ == '__main__':
    unittest.main()