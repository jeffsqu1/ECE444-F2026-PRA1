import unittest

from utils import utils


class TestUtils(unittest.TestCase):
	def setUp(self):
		self.utility = utils()

	def test_reversed_with_integer(self):
		self.assertEqual(self.utility.reversed(12345), 54321) # expects 54321

	def test_reversed_with_string(self):
		with self.assertRaises(TypeError): # expects a TypeError
			self.utility.reversed("12345")

	def test_reversed_with_float(self):
		with self.assertRaises(TypeError): # expects a TypeError
			self.utility.reversed(123.45)

	def test_formatter_with_integer(self):
		self.assertEqual(self.utility.formatter(10), ("0b1010", "0o12")) # expects 0b1010, 1o12

	def test_formatter_with_string(self):
		with self.assertRaises(TypeError): # expects a TypeError
			self.utility.formatter("10")

	def test_formatter_with_float(self):
		with self.assertRaises(TypeError): # expects a TypeError
			self.utility.formatter(10.5)


if __name__ == "__main__":
	unittest.main()
