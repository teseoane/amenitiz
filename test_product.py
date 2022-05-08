import unittest

from core import Product
from core import ProductCEO


class ProductTestCase(unittest.TestCase):

    def test_get_price_with_discount_not_implemented(self):
        product = Product('SOME_CODE', 'Product Name', 99)
        self.assertRaises(NotImplementedError, product.get_price_with_discount, 1)

    def test_product_ceo_get_price_with_discount(self):
        product_ceo = ProductCEO('GR1', 'Green Tea', 3.11)
        self.assertEqual(product_ceo.get_price_with_discount(0), 0)
        self.assertEqual(product_ceo.get_price_with_discount(1), 3.11)
        self.assertEqual(product_ceo.get_price_with_discount(2), 3.11)
        self.assertEqual(product_ceo.get_price_with_discount(3), 6.22)
