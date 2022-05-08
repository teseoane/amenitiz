import unittest

from core import Product
from core import ProductCEO
from core import ProductCOO


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

    def test_product_coo_get_price_with_discount(self):
        product_coo = ProductCOO('SR1', 'Strawberries', 5, 4.5)
        self.assertEqual(product_coo.get_price_with_discount(0), 0)
        self.assertEqual(product_coo.get_price_with_discount(1), 5)
        self.assertEqual(product_coo.get_price_with_discount(2), 10)
        self.assertEqual(product_coo.get_price_with_discount(3), 13.5)
        self.assertEqual(product_coo.get_price_with_discount(4), 18)
