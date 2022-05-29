import Item


class Basket(object):

    def __init__(self):
        self.__items = []

    def add_to_basket(self, item : Item):
        self.__items.append(item)

    def get_items(self):
        return self.__items