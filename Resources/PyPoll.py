#PyPoll.py

# Total number of votes cast
# A complete list of candidates who received votes
# Total number of votes each candidate received
# Percentage of votes each candidate won
# The winner of the election based on popular vote

# # Import the datetime class from the datetime module
# import datetime
# # Use the now() attribute on the datetime class to get the present time.
# now=datetime.datetime.now()
# # Print the present time.
# print("The time right now is ", now)

# # Assign a variable for the file to load and the path.
# file_to_load = 'Resources/election_results.csv'
# # Open the election results and read the file.
# election_data = open(file_to_load, 'r')
# # To do: perform analysis.
# # Close the file.
# election_data.close()

# #Assign a variable for the file to load and the path.
# file_to_load = 'Resources/election_results.csv'
# # Open the election results and read the file
# with open(file_to_load) as election_data:
#      # To do: perform analysis.
#      print(election_data)

# import csv
# import os
# # Assign a variable for the file to load and the path.
# file_to_load = os.path.join("Resources", "election_results.csv")
# # Open the election results and read the file.
# with open(file_to_load) as election_data:
#     # Print the file object.
#      print(election_data)

# import csv
# import os
# # Assign a variable for the file to load and the path.
# file_to_save = os.path.join("analysis", "election_analysis.txt")
# # Open the election results and read the file.
# with open(file_to_save, "w") as election_analysis0:
#      print(election_analysis0)

# import csv
# import os
# # Assign a variable for the file to load and the path.
# file_to_save = os.path.join("analysis", "election_analysis.txt")
# # Open the election results and read the file.
# open(file_to_save, "w")

# import datetime
# date=datetime.datetime.now()
# print(date)

# import csv
# import os 
# filename = os.path.join("resources","momo.txt")
# with open(filename,"x") as momoa:
#     print(momoa)

# import csv	
# import os	
# file_to_savee = os.path.join("Resources","election_analysiss.txt")	
# with open(file_to_savee,"w") as election_analysis1:	
#     print(election_analysis1)	

# import csv
# import os
# fileopen=os.path.join("Analysis","election_analysis.txt")
# x=open(fileopen,"w")
# x.write("Hello")
# x.close()

# import csv
# import os
# # Create a filename variable to a direct or indirect path to the file.
# file_to_save = os.path.join("Analysis", "election_analysis.txt")
# # Using the with statement open the file as a text file.
# outfile = open(file_to_save, "w")
# # Write some data to the file.
# outfile.write("Hello World")
# # Close the file
# outfile.close()

# import csv
# import os
# # Create a filename variable to a direct or indirect path to the file.
# file_to_save = os.path.join("analysis", "election_analysis.txt")
# # Using the with statement open the file as a text file.
# with open(file_to_save, "w") as txt_file:
#     # Write some data to the file.
#     txt_file.write("Counties in the election\n---------\nArapahoe\nDenver\nJefferson")

# import csv
# import os
# file_to_load = os.path.join("election_results.csv")
# file_to_save = os.path.join("analysis","election_analysis.txt")
# with open(file_to_load) as election_data:
#     file_reader = csv.reader(election_data)
#     for row in file_reader:
#         print(row)

# # Add our dependencies.
# import csv
# import os
# # Assign a variable to load a file from a path.
# file_to_load = os.path.join("Resources", "election_results.csv")
# # Assign a variable to save the file to a path.
# file_to_save = os.path.join("analysis", "election_analysis.txt")

# # Open the election results and read the file.
# with open(file_to_load) as election_data:
#     file_reader = csv.reader(election_data)

#     # Read and print the header row.
#     headers = next(file_reader)
#     print(headers)

# # Add our dependencies.
# import csv
# import os
# # Assign a variable to load a file from a path.
# file_to_load = os.path.join("election_results.csv")
# # Assign a variable to save the file to a path.
# file_to_save = os.path.join("analysis", "election_analysis.txt")
# # Open the election results and read the file.
# with open(file_to_load) as election_data:
#     file_reader = csv.reader(election_data)
#     # Read and print the header row.
#     headers = next(file_reader)
#     print(headers)

# import csv 
# import os 
# fileopen=os.path.join("election_results.csv")
# filesave=os.path.join("analysis", "election_analysis.txt")
# voters=0
# with open(fileopen) as election_analysis:
#     fileread=csv.reader(election_analysis)
#     header=next(fileread)
#     for row in fileread:
#         voters = voters +1    # Or voters += 1 
# print(voters)
        
# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Initialize a total vote counter.
total_votes = 0
# Candidate Options
candidate_options = []
# Open the election results and read the file.  
candidate_votes={}
# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    # Read the header row.
    headers = next(file_reader)
    # Print each row in the CSV file.
    for row in file_reader:
        # Add to the total vote count.
        total_votes += 1
        # Print the candidate name from each row.
        candidate_name = row[2]
        # If the candidate does not match any existing candidate...   
        if candidate_name not in candidate_options:
            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)
           # Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0
        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1
# Determine the percentage of votes for each candidate by looping through the counts.
# Iterate through the candidate list.
for candidate_name in candidate_votes:
    # Retrieve vote count of a candidate.
    votes = candidate_votes[candidate_name]
    # Calculate the percentage of votes.
    vote_percentage = float(votes) / float(total_votes) * 100

    #  To do: print out each candidate's name, vote count, and percentage of
    # votes to the terminal.

    # Determine winning vote count and candidate
    # Determine if the votes is greater than the winning count.
    if (votes > winning_count) and (vote_percentage > winning_percentage):
         # If true then set winning_count = votes and winning_percent =
         # vote_percentage.
         winning_count = votes
         winning_percentage = vote_percentage
         # And, set the winning_candidate equal to the candidate's name.
         winning_candidate = candidate_name
    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
print(winning_candidate_summary)
