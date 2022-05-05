from Basket import Basket
from Item import Item


class User(object):
    login = ""
    password = ""
    basket = Basket()

    def __init__(self, login, password):
        self.login = login
        self.password = password

    def add_to_basket(self, item: Item):
        self.basket.add_to_basket(item)
