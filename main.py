import time

from User import User
from CategoryGenerator import generate_categories

basket = []



def process_items(cat_num, user):
    inputString = ""
    while not (inputString == "back" ):
        item_num = 1
        for item in (categories[cat_num].get_items()):
            print(f"{item_num}) {item.get_name()} Цена:{item.get_price()} Рейтинг: {item.get_rating() if item.get_rating() is not None else 'отсутствует' }")
            item_num += 1
        inputString = input()
        if inputString == "back":
            break
        if str(inputString).startswith("add "):

            if str(inputString).startswith("add"):
                words = str(inputString).split(" ")
                if len(words) > 2:
                    print("Некорректное количествоа параметров, введите команду в стиле \"add <номер товара>\"")
                    time.sleep(2)
                else:
                    try:
                        item_num = int(words[1])
                        user.add_to_basket(categories[cat_num].get_items()[item_num - 1])
                    except Exception:
                        print("Некорректный параметр, введите команду в стиле \"add <номер товара>\"")
                        time.sleep(2)
        else:
            print("Некорректная команда, введите команду в стиле \"add <номер товара>\"")
            time.sleep(2)

def process_categories(user):
    inputString = ""
    while not inputString == "back":
        print("Выберите номер категории:")
        cat_num = 1
        for category in categories:
            print(f'''{cat_num}) {category.get_name()}''')
            cat_num += 1
        inputString = input()
        if inputString == "back":
            break
        try:
            cat_num = int(inputString)
            process_items(cat_num - 1, user)
        except Exception:
            print("Введите валидный номер категории или \"back\"")

def process_basket(user):
    print("Купленные товары")
    item_no = 1
    sum = 0

    for item in user.get_basket().get_items():
        print(f"{item_no}) {item.get_name()} цена: {item.get_price()} рублей Рейтинг: {item.get_rating()}")
        item_no += 1
        sum += item.get_price()
    print("--------------------------------------------------")
    print(f"Итого товаров: {len(user.get_basket().get_items())} Общая стоимость: {sum}")

def rate_item(user, item_num):
    print("Введите оценку от 1 до 5")
    inputstr = input()
    if (inputstr == '1' or inputstr == '2' or inputstr == '3' or inputstr == '4'
    or inputstr == '5'):
        from Item import Item
        item : Item = user.get_basket().get_items()[item_num]
        item.add_review(int(inputstr))
    else:
        print("Оценка не валидна, введите целое число от 1 до 5, процесс оценки отменен")
        time.sleep(2)


def process_rate(user):
    print("Ввведите номер товара для оценки")
    time.sleep(1)
    item_num = 1
    for item in user.get_basket().get_items():
        print(f"{item_num}) {item.get_name()}")
        item_num += 1
    inputStr = input()
    try:
        num = int(inputStr)
        rate_item(user, num-1)
    except Exception:
        print("Невалидный номер товара")



if __name__ == '__main__':
    user = User(login="denis", password="denis")
    categories = generate_categories()
    password_valid = False
    print("Введите ваши данные:")
    while not password_valid:
        print("Login:")
        login = input()
        print("Password:")
        password = input()
        if user.get_login() == login and user.get_password() == password:
            print("Valid creds")
            password_valid = True
        else:
            print("Логин или пароль не правильный, попробуйте еще раз")
    command = ""
    while not command == "cancel":
        print("Введите команду, для получения списка команд введите \"info\"")
        command = input()
        if not (command == "info" or command == "categories" or
        command == "basket" or command == "cancel" or command == "rate"):
            print("Неизвестная команда, введите \"info\" для получения списка команд")
        elif command == "info":
            print("info - информация о командах")
            print("basket - операции с корзиной")
            print("categories - информация по категориям")
            print("rate - оценить купленный товар")
            print("cancel - выйти")
        elif command == "categories":
            process_categories(user)
        elif command == "basket":
            process_basket(user)
        elif command == "rate":
            process_rate(user)


