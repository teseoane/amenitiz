'''File containing the shopping cart class.'''


class Cart(object):
    products = {}

    def add(self, product):
        if product.code in self.products.keys():
            self.products[product.code]['amount'] += 1
        else:
            self.products[product.code] = {
                'instance': product,
                'amount': 1
            }
