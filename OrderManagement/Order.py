class Order:
    def __init__(self, order_id, products):
        self.order_id = order_id
        self.products = products
        self.total = self.find_total()

    def find_total(self):
        total = 0
        for i in self.products:
            total += i['price'] * i['quatity']
        return total

products = [
    {'name': 'Baby Tee', 'price': 100, 'quatity': 1},
    {'name': 'Sweater', 'price': 300, 'quatity': 2},
    {'name': 'Long Skirt', 'price': 250, 'quatity': 1}
]

order = Order('A12345', products)
print('Total:', order.total)