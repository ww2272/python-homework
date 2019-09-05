import csv

with open("02-Homework_02-Python_Instructions_PyBank_Resources_budget_data.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    month_count = 0
    total = 0
    minimum = 0
    maximum = 0
    next(csv_reader)
    for row in csv_reader:
        month_count += 1
        total = total + float(row[1])
        if minimum == 0:
            minimum = float(row[1])
            min_name = row[0]
        if maximum == 0:
            maximum = float(row[1])
            max_name = row[0]
        elif float(row[1]) < minimum:
            minimum = float(row[1])
            min_name = row[0]
        elif float(row[1]) > maximum:
            maximum = float(row[1])
            max_name = row[0]
                
    print("Financial Analysis")
    print("--------------------")
    print(f"Total Months: {month_count}")
    print(f"Total: ${total}")
    print(f"Average  Change: ${total/month_count}")
    print(f"Greatest Increase in Profits: {max_name} (${maximum})")
    print(f"Greatest Decrease in Profits: {min_name} (${minimum})")

    greatest_incr = f"{max_name} (${maximum})"
    greatest_decr = f"{min_name} (${minimum})"
    results = {"Total Months": month_count, "Total": total, "Average Change": total/month_count, "Greatest Increase in Profits": greatest_incr, "Greatest Decrease in Profits": greatest_decr}
    f = open("PyBank_results.txt", "w")
    f.write(str(results))
    f.close()
