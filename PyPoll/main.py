# import os module to work on any operating system
import os
#import csv module to read the csv file
import csv

#set the working directory to where the main file is:
os.chdir (os.path.dirname (__file__))
#locate the Resources file
pypoll_csv = os.path.join ("Resources", "election_data.csv")

total_number_vote = 0
candidate_votes = {} # create dictionary object to hold candidate names as keys + number of votes for each candidate


#open the file to read
with open (pypoll_csv) as pypoll:
    # create csv reader to iterate through csv file
    election_data = csv.reader(pypoll, delimiter=',')
   
    # skip first row because that's headers row
    next(election_data)
   
    # loop through election data rows to count votes
    for row in election_data:
        # add 1 vote to total number of votes
        total_number_vote += 1
       
        candidate_name = row[2]
        # if we have not seen candidate name before, then add their name to candidate_votes dictionary and increment their vote count
        if candidate_name not in candidate_votes.keys():
            # new candidate got 1 vote
            candidate_votes[candidate_name] = 1
        else:
            # if candidate already exists in dictionary, add 1 to vote number
            candidate_votes[candidate_name] += 1
       
# determine winner by finding key value with highest number in dictionary
winner = max(candidate_votes, key=candidate_votes.get)

# print outputs
print("Election Results")
print("------------------------")
print("Total votes: {total_votes}".format(total_votes=total_number_vote))
print("------------------------")
# loop through dictionary to print candidate results
for key in candidate_votes.keys():
    variable1 = key
    variable2 = "%.3f%% (%d)"
    variable3 = (candidate_votes[key]/total_number_vote*100)
    variable4 = candidate_votes[key]
   # ((key + ": %.3f%% (%d)") % ((candidate_votes[key]/total_number_vote*100), candidate_votes[key]))
    # %.3f so that percentage is 3 decimal places
    # %d to print integer (number of votes for each candidate)
variable= (variable1, variable2 +"%", variable3, variable4)
print (variable)
print("------------------------")
print("Winner: " + winner)
print("------------------------")

#export output as txt file:
output_file = os.path.join ("analysis","outcome.txt")

#open the output file
with open (output_file, "w") as datafile:

     #print out the output
    data = (
        f"Election Results \n"
        f"-------------------------------------\n"
        f"Total votes: {str(total_number_vote)}\n"
        f"-------------------------------------\n"
        f"{str(variable)}\n"
        f"-------------------------------------\n"
        f"Winner: {winner}\n"
        f"-------------------------------------\n"
        
        )
    datafile.write(data)