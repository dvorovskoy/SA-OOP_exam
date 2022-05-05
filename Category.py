import Item


class Category(object):

    name = ""

    items = []

    def __init__(self, name, items):
        self.name = name
        self.items = items

    def add_to_category(self, item):
        self.items.append(item)

    def add_all_to_category(self, items):
        for item in items:
            self.add_to_category(item)