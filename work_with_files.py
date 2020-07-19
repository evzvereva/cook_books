from email.policy import default

with open('recipes.txt', encoding='utf8') as f:
    cook_book = {}
    while True:
        dish = f.readline().strip()  # список блюд
        if not dish:
            break
        number = int(f.readline().strip())  # количество ингредиентов
        recipe_list = []
        while number > 0:
            recipe_list.append(f.readline().strip().split(' | '))  # список ингредиентов
            number -= 1
        f.readline()
        ingredients_dish = []
        for line in recipe_list:
            ingredients_dish.append({'ingredient name': line[0], 'quantity': line[1], 'measure': line[2]})
        cook_book[dish] = ingredients_dish

print(cook_book)


person_count = int(input('Введите, пожалуйста, количество персон: '))


list_dishes = []

from collections import Counter


def get_shop_list_by_dishes(list_dishes, person_count):
    quantity_ingredients = []
    dictionary_ingredients = {}
    for dishes, ingredients_dish in cook_book.items():
        list_dishes.append(dishes)
        for ingredients in ingredients_dish:
            quantity = ingredients['quantity']
            ingredient_name = ingredients['ingredient name']
            quantity_ingredients.append(ingredient_name)
    counter = Counter(quantity_ingredients)
    for key, value in counter.items():
        result = value * int(ingredients['quantity']) * person_count
        dictionary_ingredients[key] = {'quantity': result, 'measure': ingredients['measure']}
    return dictionary_ingredients


print(get_shop_list_by_dishes(list_dishes, person_count))
