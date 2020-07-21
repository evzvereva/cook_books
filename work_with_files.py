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


    def get_shop_list_by_dishes(list_dishes, person_count):
        dictionary_ingredients = {}
        for dishes in list_dishes:
            if dishes in cook_book.keys():
                for ingredients in cook_book[dishes]:
                    ingredient_name = ingredients['ingredient name']
                    if ingredient_name not in dictionary_ingredients.keys():
                        dictionary_ingredients[ingredient_name] = {'measure': ingredients['measure'],
                                                                   'quantity': int(
                                                                       ingredients['quantity']) * person_count}
                    else:
                        plus = int(ingredients['quantity']) * person_count
                        dictionary_ingredients[ingredient_name]['quantity'] += plus
        return dictionary_ingredients


    print(get_shop_list_by_dishes(['Омлет', 'Фахитос'], person_count=3))
print(cook_book)
