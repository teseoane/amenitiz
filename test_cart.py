import unittest

from cart import Cart
from product import ProductCEO
from product import ProductCOO
from product import ProductVP


class CartTestCase(unittest.TestCase):

    def setUp(self):
        self.cart = Cart()
        self.product_ceo = ProductCEO('GR1', 'Green Tea', 3.11)
        self.product_coo = ProductCOO('SR1', 'Strawberries', 5, 4.5)
        self.product_vp = ProductVP('CF1', 'Coffee', 11.23)

    def test_add_product(self):
        self.cart.add(self.product_ceo)
        self.assertEqual(self.cart.products[self.product_ceo.code]['amount'], 1)
        self.cart.add(self.product_ceo)
        self.cart.add(self.product_coo)
        self.assertEqual(self.cart.products[self.product_ceo.code]['amount'], 2)
        self.assertEqual(self.cart.products[self.product_coo.code]['amount'], 1)
