# shell.py

import secrets

dish = ''
recipe_amount = 10

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
        print(dish)
    
    else:
        print('Unknown command')