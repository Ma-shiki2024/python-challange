# -*- coding: UTF-8 -*-
"""PyPoll Homework Starter File."""

# Import necessary modules
import csv
import os

# Files to load and output (update with correct file paths)

file_to_output = os.path.join("C:/Users/shiki/ClassAssignments/Module3/python-challange/pyPoll/analysis/election_analysis.txt")  # Output file path

file_to_load = os.path.join("C:/Users/shiki/ClassAssignments/Module3/python-challange/pyPoll/Resources/election_data.csv")

# Initialize variables to track the election data
total_votes = 0  # Track the total number of votes cast
candidate_name = ''
candidate_vote_count = 0

# Define lists and dictionaries to track candidate names and vote counts
candidate_counts = {}
        

# Winning Candidate and Winning Count Tracker
winner_candidate = ''


# Open the CSV file and process it
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Skip the header row
    header = next(reader)

    # Loop through each row of the dataset and process it
    for row in reader:

        # Print a loading indicator (for large datasets)
       
        print(". ", end="")

        # Increment the total vote count for each row

        total_votes=total_votes+1

        # Get the candidate's name from the row
        candidate_name = row[2]

        # If the candidate is not already in the candidate list, add them
        
        if (candidate_name not in candidate_counts):
            candidate_counts[candidate_name] = 1
        else : 
           candidate_vote_count = candidate_counts[candidate_name]
           candidate_counts[candidate_name] = candidate_vote_count+1


        # Add a vote to the candidate's count

output = f"Election Results \n --------------------- \n\nTotal Votes :{total_votes}\n\n --------------------- \n\n"

winner_vote = next(iter(candidate_counts.values()))

# Loop through the candidates to determine vote percentages and identify the winner
for key,value in candidate_counts.items() :
    # Get the vote count and calculate the percentage
    output = output+f"{key} : {round((value/total_votes)*100,3)}% ({value})\n\n"
    # Update the winning candidate if this one has more votes
    if (value>winner_vote):
        winner_candidate = key
        winner_vote=value


output = output + f"\n --------------------- \n\nWinner :{winner_candidate} \n\n --------------------- "
print(total_votes)
print(output)

# Open a text file to save the output
with open(file_to_output, "w") as txt_file:

    # Print the total vote count (to terminal)

    # Write the total vote count to the text file
    # Print and save each candidate's vote count and percentage
    # Generate and print the winning candidate summary
    # # Save the winning candidate summary to the text file
    txt_file.write(output)


