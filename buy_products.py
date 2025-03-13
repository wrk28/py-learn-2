from pprint import pprint


def fill_book(address:str) -> dict:
   cook_book = {}
   with open(address) as f:
    lines = [line.strip() for line in f]
    index = 0
    while index < len(lines):
        dish = lines[index]
        number_ingredients = int(lines[index+1])
        cook_book[lines[index]] = []
        
        start_ingr_indx = index + 2
        end_ingr_indx = index + number_ingredients + 2
        end_dish_indx = number_ingredients + 3
        
        for i in range(start_ingr_indx, end_ingr_indx):
            ingredients = lines[i].split(' | ')
            cook_book[dish] += [{'ingredient_name': ingredients[0], 'quantity': int(ingredients[1]), 'measure': ingredients[2]}]
        index += end_dish_indx
    return cook_book

def get_shop_list_by_dishes(dishes: list, person_count: int, cook_book) -> dict:
    shop_list = {}
    for item in dishes:
        ingredients = cook_book[item]
        for ingr in ingredients:
            ingredient_name = ingr['ingredient_name']
            if ingredient_name in shop_list:
                value = shop_list[ingredient_name]
                value['quantity'] += ingr['quantity'] * person_count
            else:
                shop_list[ingredient_name] = {'quantity': ingr['quantity'] * person_count, 'measure': ingr['measure']}
    return shop_list

if __name__ == '__main__':
    cook_book = fill_book(r"./files/recipes.txt")
    pprint(cook_book)
    print()
    
    shop_list = get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2, cook_book)
    pprint(shop_list)