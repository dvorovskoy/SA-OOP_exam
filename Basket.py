import Item


class Basket(object):

    items = []

    def add_to_basket(self, item : Item):
        self.items.append(item)
