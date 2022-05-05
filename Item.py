class Item(object):
    name = ""
    price = 0.0
    rating = None
    num_of_reviews = 0

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def add_review(self, rating):
        if self.num_of_reviews > 0:
            self.rating = ((self.rating * self.num_of_reviews) + rating) / (self.num_of_reviews + 1)
        else:
            self.rating = rating
        self.num_of_reviews = self.num_of_reviews + 1
