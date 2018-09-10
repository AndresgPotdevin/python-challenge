
# coding: utf-8

# In[324]:


import os
import csv


# In[325]:


total_months = 0
total_revenue = 0
revenue_change = 0
previous_revenue = 0
greatest_increase = ["",0]
greatest_decrease = ["",999999999999999999]
revenue_changes = []

file_to_output = "PyBank.txt"


# In[326]:


csvpath = os.path.join('budget_data.csv')
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    for row in csvreader:

        total_months = total_months + 1

        total_revenue = total_revenue + int(row[1])
        
        revenue_change = int(row[1]) - previous_revenue
        
        previous_revenue = int(row[1])
        
        if (revenue_change > greatest_increase[1]):
            greatest_increase[1] = revenue_change
            greatest_increase[0] = row[0]
            
        if (revenue_change < greatest_decrease[1]):
            greatest_decrease[1] = revenue_change
            greatest_decrease[0] = row[0]
            
        revenue_changes.append(int(row[1]))
        
        average_change = (revenue_changes[-1] - revenue_changes[0]) / total_months
        
       

   


# In[327]:


print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_revenue}")
print(f"Average Change: ${round(average_change)}")
print("Greatest Increase in Profits: " + str(greatest_increase[0]) + " ($" +  str(greatest_increase[1]) + ")") 
print("Greatest Decrease in Profits: " + str(greatest_decrease[0]) + " ($" +  str(greatest_decrease[1]) + ")")


# In[330]:


with open(file_to_output, "w") as txt_file:
    txt_file.write("Total Months: " + str(total_months))
    txt_file.write("\n")
    txt_file.write("Total Revenue: " + "$" + str(total_revenue))
    txt_file.write("\n")
    txt_file.write("Average Change: " + "$" + str(average_change))
    txt_file.write("\n")
    txt_file.write("Greatest Increase: " + str(greatest_increase[0]) + " ($" + str(greatest_increase[1]) + ")") 
    txt_file.write("\n")
    txt_file.write("Greatest Decrease: " + str(greatest_decrease[0]) + " ($" + str(greatest_decrease[1]) + ")")

