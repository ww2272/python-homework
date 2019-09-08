import csv

with open("02-Homework_02-Python_Instructions_PyBank_Resources_budget_data.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    month_count = 0
    total = 0
    minimum = 0
    maximum = 0
    next(csv_reader)
    log = []
    change_list = []
    for row in csv_reader:
        if (month_count==0):            
            month_count += 1
            total = total + float(row[1])
            log.append(float(row[1]))
        else:
            month_count += 1
            total = total + float(row[1])
            change = float(row[1])-log[-1]
            print(change)
            change_list.append(change)
            if minimum == 0:
                minimum = change
                min_name = row[0]
            if maximum == 0:
                maximum = change
                max_name = row[0]
            elif change < minimum:
                minimum = change
                min_name = row[0]
            elif change > maximum:
                maximum = change
                max_name = row[0]
            log.append(float(row[1]))

print("Financial Analysis\n")
print("--------------------")
print(f"Total Months: {month_count}")
print(f"Total: ${total}")
print(f"Average  Change: ${round(sum(change_list)/len(change_list))}")
print(f"Greatest Increase in Profits: {max_name} (${maximum})")
print(f"Greatest Decrease in Profits: {min_name} (${minimum})")

f = open("PyBank_results.txt", "w")
f.write("Financial Analysis\n")
f.write("----------------------\n")
f.write(f"Total Months: {month_count}\n")
f.write(f"Total: ${total}\n")
f.write(f"Average  Change: ${round(sum(change_list)/len(change_list))}\n")
f.write(f"Greatest Increase in Profits: {max_name} (${maximum})\n")
f.write(f"Greatest Decrease in Profits: {min_name} (${minimum})\n")
f.close()
