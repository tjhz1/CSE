import csv

with open("Sales Records.csv", 'r') as csv_file_thing:
    reader = csv.reader(csv_file_thing)
    total = 0
    for row in reader:
        profit = row[13]
        items = row[2]
        Revenue = row[11]
        Total_cost = row[12]
        Unit_Cost = row[11]
        Unit_Price = row[10]
        Unit_Sold = row[9]
        if items == "Fruits":
            print(profit, items, Revenue, Total_cost)
            total += float(profit)
        if items == "Beverages":
            total += float(profit)
        if items == "Clothes":
            total += float(profit)
        if items == "Meat":
            total += float(profit)
    print(total)
