# Преобразование в словарь вида:
# cook_book = {
#   'Омлет': [
#     {'ingredient_name': 'Яйцо', 'quantity': 2, 'measure': 'шт.'},
#     {'ingredient_name': 'Молоко', 'quantity': 100, 'measure': 'мл'},
#     {'ingredient_name': 'Помидор', 'quantity': 2, 'measure': 'шт'}
#     ]

with open("../files/recipes.txt", "r") as recipes_file:
    cook_book = {}
    for line in recipes_file:
        dish = line.rstrip()
        ingredient_count = recipes_file.readline().rstrip()
        list_of_ingridient = []
        for i in range(int(ingredient_count)):
            dict_for_ingredient = {'ingredient_name': '', 'quantity': '', 'measure': ''}
            ingridient = recipes_file.readline().strip().split(' | ')
            dict_for_ingredient['ingredient_name'] = ingridient[0]
            dict_for_ingredient['quantity'] = int(ingridient[1])
            dict_for_ingredient['measure'] = ingridient[2]
            list_of_ingridient.append(dict_for_ingredient)
        cook_book[dish] = list_of_ingridient
        recipes_file.readline()

final_list = {}
ingredient_list = {}


def get_shop_list_by_dishes(dishes, person):
    """Метод на вход получает название блюда и кол-во персон.
    На выходе получаем словарь ингридиентов с нужным количеством"""
    for dishes in dishes:
        for dish, ingredient in cook_book.items():
            if dish == dishes:
                for sum_list in ingredient:
                    ingredient_list = {'measure': sum_list['measure'], 'quantity': (sum_list['quantity'] * person)}
                    final_list.update({sum_list['ingredient_name']: ingredient_list})
    print(final_list)


get_shop_list_by_dishes(['Омлет', 'Утка по-пекински'], 10)
