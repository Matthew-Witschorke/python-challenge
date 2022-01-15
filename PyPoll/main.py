import csv

csvpath = "Resources/election_data.csv"

#Declaring Needed Variables
totalVotes = 0
voteKhan = 0
voteCorrey = 0
voteLi = 0
voteOTooley = 0

with open(csvpath, "r") as file:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(file, delimiter=',')
    csvheader = next(csvreader)
    
    for row in csvreader:
        totalVotes = totalVotes + 1
        if row[2] == "Khan":
            voteKhan = voteKhan + 1
        elif row[2] == "Correy":
            voteCorrey = voteCorrey + 1
        elif row[2] == "Li":
            voteLi = voteLi + 1
        elif row[2] == "O'Tooley":
            voteOTooley = voteOTooley + 1

precentageKhan = "{:.3%}".format(voteKhan / totalVotes)
precentageCorrey = "{:.3%}".format(voteCorrey / totalVotes)
precentageLi = "{:.3%}".format(voteLi / totalVotes)
precentageOTooley = "{:.3%}".format(voteOTooley / totalVotes)

winner = max(voteKhan, voteCorrey, voteLi, voteOTooley)
if winner == voteKhan:
    winner_name = "Khan"
elif winner == voteCorrey:
    winner_name = "Correy"
elif winner == voteLi:
    winner_name = "Li"
elif winner == voteOTooley:
    winner_name = "O'Tooley"

results = f"""Election Results
-------------------------
Total Votes: {totalVotes}
-------------------------
Khan: {precentageKhan} {voteKhan}
Correy: {precentageCorrey} {voteCorrey}
Li: {precentageLi} {voteLi}
O'Tooley: {precentageOTooley} {voteOTooley}
-------------------------
Winner: Khan
-------------------------
"""
print(results)


with open("analysis/Election_Results.txt", "w") as text:
    text.write(results)
