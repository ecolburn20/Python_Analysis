import os
import csv

#csvpath = "C:\\Users\\Owner\\Desktop\\Homework\\python-challenge\\PyPoll\\election_data.csv"
csvpath = os.path.join("..", "PyPoll", "election_data.csv")
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    voter_id = []
    canidate_list = []
    khan = 0
    correy = 0
    li = 0
    otooley = 0
# total number of voters
    for x in csvreader:
        voter_id.append(x[0])
        canidate_list.append(x[2])
    num_votes = len(voter_id)
    
# votes per canidate
    for y in canidate_list:
        if y == "Khan":
            khan += 1
        elif y == "Correy":
            correy += 1
        elif y == "Li":
            li += 1   
        elif y == "O'Tooley":
            otooley += 1 
# winner
    votes_dict = {khan:"khan",correy:"correy",li:"li",otooley:"otooley"}
    voter_list = [khan, correy, li, otooley]
    winner_pos = max(voter_list)
    winner = votes_dict[winner_pos]

# percent of total votes
    khan_percent = "{0:.3f}%".format(khan/num_votes*100)
    correy_percent = "{0:.3f}%".format(correy/num_votes*100)
    li_percent = "{0:.3f}%".format(li/num_votes*100)
    otooley_percent = "{0:.3f}%".format(otooley/num_votes*100)
    

# printing outputs
print("Election Results")
print("-----------------------")
print("Total Votes: " + str(num_votes))
print("-----------------------")
print(f'Khan: {khan_percent} ({khan})')
print(f'Correy: {correy_percent} ({correy})')
print(f'Li: {li_percent} ({li})')
print(f'O Tooley: {otooley_percent} ({otooley})')
print("-----------------------")
print(f'Winner: {winner.title()}')
print("-----------------------")