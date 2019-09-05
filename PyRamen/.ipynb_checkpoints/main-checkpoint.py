import csv

menu = []
with open("02-Homework_02-Python_Instructions_PyRamen_Resources_menu_data.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    next(csv_reader)
    for row in csv_reader:
        menu.append(row)

sales = []
with open("02-Homework_02-Python_Instructions_PyRamen_Resources_sales_data.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    next(csv_reader)
    for row in csv_reader:
        sales.append(row)

report = {}
Quantity = []
Menu_Item = []
for lists in sales:
    Menu_Item.append(lists[4])
    Quantity.append(int(lists[3]))
for item in Menu_Item:
    if item not in report.keys():
        report[item]={
            "01-count": 0,
            "02-revenue": 0,
            "03-cogs": 0,
            "04-profit": 0
        }


Item = []
Price = []
Cost = []

for each_list in menu:
    Item.append(each_list[0])
    Price.append(float(each_list[3]))
    Cost.append(float(each_list[4]))

for i in range(len(Menu_Item)):
    each_item = Menu_Item[i]    
    if each_item in Item:
        menu_index = Item.index(each_item)
        profit = Price[menu_index] - Cost[menu_index]
        report[each_item]['01-count'] += Quantity[i]
        report[each_item]['02-revenue'] += Quantity[i]*Price[menu_index]
        report[each_item]['03-cogs'] += Quantity[i]*Cost[menu_index]
        report[each_item]['04-profit'] += Quantity[i]*profit

f = open("PyRamen_results.txt", "w")
f.write(str(report))   
f.close()
