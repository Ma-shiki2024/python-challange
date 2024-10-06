# -*- coding: UTF-8 -*-


# Dependencies
import csv
import os

# Files to load and output (update with correct file paths)
#file_to_load = os.path.join("..","Resources", "budget_data.csv")  # Input file path
file_to_output = os.path.join("C:/Users/shiki/ClassAssignments/Module3/python-challange/pyBank/analysis/budget_analysis.txt")  # Output file path

file_to_load = os.path.join("C:/Users/shiki/ClassAssignments/Module3/python-challange/pyBank/Resources/budget_data.csv")


# Define variables to track the financial data
total_months = 0
total_net = 0
previous_profit=0
current_profit = 0
greatest_diff = 0 
greatest_month = ""
lowest_diff = 0
lowest_month=""
Total_change=0
Average_change=0
loop_counter=0



# Add more variables to track other necessary financial data

# Open and read the csv
with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data, delimiter=",")

    # Skip the header row
    header = next(reader)

    # Extract first row to avoid appending to net_change_list
    

    # Track the total and net change
    # Process each row of data
    for row in reader:

    
        # Track the total
        total_months = total_months+1

        current_profit = int(row[1])

        # Track the net change
        
        total_net = total_net + current_profit

        # Calculate the greatest increase in profits (month and amount)

        profit_diff = current_profit - previous_profit

        if(loop_counter > 0) :
            Total_change = Total_change + profit_diff


        if (profit_diff > greatest_diff) :
            greatest_diff= profit_diff
            greatest_month=row[0]
        
        # Calculate the greatest decrease in losses (month and amount)
        
        if (profit_diff<lowest_diff):
            lowest_diff=profit_diff
            lowest_month=row[0]
           

        previous_profit=current_profit

        loop_counter = loop_counter+1
                


# Calculate the average net change across the months
Average_change= Total_change/(total_months-1)



# Generate the output summary

output = f"Total Months : {total_months} \nTotal : {total_net} \n Average_change : {Average_change} \n Greatest Increase in profits : {greatest_month}  (${greatest_diff} ) \n Greatest Decrease in profits : {lowest_month} (${lowest_diff} )\n"
      
 
# Print the output

print(output)


#print(f"Total Months : {total_months}")
#print(f"Total : {total_net}")
#print(f"Average_change : {Average_change}")

#print(f"Greatest Increase in profits : {greatest_month}  (${greatest_diff} )")

#print(f"Greatest Decrease in profits : {lowest_month} (${lowest_diff} )")

# Write the results to a text file
with open(file_to_output, "w") as txt_file:
  txt_file.write(output)
