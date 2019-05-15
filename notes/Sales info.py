import csv

with open("Sales Records.csv", 'r') as csv_file_thing:
    reader = csv.reader(csv_file_thing)
    Fruit_Profit = []
    Clothes_Profit = []
    Meats_Profits = []
    Beverages_Profits = []
    Office_supplies_Profits = []
    Cosmetics_Profits = []
    Personal_Care_Profits = []
    HouseHold_Profits = []
    Vegetables_Profits = []
    Baby_Food_Profits = []
    Snacks_Profits = []
    Cereal_Profits = []
    for row in reader:
        profit = row[13]
        items = row[2]
        if items == "Fruits":
            Fruit_Profit.append(float(profit))
        if items == "Clothes":
            Clothes_Profit.append(float(profit))
        if items == "Meat":
            Meats_Profits.append(float(profit))
        if items == "Beverages":
            Beverages_Profits.append(float(profit))
        if items == "Office Supplies":
            Office_supplies_Profits.append(float(profit))
        if items == "Cosmetics":
            Cosmetics_Profits.append(float(profit))
        if items == "Personal Care":
            Personal_Care_Profits.append(float(profit))
        if items == "Household":
            HouseHold_Profits.append(float(profit))
        if items == "Vegetables":
            Vegetables_Profits.append(float(profit))
        if items == "Baby Food":
            Baby_Food_Profits.append(float(profit))
        if items == "Snacks":
            Snacks_Profits.append(float(profit))
        if items == "Cereal":
            Cereal_Profits.append(float(profit))
Fruit_Profit = sum(Fruit_Profit)
Clothes_Profit = sum(Clothes_Profit)
Meats_Profits = sum(Meats_Profits)
Beverages_Profits = sum(Beverages_Profits)
Office_supplies_Profits = sum(Office_supplies_Profits)
Cosmetics_Profits = sum(Cosmetics_Profits)
Personal_Care_Profits = sum(Personal_Care_Profits)
HouseHold_Profits = sum(HouseHold_Profits)
Vegetables_Profits = sum(Vegetables_Profits)
Baby_Food_Profits = sum(Baby_Food_Profits)
Snacks_Profits = sum(Snacks_Profits)
Cereal_Profits = sum(Cereal_Profits)
print("Fruit total profits = %f" % Fruit_Profit)
print("Clothes total profits = %f" % Clothes_Profit)
print("Meats total profits = %f " % Meats_Profits)
print("Beverages total profits = %f" % Beverages_Profits)
print("Office supplies total profits = %f" % Office_supplies_Profits)
print("Cosmetics total profits = %f" % Cosmetics_Profits)
print("Personal_Care_Profits = %f" % Personal_Care_Profits)
print("HouseHold_Profits = %f" % HouseHold_Profits)
print("Vegetables_Profits = %f" % Vegetables_Profits)
print("Baby_Food_Profits = %f" % Baby_Food_Profits)
print("Snacks_Profits = %f" % Snacks_Profits)
print("Cereal_Profits = %f" % Cereal_Profits)


list_num = [Profits_For_Fruits, Profits_For_Cereal, Profits_For_Vegetables, Profits_For_Household, Profits_For_Snacks,
            Profits_For_Meats, Profits_For_Personal_Care, Profits_For_Beverages, Profits_For_Cosmetica, Profits_For_Baby_Food,
            Profits_For,]