# shell.py

from recipelist import *
import secrets

dish = ''
available_commands = ['help', 'vegan', 'details', 'ingredients', 'add', 'quit']

def get_vegan(generated):
    return get_dish(generated)

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

    elif x == 'vegan':
        dish = get_vegan(secrets.randbelow(amount_dishes()))
        print(dish[0])
    
    elif x == 'add':
        print('List the dish to add in following format, separatet by commas:')
        print('Name, Ingredient 1, Ingredient 2, ..., Ingredient N')
        y = input('> ')
        add_dish(y)

    elif x == 'help':
        print(available_commands)
    
    else:
        print('Unknown command')