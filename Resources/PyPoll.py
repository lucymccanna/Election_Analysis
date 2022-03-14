# psuedocode
#1. The total number of votes cast
#2. A complete list of candidates who received votes
#3. The percentage of votes each candidate won
#4. The total number of votes each candidate won
#5. The winner of the election based on popular vote

#Add our dependencies
import csv
import os

# Assign a variable for the file to load and the path
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path
file_to_save = os.path.join("analysis", "election_analysis.txt")

# 1. create and initialize the total votes variable to zero
total_votes = 0    

# 2.1 declare new list for Candidate names
candidate_options = []

# 4.1 create a dictionary for votes per candidate
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0


# Open the election results and read the file
with open(file_to_load) as election_data:
    
    #to do: read and analyze the data here
        #read the file object with the reader function
    file_reader = csv.reader(election_data)
   
    # Read and print the header row
    headers = next(file_reader)
          
    # Print each row in the CSV file
    for row in file_reader:
        #print(row)

        # 1.2. Add to the total vote count
        total_votes += 1


    #2.2 Print the candidate name from each row
        candidate_name = row[2]
    #2.3 Add the candidatename to the candidate options list using append if not existing in list
        if candidate_name not in candidate_options:
            #Add it to the list of candidates
            candidate_options.append(candidate_name)

            #4.2 Begin tracking that candidate's vote count
            candidate_votes[candidate_name]= 0

    # 4.3 Add a vote to that candidate
        candidate_votes[candidate_name] += 1        

file_to_save = os.path.join("analysis", "election_analysis.txt")
#Save the resultst to our text file
with open(file_to_save, "w") as txt_file:
# Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    # Save the final vote count to the text file.
    txt_file.write(election_results)    

# 1.3. Print the total votes
    #print(total_votes)

#4.4 print candidates votes
#print(candidate_votes)

#2.4 Add a print statement for candidate names
#print(candidate_options)

    # 3 - Determine the percentage of votes for each candidate by looping through the counts
    #1 Iterate through the candidate list
    for candidate_name in candidate_votes:
            #2 retreive vote count of a candidate
        votes = candidate_votes[candidate_name]
            #3 calculate percentage of votes
        vote_percentage = float(votes) / float(total_votes) * 100
            #4 print the candidate name and percentage of votes
        # print(f"{candidate_name}: received {vote_percentage:.1f} % of the vote")

        # print out each candidate's name, vote count, and percentage of votes to the terminal
        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        print(candidate_results)

        #Save the candidate results to our text file
        txt_file.write(candidate_results)

        if (votes > winning_count) and (vote_percentage > winning_percentage):
            #2 If True, then set winning_count = votes and winning_percent = vote_percentage
            winning_count = votes
            winning_percentage = vote_percentage
            #3 set the winning candidate equal to the candidate's name
            winning_candidate = candidate_name

    winning_candidate_summary = (
        f"----------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}\n"
        f"----------------------\n")
    print(winning_candidate_summary)

    #save the winning candidate's name to the text file
    txt_file.write(winning_candidate_summary)











#WRITING PRACTICE in a text file
# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

#Use the open statement to open the file as a text file.
#with open(file_to_save, "w") as outfile:
    #Write some data to the file
    #outfile.write("Counties in the Election \n ------------------------\n")
    #outfile.write("\nArapahone\nDenver\nJefferson")


#close the file
txt_file.close()

