import ItemGenerator
from Category import Category

categories = ["Гвозди и Шурупы", "Молотоки", "Отвертки", "Кирпичи"]

def generate_categories():
    result = []
    nail_category = Category(categories[0],list(ItemGenerator.generate_nails()))
    hammer_category = Category(categories[1],list(ItemGenerator.generate_hammers()))
    screwdriver_category = Category(categories[2],list(ItemGenerator.generate_screwdrivers()))
    brick_category = Category(categories[3], list(ItemGenerator.generate_bricks()))

    result.append(nail_category)
    result.append(hammer_category)
    result.append(screwdriver_category)
    result.append(brick_category)
    return result

