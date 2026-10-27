import csv

path_file = "database\\src\\cs50\\stock_prices.csv"

counts = {}

with open(path_file, 'r') as file:
    # reader = csv.reader(file)
    reader = csv.DictReader(file)
    for row in reader:
        comp = row['comp']
        if comp not in counts:
            counts[comp] = 0
        counts[comp] += 1
    for comp in counts:
        print(comp, counts[comp])
