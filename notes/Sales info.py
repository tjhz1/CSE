import csv

with open("Sales Records.csv", 'r') as csv_file_thing:
    reader = csv.reader(csv_file_thing)
    Fruit_Profit = []
    Clothes_Profit = []
    Meats_Profits = []
    Beverages_Profits = []
    for row in reader:
        profit = row[13]
        items = row[2]
        if items == "Fruits":
            Fruit_Profit.append(float(profit))
        if items == "Clothes":
            Clothes_Profit.append(float(profit))
        if items == "Meats":
            Meats_Profits.append(float(profit))
        if items == "Beverages":
            Beverages_Profits.append(float(profit))
Fruit_Profit = sum(Fruit_Profit)
Clothes_Profit = sum(Clothes_Profit)
Meats_Profits = sum(Meats_Profits)
Beverages_Profits = sum(Beverages_Profits)
print("Fruit total profits = %f" % Fruit_Profit)
print("Clothes total profits = %f" % Clothes_Profit)
print("Meats total profits = %f " % Meats_Profits)
print("Beverages total profits = %f" % Beverages_Profits)
