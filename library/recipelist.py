# recipelist.py

import csv

dishes = []

def load_dishfile(category) :
    dishes.clear()
    with open('library/dishlibrary/' + category + '_dishes.csv', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar = '|')
        for row in reader:
            dishes.append(row)

def amount_dishes(category):
    i = 0
    with open('library/dishlibrary/' + category + '_dishes.csv', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar = '|')
        for row in reader:
            i += 1
    return i

def get_dish(position, filename):
    load_dishfile(filename)
    return dishes[position]

def add_dish(toAdd, category):
    dish = toAdd.split(',')
    with open('library/dishlibrary/' + category + '_dishes.csv', 'a+', newline='') as writeobj:
        csv_writer = csv.writer(writeobj)
        csv_writer.writerow(dish)
        writeobj.close()

def bookmark_dish(toAdd):
    load_dishfile('favourite')
    if toAdd in dishes:
        print('Dish already bookmarked')
        return  
    
    else:
        with open('library/dishlibrary/favourite_dishes.csv', 'a+', newline='') as writeobj:
            csv_writer = csv.writer(writeobj)
            csv_writer.writerow(toAdd)
            writeobj.close()