from Basket import Basket
from Item import Item


class User(object):

    def __init__(self, login, password):
        self.__login = login
        self.__password = password
        self.__basket = Basket()

    def add_to_basket(self, item: Item):
        self.__basket.add_to_basket(item)

    def get_login(self):
        return self.__login

    def get_password(self):
        return self.__password

    def get_basket(self):
        return self.__basket