import pandas as pd
import csv


def properatiWebScraping(amb, precioMin, precioMax, barrio):
    res = []
    filter_condition = lambda row: row['Barrio'].lower() == str(barrio).replace(" ","-").lower() and (int(row['$']) > int(precioMin) and int(row['$']) < int(precioMax)) and int(row['Ambientes']) == amb
    with open('utilities/Properati.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            if filter_condition(row):
                res.append(row['Link'])
    return res
