# -*- coding: UTF-8 -*-
"""PyPoll Homework Starter File."""

# Import necessary modules
import csv
import os

# Files to load and output (update with correct file paths)
filepath= "Resources/election_data.csv"
file_to_output = "analysis/election_analysis.txt"  # Output file path

# Define variables to track the election data
total_votes = 0 
vote_dict = {}

   # Code ripped 3.2.8
with open(filepath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    for row in csvreader:
        # print(row)
        total_votes += 1

        #Track votes
        candidate =row[2]
        if candidate in vote_dict.keys():
            vote_dict[candidate] +=1 #add one to the value
        else:
            vote_dict[candidate] = 1 #initialize with one vote
                       
 


 # Generate the output summary
print(vote_dict)
output = f"""
Election Results\n
----------------------------\n
Total votes: {total_votes}\n
----------------------------\n
"""


# Loop througth the dictionary
for candidate in vote_dict.keys():
    votes = vote_dict[candidate] #get votes (value) for that key
    vote_percent = round(100 * votes / total_votes, 3)
   
    
    #create output
    text = f"{candidate}: {vote_percent}% ({votes})\n"
    output +=text

#winner
winner = max(vote_dict, key=vote_dict.get) #got code from GPT
print (winner)

winner_text = f"""----------------------------\n
winner:{winner}\n
----------------------------\n
"""
output += winner_text

# Print the output
print(output)

# write the output
with open(file_to_output, "w") as txt_file:
    txt_file.write(output)