import csv, os


with open('Homework_03-Python_Instructions_PyPoll_Resources_election_data.csv') as csvfile:
    read_csv=csv.reader(csvfile, delimiter=',')
    
    
    next(read_csv)
    total_votes=[]
    Khan_votes=[]
    Correy_votes=[]
    Li_votes=[]
    OTooley_votes=[]

    for row in read_csv:
        total_votes.append(row[0])
        
        if row[2]=="Khan":
            Khan_votes.append(row[2])
        elif row[2]=="Correy":
            Correy_votes.append(row[2])
        elif row[2]=="Li":
            Li_votes.append(row[2])
        elif row[2]=="O'Tooley":
            OTooley_votes.append(row[2])

total=len(total_votes)
a=len(total_votes)

max_list=[['khan',len(Khan_votes)], ['Correy',len(Correy_votes)],['Li',len(Li_votes)],['OTooley',len(OTooley_votes)]]


print("Election Results")
print("-------------------------")
print"Total Votes:",(total)
print("-------------------------")
print "Khan", 100*len(Khan_votes)/a,"%(",(len(Khan_votes)),")"

print "Correy", (100*len(Khan_votes)/a),"%(",(len(Correy_votes)),")"

print "Li", 100*len(Li_votes)/a,"%(", len(Li_votes),")"

print "O'Tooley", 100*len(OTooley_votes)/a,"%(", len(OTooley_votes), ")"


print("-------------------------")
print"Winner", max(max_list,key=lambda x: x[1])

print("-------------------------")
