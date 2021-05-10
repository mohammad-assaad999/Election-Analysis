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

# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read and print the header row.
    headers = next(file_reader)
    print(headers)