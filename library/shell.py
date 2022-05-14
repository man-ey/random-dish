# shell.py

from recipelist import *
import secrets

dish = ''
available_commands = ['help', 'bookmarks', 'vegan', 'vegetarian', 'omnivor', 'details', 'ingredients', 'add', 'favourite', 'bookmark', 'quit']

def get_ingredients():
    return dish[1:len(dish)]


while 1:
    x = input('> ')
    
    if x == 'quit':
        break

    elif (x == 'details' or x == 'ingredients' or x == 'detail'):
        if dish == '':
            print('Request a dish first')
        else:
            print(get_ingredients())

    elif x == 'omnivor' or x == 'vegan' or x == 'vegetarian':
        dish = get_dish(secrets.randbelow(amount_dishes(x)), x)
        print(dish[0])
    
    elif x == 'bookmarked':
        dish = get_dish(secrets.randbelow(amount_dishes('favourite')), 'favourite')
        print(dish[0])

    elif x == 'add':
        print('List the dish to add in following format, separatet by commas:')
        print('Name, Ingredient 1, Ingredient 2, ..., Ingredient N')
        y = input('> ')
        print('Vegan, vegetarian or omnivor dish?')
        z = input('> ')
        if z == 'vegan' or z == 'vegetarian' or z == 'omnivor':
            add_dish(y, z)
        else:
            print('Category not available. Try again.')
    
    elif x == 'bookmark' or x == 'favourite':
        if dish == '':
            print('Generate a dish first')
        else:
            bookmark_dish(dish)

    elif x == 'help':
        print(available_commands)
    
    else:
        print('Unknown command')