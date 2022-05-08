'''File containing the shopping cart class.'''


class Cart(object):
    products = {}

    def __init__(self):
        self.products = {}

    def add(self, product):
        if product.code in self.products.keys():
            self.products[product.code]['amount'] += 1
        else:
            self.products[product.code] = {
                'instance': product,
                'amount': 1
            }

    def get_total(self):
        total = 0
        for code in self.products:
            total += self.products[code]['instance'].get_price_with_discount(self.products[code]['amount'])
        return total
