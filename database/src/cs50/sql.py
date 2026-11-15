import csv
import sqlite3

path_file = "src\\cs50\\stock_prices.csv"

counts = {}

with open(path_file, 'r') as file:
    # reader = csv.reader(file)
    reader = csv.DictReader(file)
    for row in reader:
        comp = row['comp'].strip()
        try:
            counts[comp] += 1
        except KeyError:
            counts[comp] = 1
        
        # if comp not in counts:
        #     counts[comp] = 0
        # counts[comp] += 1

for comp in counts:
    print(comp, counts[comp])

# connect to database file
conn = sqlite3.connect("src\\cs50\\test_01.db")
cursor = conn.cursor()

# query the database
cursor.execute("SELECT * FROM stock LIMIT 3")
rows = cursor.fetchall()
for row in rows:
    print(row)

# close connection
conn.close()