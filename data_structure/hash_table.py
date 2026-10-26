path_to_file = "C://Users//Tran Duy Dinh//Documents//GitHub//code//data_structure//src//Hash Table//stock_prices.csv"

" dictionary "
def load_data_from_csv(file_path):
    data = {}
    with open(file_path, "r") as f:
        for line in f:
            tokens = line.strip().split(',')
            day = tokens[0]
            prices = float(tokens[1])
            data[day] = prices
    return data

" list "
# def load_data_from_csv(file_path):
#     data = []
#     with open(file_path, "r") as f:
#         for line in f:
#             tokens = line.strip().split(',')
#             day = tokens[0]
#             prices = float(tokens[1])
#             data.append([day, prices])
#     return data


class HashTable:

    def __init__(self):
        self.size = 100
        self.table = [None] * self.size

    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % 100




if __name__ == "__main__":
    stock_prices = load_data_from_csv(path_to_file)
    # print(stock_prices)

    # Dictionary
    # print("09-Mar:", stock_prices['09-Mar'])

    # List
    # for element in stock_prices:
    #     if element[0] == '09-Mar':
    #         print(element[1])

    table = [None for i in range(5)]
    print(table)


    # print(get_hash('09-Mar'))
    print("\nGoodbye...")








