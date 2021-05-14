# Election-Analysis

## Overview of Election Audit
In this project, I've helped Seth and Tom to analyze and submit the election audit results to the Colorado Board of Elections. The analysis includes writing a script of codes that open a CSV file, read it, retrieve data, calculate these data using some functions, logical conditions, and expressions, and output the results on a text file to be presented to the board. A Colorado Board of Elections employee has given me the following tasks to complete the election audit of a recent local congressional election:

  1. Calculate the total number of votes cast.
  2. Get a complete list of candidates who received votes.
  3. Calculate the total number of votes each candidate received.
  4. Calculate the percentage of votes each candidate won.
  5. Determine the winner of the election based on populer vote.
  6. Determine the voter turnout for each county
  7. Calculate the percentage of votes from each county out of the total count
  8. Determine the county with the highest turnout

### All the resources that were used in the project are:
  - Data Source: election_results.csv
  - Software: Python and Visual Studio Code 

## Election-Audit Results
The analysis of the election showed that:
- There were 369,711 votes cast in the election.
- The candidates were:
  - Charles Casper Stockham
  - Diana DeGette
  - Raymon Anthony Doane
- The candidates results were: 
  - Charles Casper Stockham: 23.0% of the total votes (85,213)
  - Diana DeGette: 73.8% of the total votes (272,892)
  - Raymon Anthony Doane: 3.1% of the total votes (11,606)
- The counties were:
  - Jefferson
  - Denver
  - Arapahoe
- The counties results were:
  - Jefferson: 10.5% (38,855)
  - Denver: 82.8% (306,055)
  - Arapahoe: 6.7% (24,801)
  - The largest county turnout was Denver
- The winner of the election was Diana DeGette who received 73.8% of the total votes 272,892 number of votes

The following two images show the election results on Git Bash and in the output text file, respectively:

![image](https://user-images.githubusercontent.com/80184581/118222660-03da0280-b44e-11eb-8454-83676c4a15c9.png)

![image](https://user-images.githubusercontent.com/80184581/118225061-5a494000-b452-11eb-9079-4f035c23e54a.png)

## Election-Audit Summary
This script was made in a way that anyone can use it to analyze other election processes for the following reasons:
- This script starts from scartch and ends with the final code before we get the results. In other words, all the formulas, functions, and expressions, are starting from zero or empty quotation marks and end with a well formed and organized expression to give the developer what he/she is asking for, so nothing else is missing in our script to finish the analysis. For example, we have started with total_votes = 0 and built many conditions and loops in our script in order to calculate the total votes in the election.
- In addition, the only one source of this script is the CSV file that includes a very large data of the number of total votes adn names of counties and candidates. That's why it's very easy to get a very similar file which has the same number, titles, and order of columns for another election because we are only using the number of rows and the headers order of the votes. For instance, we wrote candidate_name = row[2] which assumes that the candidate names are in the third column and needs to be retrieved and analyzed from the election results CSV file.

In brief, this script can be easily used and modified by other developers or analysts in order to analyze elections data. In this case, we can say that the main two things that should be done by the new user before he/she starts the analysis are to edit the data file to match the number, the order, and the header of the file columns and to edit the output file and the data file sources in the script to create the path from the data file to your script than to the output file (Text file). 
