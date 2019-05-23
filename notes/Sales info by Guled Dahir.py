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
    # Regions
    Sub_Saharan_Africa_Profits = []
    Middle_East_Profits = []
    North_Africa_Profits = []
    Australia_Profits = []
    Oceania_Profits = []
    Europe_Profits = []
    Asia_Profit = []
    Central_America_Profits = []
    Caribbean_Profits = []
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

list_num = [Fruit_Profit, Cereal_Profits, Vegetables_Profits, HouseHold_Profits, Snacks_Profits,
            Meats_Profits, Personal_Care_Profits, Beverages_Profits, Cosmetics_Profits,
            Baby_Food_Profits, Clothes_Profit, Office_supplies_Profits]

list_type = ("Fruits, Cereal, Vegetables, Household, Snacks, Meat, Personal_Care, Beverages, Cosmetics, Baby_Food,"
             "Cloths, Office_Supplies")

index = list_num.index(max(list_num))
print()
print("Item with the highest profit is %s" % list_num[index])

regions = ['Sub-Saharan_Africa', 'Middle_East_and_North_Africa', 'Australia_and _Oceania', 'Europe', 'Asia',
           'Central_America_and_the_Caribbean']

regions_num = (Sub_Saharan_Africa_Profits, Middle_East_Profits and North_Africa_Profits, Australia_Profits and
               Oceania_Profits, Europe_Profits, Asia_Profit, Central_America_Profits and Caribbean_Profits)

Sub_Saharan_Africa_Profits = sum(Sub_Saharan_Africa_Profits)
Middle_East_Profits = sum(Middle_East_Profits)
North_Africa_Profits = sum(North_Africa_Profits)
Australia_Profits = sum(Australia_Profits)
Oceania_Profits = sum(Oceania_Profits)
Europe_Profits = sum(Europe_Profits)
Asia_Profit = sum(Asia_Profit)
Central_America_Profits = sum(Central_America_Profits)
Caribbean_Profits = sum(Caribbean_Profits)

print("Sub_Saharan_Africa_Profits = %f" % Sub_Saharan_Africa_Profits)
print("Middle_East_Profits = %f" % Middle_East_Profits)
print("North_Africa_Profits = %f " % North_Africa_Profits)
print("Australia_Profits = %f" % Australia_Profits)
print("Oceania_Profits = %f" % Oceania_Profits)
print("Europe_Profits = %f" % Europe_Profits)
print("Asia_Profit = %f" % Asia_Profit)
print("Central_America_Profits = %f" % Central_America_Profits)
print("Caribbean_Profits = %f" % Caribbean_Profits)


index = regions_num.index(max(regions_num))
print()
print("Region with the highest profit is %s" % regions_num[index])
