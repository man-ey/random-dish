# shell.py

from recipelist import *
import secrets
from zoneinfo import available_timezones

dish = ''
recipe_amount = 10
available_commands = ['help', 'vegan', 'details', 'ingredients', 'quit']

def get_vegan(number):
    return ''.join(['Vegan dish generated: ', str(number)])

while 1:
    x = input('> ')
    
    if x == 'quit':
        break

    elif (x == 'details' or x == 'ingredients'):
        if dish == '':
            print('Request a dish first')
        else:
            print('details here')

    elif x == 'vegan':
        dish = get_vegan(secrets.randbelow(recipe_amount))
        load_dishfile()
        print(dish)

    elif x == 'help':
        print(available_commands)
    
    else:
        print('Unknown command')