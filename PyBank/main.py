import os
import csv

#csvpath = "C:\\Users\\Owner\\Desktop\\Homework\\python-challenge\\PyBank\\budget_data.csv"
csvpath = os.path.join("..", "PyBank", "budget_data.csv")
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    months = []
    profit_losses = []
    avg_change = []
# finding number of months and sum of profits/losses
    for x in csvreader:
        months.append(x[0])
        profit_losses.append(int(x[1]))

    months_count = len(months)
    total = sum(profit_losses)
    

# finding average gain/loss
    for y in range(len(profit_losses)):
        x = y - 1
        change = profit_losses[y]-profit_losses[x]
        avg_change.append(change)
#pop first value because x is -1
    avg_change.pop(0)
    avg = round(sum(avg_change)/(len(avg_change)),2)
   

# finding max increase
    max_change = max(avg_change)
    ind_max = avg_change.index(max_change)  
# add one to index because took one out in avg_change list   
    month_max = months[ind_max+1]

# finding biggest decrease
    min_change = min(avg_change)
    ind_min = avg_change.index(min_change)
# add one to index because took one out in avg_change list
    month_min = months[ind_min+1]
   

# output
print("Financial Analysis")
print("-----------------------")
print("Total Months: " + str(months_count))
print("Total: $" + str(total))
print("Average Change: $" + str(avg))
print("Greatest Increase in Profits: " + str(month_max) + "($" + str(max_change) + ")")
print("Greatest Decrease in Profits: " + str(month_min) + "($" + str(min_change) + ")")