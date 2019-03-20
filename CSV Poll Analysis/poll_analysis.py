
import os
import csv
#variable instantiation
Total=0
KhanTotal=0
CorreyTotal=0
LiTotal=0
OTooleyTotal=0  
#csv path reader, home directory
csvpath = os.path.join("election_data.csv")
#text file writer, home directory
output_path = os.path.join("ElectionAnalysis.txt")

#Read file
with open(csvpath, "r") as csvfile:

    # delimeters
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    #Read through file, collect the votes for each
    for row in csvreader:
        Total=Total+1
        if row[2]=="Khan":
            KhanTotal=KhanTotal+1
        elif row[2]=="Correy":
            CorreyTotal=CorreyTotal+1
        elif row[2]=="Li":
            LiTotal=LiTotal+1
        elif row[2]=="O'Tooley":
            OTooleyTotal=OTooleyTotal+1

#Calculate the winner
if KhanTotal>CorreyTotal:
    if KhanTotal>LiTotal:
        if KhanTotal>OTooleyTotal:
            winner="Khan"
        else:
            winner="O'Tooley"
    else:
        if LiTotal>OTooleyTotal:
            winner="Li"
        else:
            winner="O'Tooley"
else:
    if CorreyTotal>LiTotal:
        if CorreyTotal>OTooleyTotal:
            winner="Correy"
        else:
            Winner="O'Tooley"
    else:
        if LiTotal>OTooleyTotal:
                winner="Li"
        else:
                winner="O'Tooley"

#Calculate the % of each candidate
KhanPercent= (KhanTotal * 100)/Total
CorreyPercent=(CorreyTotal * 100)/Total
LiPercent=(LiTotal* 100)/Total
OTooleyPercent=(OTooleyTotal * 100)/Total

#Results printed to terminal
print("Election Results")
print("-----------------------------")
print("Total Votes: " + str(Total))
print("-----------------------------")
print("Khan: " + str("%.4f" % KhanPercent) + "% (" + str(KhanTotal) + ")")
print("Correy: " + str("%.4f" %CorreyPercent) + "% (" + str(CorreyTotal) + ")")
print("Li: " + str("%.4f" %LiPercent) + "% (" + str(LiTotal) + ")")
print("O'Tooley: " + str("%.4f" %OTooleyPercent) + "% (" + str(OTooleyTotal) + ")")
print("-----------------------------")
print("Winner: " + winner)
print("-----------------------------")

#write the file
file=open(output_path, "w")

file.write("Election Results\n")
file.write("-----------------------------\n")
file.write("Total Votes: " + str(Total) + "\n")
file.write("-----------------------------\n")
file.write("Khan: " + str("%.4f" % KhanPercent) + " (" + str(KhanTotal) + ")\n")
file.write("Correy: " + str("%.4f" % CorreyPercent) + " (" + str(CorreyTotal) + ")\n")
file.write("Li: " + str("%.4f" % LiPercent) + " (" + str(LiTotal) + ")\n")
file.write("O'Tooley: " + str("%.4f" % OTooleyPercent) + " (" + str(OTooleyTotal) + ")\n")
file.write("-----------------------------\n")
file.write("Winner: " + winner + "\n")
file.write("-----------------------------\n")
