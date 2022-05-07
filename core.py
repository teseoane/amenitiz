'''File containing the main classes of the application.'''


class Product(object):

    def __init__(self, code, name, price):
        self.code = code
        self.name = name
        self.price = price

    def get_price_with_discount(self, amount):
        '''Return the price for certain amonunt of products.'''
        raise NotImplementedError
