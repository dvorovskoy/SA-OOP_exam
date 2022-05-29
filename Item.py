class Item(object):

    def __init__(self, name, price):
        self.__name = name
        self.__price = price
        self.__rating = None
        self.__num_of_reviews = 0

    def add_review(self, rating):
        if self.__num_of_reviews > 0:
            self.__rating = ((self.__rating * self.__num_of_reviews) + rating) / (self.__num_of_reviews + 1)
        else:
            self.__rating = rating
        self.__num_of_reviews = self.__num_of_reviews + 1

    def get_name(self):
        return self.__name

    def get_rating(self):
        return self.__rating

    def get_price(self):
        return self.__price