# Import packages
import os
import csv

# Create and store filepath
budget_csv = os.path.join("PyBank","Resources","budget_data.csv")

# lists to store csv read
date = []
profit_loss = []
# list to store column mutation on profit_loss
monthly_change = []

# var iteration as we go, rerun for each loop change
total_profit = 0
total_change_profit = 0
initial_profit = 0

# Open and read csv, with open
with open(budget_csv) as budget_csv_file:
    budget_read = csv.reader(budget_csv_file, delimiter = ",")
    # denote header
    header = next(budget_read)
    # denote headless set
    headless_budget = [row for row in budget_read]
    # read through rows append column heads to row[num]
    for row in headless_budget:
        # append date list, 0
        date.append(row[0])
        # append profit_loss, 1
        profit_loss.append(row[1])
        # using int to ensure number
        total_profit =  total_profit + int(row[1])
        final_profit = int(row[1])
        # at start of iteration initial profit is 0
        change_in_profit = final_profit - initial_profit
        # append monthly_change
        monthly_change.append(change_in_profit)
        #iterate total_change_profit by adding supp calc for change_in_profit
        total_change_profit = total_change_profit + change_in_profit
        
# months iteration
months = 0
for number in date:
    months += 1
    
# this works, but the diff list by itself is super weird
diff = []
for i in range(1, len(monthly_change)):
    rec = monthly_change[i] - monthly_change[i-1]
    diff.append(rec)
diff_sum = sum(diff)
diff_avg = diff_sum/(months-1)

# id largest value
greatest_increase = max(monthly_change)
inc_date = date[monthly_change.index(greatest_increase)]
# id lowest value
greatest_decrease = min(monthly_change)
dec_date = date[monthly_change.index(greatest_decrease)]

print("Financial Analysis")
print(f"-"*45)
print(f"Total Months: {months}")
print(f"Total:  {total_change_profit}") 
print(f"Average Change: {round(diff_avg,3)}")
print(f"Greatest Increase in Profits: {inc_date}: {greatest_increase}")
print(f"Greatest Decrease in Profits: {dec_date}: {greatest_decrease}")