import Item


class Category(object):

    def __init__(self, name, items):
        self.__name = name
        self.__items = items

    def add_to_category(self, item):
        self.__items.append(item)

    def add_all_to_category(self, items):
        for item in items:
            self.add_to_category(item)

    def get_items(self):
        return self.__items

    def get_name(self):
        return self.__name