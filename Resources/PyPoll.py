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

# Open the election results and read the file
with open(file_to_load) as election_data:
    
    #to do: read and analyze the data here
        #read the file object with the reader function
    file_reader = csv.reader(election_data)
        #print each row in the CSV file
    #for row in file_reader:
      #  print(row)
    # Read and print the header row
    headers = next(file_reader)
    print(headers)








#WRITING PRACTICE in a text file
# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

#Use the open statement to open the file as a text file.
with open(file_to_save, "w") as outfile:
    #Write some data to the file
    outfile.write("Counties in the Election \n ------------------------\n")
    outfile.write("\nArapahone\nDenver\nJefferson")


#close the file
outfile.close()

