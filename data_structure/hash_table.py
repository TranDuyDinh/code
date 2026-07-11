path_to_file = "C://Users//Tran Duy Dinh//Documents//GitHub//code//data_structure//src//Hash Table//stock_prices.csv"

# list
stock_prices = []
with open(path_to_file, "r") as f:
    for line in f:
        tokens = line.split(',')
        day = tokens[0]
        prices = float(tokens[1])
        stock_prices.append([day, prices])

print(stock_prices)

for element in stock_prices:
    if element[0] == '09-Mar':
        print(element[1])

# dictionary
stock_prices = {}
with open(path_to_file, "r") as f:
    for line in f:
        tokens = line.split(',')
        day = tokens[0]
        prices = float(tokens[1])
        stock_prices[day] = [prices]

print(stock_prices)
print(stock_prices['09-Mar'])

print("\nGoodbye...")