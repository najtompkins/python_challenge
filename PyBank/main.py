# Importing Dependencies

import os
import csv

# Defning the relative path to the CSV file
budget_data_path = os.path.join("Resources", "budget_data.csv")

# Setting up variables for later (which were added as needed)
num_months = 0
sum_of_numbers = 0
average_of_number = 0

# This list stores each change in value starting from the second subtracted from the first, the third subtracted from the second, etc.
# This will be used to run a len() funciton and a mean() function later on. 
mean_of_numbers = []

# Setting code to use while the CSV file is open
with open(budget_data_path) as csv_file:

    csv_reader = csv.reader(csv_file)
    # First instance of using NEXT() in a variable COLLECTS THE FIRST LINE, WHICH ARE HEADERS
    csv_header = next(csv_reader)
    ## print(csv_header)

    # FIRST ROW INSTRUCTIONS
    # Second instance of NEXT() COLLECTS THE SECOND LINE, WHICH IS THE FIRST ROW OF DATA
    first_row = next(csv_reader)

    ## print(first_row)

    first_value = int(first_row[1])
    first_value_add = int(first_row[1])
    max_value_date = str("Not Changed")
    min_value_date = str("Also not Changed")


    for months in csv_reader:

        # Counts the number of months by increasing by 1 for each row. 
        # THIS IS DEPENDANT ON THE DATA ALREADY HAVING ONLY 1 ENTRY PER MONTH
        num_months += 1

        # Adds each int(total) to each other, storing them in the sum_of_numbers variable
        sum_of_numbers += int(months[1])
        
        # Takes the changes in values between each sequential integer and stores them in the mean_of_numbers list above
        change_in_value = (int(first_value) - int(months[1]))
        mean_of_numbers.append(change_in_value)

        if change_in_value == max(mean_of_numbers):
            max_value_date = months[0]

        if change_in_value == min(mean_of_numbers):
            min_value_date = months[0]

        # In order for the calculation of finding the change between two values to work... 
        # the variable first_value needs to be reset to the current iteration so that the next iteration can be compared against it...
        # and not perpetually against the initial starting value
        first_value = months[1]
        

    # Since the first row is stored in the first_row variable, everything starts on row 3, meaning the count will be off by 1. This corrects this.
    num_months += 1

    # Averaging the changes between one month and the next that were stored in the mean_of_numbers list
    average_of_number = round(((sum(mean_of_numbers)/len(mean_of_numbers)) * -1),2)
    
    # Since the first row is stored in the first_row variable, everything starts on row 3, meaning the count will be off by 1. This corrects this.
    sum_of_numbers += first_value_add
    
    # Finding the maximum increase in the mean_of_numbers list
    max_increase = (max(mean_of_numbers)) * -1

    # Finding the minimum increase in the mean_of_numbers list
    min_increase = (min(mean_of_numbers)) * -1


# Prints to the terminal

print("Financial Analysis")
print("---------------------------------------")
print(f"Total months: {num_months}")
print(f"Total: ${sum_of_numbers}")
print(f"Average Change: ${average_of_number}")
print(f"Greatest Increase in Profits: {min_value_date} ${min_increase}")
print(f"Greatest Decrease in Profits: {max_value_date} ${max_increase}")



# This exports the results to a .txt file

# Get the current directory
current_directory = os.getcwd()

# Create the "analysis" folder if it doesn't exist
# '''''''''''''''''' 
# '''''''''''''''''' Google Bard actually helped with the syntax of this!
analysis_directory = os.path.join(current_directory, "Analysis")

export_file_name = "Analysis.txt"

if not os.path.exists(analysis_directory):
    os.mkdir(analysis_directory)

if os.path.exists(os.path.join(analysis_directory, export_file_name)):
    os.remove(os.path.join(analysis_directory, export_file_name))

# Open the text file in append mode
text_file = open(os.path.join(analysis_directory, "Analysis.txt"), "a")

# Write to the text file
text_file.write("Financial Analysis\n")
text_file.write("---------------------------------------\n")
text_file.write(f"Total months: {num_months}\n")
text_file.write(f"Total: ${sum_of_numbers}\n")
text_file.write(f"Average Change: ${average_of_number}\n")
text_file.write(f"Greatest Increase in Profits: {min_value_date} (${min_increase})\n")
text_file.write(f"Greatest Decrease in Profits: {max_value_date} (${max_increase})\n")

# Close the text file
text_file.close()