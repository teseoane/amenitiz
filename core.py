'''File containing the main classes of the application.'''


class Product(object):

    def __init__(self, code, name, price):
        self.code = code
        self.name = name
        self.price = price

    def get_price_with_discount(self, amount):
        '''Return the price for certain amonunt of products.'''
        raise NotImplementedError


class ProductCEO(Product):

    def get_price_with_discount(self, amount):
        '''Return the price with buy-one-get-one-free discount.'''
        if amount == 1:
            return self.price
        return self.price * (amount // 2 + amount % 2)


class ProductCOO(Product):

    def __init__(self, code, name, price, price_with_discount):
        super().__init__(code, name, price)
        self.price_with_discount = price_with_discount

    def get_price_with_discount(self, amount):
        '''If you buy 3 or more the price drops.'''
        if amount < 3:
            return self.price * amount
        return self.price_with_discount * amount
