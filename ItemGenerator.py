import random

from Item import Item

categories = ["Гвозди и Шурупы", "Молотоки", "Отвертки", "Кирпичи"]

itemType = ["Гвоздь", "Шуруп", "Саморез", "Молоток", "Отвертка", "Кирпич"]

manufacturers = ["Стройкин", "Буратино", "Колотушкин Inc.", "ООО \"Кирпичи\"", "Пензенский строительный завод"]

nail_sizes = ["4 cm", "5 cm", "6 cm", "7 cm"]

hammer_screwdriver_sizes = ["15 cm", "18 cm", "20 cm", "25 cm", "30 cm"]

brick_colors = ["Желтый", "Оранжевый", "Белый", "Красный"]




def generate_nails():
    nails = set()
    result = set()
    while len(nails) < 20:
        nail_num = random.randrange(0, 3, 1)
        manufacturer_num = random.randrange(0, 5, 1)
        size_num = random.randrange(0, 4, 1)
        name = f'''{itemType[nail_num]} {manufacturers[manufacturer_num]} {nail_sizes[size_num]}'''
        price = random.randrange(3, 10, 1)
        item = Item(name, price)
        if not nails.__contains__(name):
            nails.add(name)
            result.add(item)
    return result


def generate_hammers():
    hammers = set()
    result = set()
    while len(hammers) < 17:
        item_num = 3
        manufacturer_num = random.randrange(0, 5, 1)
        size_num = random.randrange(0, 5, 1)
        name = f'''{itemType[item_num]} {manufacturers[manufacturer_num]} {hammer_screwdriver_sizes[size_num]}'''
        price = random.randrange(150, 550)
        item = Item(name, price)
        if not hammers.__contains__(name):
            hammers.add(name)
            result.add(item)
    return result



def generate_screwdrivers():
    screwdrivers = set()
    result = set()
    while len(screwdrivers) < 17:
        item_num = 4
        manufacturer_num = random.randrange(0, 5, 1)
        size_num = random.randrange(0, 5, 1)
        name = f'''{itemType[item_num]} {manufacturers[manufacturer_num]} {hammer_screwdriver_sizes[size_num]}'''
        price = random.randrange(150, 550)
        item = Item(name, price)
        if not screwdrivers.__contains__(name):
            screwdrivers.add(name)
            result.add(item)
    return result


def generate_bricks():
    bricks = set()
    result = set()
    while len(bricks) < 17:
        item_num = 5
        manufacturer_num = random.randrange(0, 5, 1)
        color_num = random.randrange(0, 4, 1)
        name = f'''{itemType[item_num]} {manufacturers[manufacturer_num]} {brick_colors[color_num]}'''
        item = Item(name, random.randrange(30, 90, 1))
        if not bricks.__contains__(name):
            bricks.add(name)
            result.add(item)
    return result
