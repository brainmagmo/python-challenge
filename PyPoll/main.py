#os to interact with system, csv because we can't use pandas yet
import os
import csv

# takes a list, lst, and an item that might be in the list, item, 
# returns the index of the item in the list
# returns -1 if the item is not in the list
# O(2n)
def fuzzy_index(lst, item):
    if lst.count(item) == 0:
        return -1
    else:
        return lst.index(item)

# You will be give a set of poll data called [election_data.csv](PyPoll/Resources/election_data.csv). 
data_path = os.path.join('Resources', 'election_data.csv')
#  The dataset is composed of three columns: `Voter ID`, `County`, and `Candidate`. 

#  Your task is to create a Python script that analyzes the votes and calculates each of the following:
#
#  * The total number of votes cast
total_v = 0
#  * A complete list of candidates who received votes
# candidates
candid_s = []
#  * The percentage of votes each candidate won
#  vbc/total
#  * The total number of votes each candidate won
#v otes by candidate
votes_bc = []
#  * The winner of the election based on popular vote.
winner = ''

#Read the poll data
data_path = os.path.join('Resources', 'election_data.csv')
with open(data_path) as data_file:
    data_reader = csv.reader(data_file, delimiter=',')
    data_header = next(data_reader)
    #print(data_header)
    for row in data_reader:
        #note that a vote is cast
        total_v += 1
        
        #grab who was voted for
        cand = row[2]
        #see if we have listed them as a candidate
        cindex = fuzzy_index(candid_s,cand)
        #if not, add them to the candidate list and note that someone voted for them
        if cindex == -1:
            candid_s.append(cand)
            votes_bc.append(1)
        #if so, count their vote
        else:
            votes_bc[cindex] += 1
    #find the winner        
    winner = candid_s[
        votes_bc.index(max(votes_bc))
    ]

#* In addition, your final script should both print the analysis to the terminal and export a text file with the results.
#* As an example, your analysis should look similar to the one below:
#
#  ```text
lines = [ "Election Results",
         "-------------------------",
         "Total Votes: " + str(total_v),
         "-------------------------"
]

#  Election Results
#  -------------------------
#  Total Votes: 3521001
#  -------------------------
#for each candidate in the candidate list
for cd in candid_s:
    #lookup how many votes they got
    cd_v = votes_bc[candid_s.index(cd)]
    #calcuate their win%
    cd_p = round(100*(cd_v/total_v),3)
    #write their results
    lines.append(f'{cd}: {cd_p}% ({cd_v})')
#  Khan: 63.000% (2218231)
#  Correy: 20.000% (704200)
#  Li: 14.000% (492940)
#  O'Tooley: 3.000% (105630)
lines.append('-------------------------')
#  -------------------------

lines.append(f'Winner: {winner}')
#  Winner: Khan

lines.append('-------------------------')
#  -------------------------
#  ```
analysis_path = os.path.join("analysis", "poll_analysis.txt")
with open(analysis_path, 'w') as ap:
    apw = csv.writer(ap)
    for l in lines:
        print(l)
        apw.writerow([l])

#abra cadabra!