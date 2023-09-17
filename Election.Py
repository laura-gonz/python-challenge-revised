#libraries or dependencies 
import os
import csv 

#variable is being defined by inputted data from Excel 
Election_DataLoad = os.path.join ("Resources", "ElectionData.csv")
Election_Output = os.path.join ("Resources", "Election_Analysis.txt")


#whenever you're extracting data from your local computer you use os.path.join 

#initialize parameters 
Total_Votes = 0

Candidates_List = []
#intialized values

Candidates_Votes = {} 
#dictionary 

Percentage_Winners = 0 
Total_WinningVotes = 0 
Winner = ""


with open (Election_DataLoad) as data:
    reader = csv.reader(data)
    #header row 
    header = next(reader)

    for Row in reader:
        
        Total_Votes += 1
        #total number of votes 

        Candidate_Name = Row[2]
        #retrive values from column 2 from each row 
        if Candidate_Name not in Candidates_List: 
            Candidates_List.append(Candidate_Name)
        
            Candidates_Votes [Candidate_Name] = 0
            #initializing a count with 0
        Candidates_Votes [Candidate_Name] += 1
        

    print(Candidates_Votes)
    print(Candidates_List)

        
        
         
        
        #adds value to existing and assigns new value back to same variable 
            


    print(Total_Votes) 

    #print(list[0])
    #print(list(1))
    #print(list(2))

    
# output = f"""
# Election Results
# -------------------------
# Total Votes: 369711
# -------------------------
# Charles Casper Stockham: 23.049% (85213)
# Diana DeGette: 73.812% (272892)
# Raymon Anthony Doane: 3.139% (11606)
# -------------------------
# Winner: Diana DeGette
# """    

# print(output) 

# with open (Election_Output, "w") as fdata:
#     fdata.write(output)
    
    