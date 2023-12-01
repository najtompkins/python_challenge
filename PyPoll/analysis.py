# Importing Dependencies

import os
import csv

# Creates a dynamic dictionary that lists the candidate values as Keys and their vote counts as Values.
from collections import defaultdict

# Used to help round the percentages later on in the calculations to avoid floating-point rounding errors
import decimal

# Defining the relative path to the CSV file
election_data_path = os.path.join("Resources", "election_data.csv")

# Setting up variables for later (which were added as needed)
num_votes = 0
winner_total = 0
election_winner = "No Winner"
counter = defaultdict(int)

# This list stores each unique candidate voted for.
list_of_candidates = []
list_of_keys = []
list_of_totals = []

# Opening CSV and running processes
with open(election_data_path) as csv_file:

    csv_reader = csv.reader(csv_file)

    # First instance of using NEXT() in a variable collects the headers.
    csv_header = next(csv_reader)

    for votes in csv_reader:

        # This assumes 1 vote per line.
        num_votes += 1
        
        # Creates a standard list of Candidates found in the data if they are not already in the list.
        # List starts empty and populates with each new value (candidate) found in column 3 of the CSV file.
        if votes[2] not in list_of_candidates:
            list_of_candidates.append(votes[2])
        
        # Combined with the Collections Import this looks at the third column 
        # and creates a dicationary as it iterates over it, setting candidates as Keys and their votes as Values
        counter[votes[2]] += 1

    # Setting each candidate to their own correspoding index
    candidate_1 = list_of_candidates[0]
    candidate_2 = list_of_candidates[1]
    candidate_3 = list_of_candidates[2]

    # Populates the list_of_totals list collected and stored as values in the Counter dictionary
    for value in counter.values():
        list_of_totals.append(value)

        # Sets a variable = to the most votes
        winner_total = max(list_of_totals)

    # Populates the list_of_keys list collected and stored as keys in the Counter dictionary
    for key in counter.keys():
        list_of_keys.append(key)
    
    # Finds the winner_total value in the list_of_totals list and stores the corresponding index number for use later
    for index, value in enumerate(list_of_totals):
        if value == winner_total:
            winner_index = index
    
    # changes the value of election_winner from "No winner" to the candidate who won 
    election_winner = list_of_keys[winner_index]

    # Calculations for each candidate's scores into percentages
    can_1_perc = (((counter.get(f"{candidate_1}")) / num_votes)*100)
    can_2_perc = (((counter.get(f"{candidate_2}")) / num_votes)*100)
    can_3_perc = (((counter.get(f"{candidate_3}")) / num_votes)*100)
    
    can_1_perc = decimal.Decimal(can_1_perc).quantize(decimal.Decimal("0.000"))
    can_2_perc = decimal.Decimal(can_2_perc).quantize(decimal.Decimal("0.000"))
    can_3_perc = decimal.Decimal(can_3_perc).quantize(decimal.Decimal("0.000"))


# Print to terminal

bar = "---------------------------------------"

print("Election Results")
print(bar)
print(f"Total votes: {num_votes}")
print(bar)
print(f"{candidate_1}: {can_1_perc}% ({counter[candidate_1]})")
print(f"{candidate_2}: {can_2_perc}% ({counter[candidate_2]})")
print(f"{candidate_3}: {can_3_perc}% ({counter[candidate_3]})")
print(bar)
print(f"Winner: {election_winner}")


# Export the data to a .txt file

# Get the current directory
current_directory = os.getcwd()

export_file_name = "Analysis.txt"

# Create the "analysis" folder if it doesn't exist
analysis_directory = os.path.join(current_directory, "Analysis")
if not os.path.exists(analysis_directory):
    os.mkdir(analysis_directory)

if os.path.exists(os.path.join(analysis_directory, export_file_name)):
    os.remove(os.path.join(analysis_directory, export_file_name))

# Open the text file in append mode
text_file = open(os.path.join(analysis_directory, "Analysis.txt"), "a")

# Write to the text file
text_file.write("Election Results\n")
text_file.write(f"{bar}\n")
text_file.write(f"Total votes: {num_votes}\n")
text_file.write(f"{bar}\n")
text_file.write(f"{candidate_1}: {can_1_perc}% ({counter[candidate_1]})\n")
text_file.write(f"{candidate_2}: {can_2_perc}% ({counter[candidate_2]})\n")
text_file.write(f"{candidate_3}: {can_3_perc}% ({counter[candidate_3]})\n")
text_file.write(f"{bar}\n")
text_file.write(f"Winner: {election_winner}")


# Close the text file
text_file.close()