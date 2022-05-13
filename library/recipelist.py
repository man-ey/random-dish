# recipelist.py

import csv

dishes = []

def load_dishfile() :
    dishes.clear()
    with open('library/dishes.csv', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar = '|')
        for row in reader:
            dishes.append(row)

def amount_dishes():
    i = 0
    with open('library/dishes.csv', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar = '|')
        for row in reader:
            i += 1
    return i

def get_dish(position):
    load_dishfile()
    return dishes[position]