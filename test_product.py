import unittest

from core import Product


class ProductTestCase(unittest.TestCase):

    def setUp(self):
        self.product = Product('GR1', 'Green Tea', 3.11)

    def test_get_price_with_discount_not_implemented(self):
        self.assertRaises(NotImplementedError, self.product.get_price_with_discount, 1)
