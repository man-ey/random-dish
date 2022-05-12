# recipelist.py

import csv

def load_dishfile() :
    with open('library/dishes.csv', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=' ', quotechar = '|')
        for row in reader:
            print(','.join(row))

