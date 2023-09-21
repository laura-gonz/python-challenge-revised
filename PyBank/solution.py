#import OS and csv
import os
import csv

#import csv file
csvpath = os.path.join('Resources', 'budget_data.csv')
print(csvpath)

#ouput to text 
text_path = "output.txt"

#print headers 
print("Financial Analysis")
print("----------------------")

#open the csv

#use an array, use list--build list ith loop first to get data into a dictionary, then put it into the loop. 
#create variables then use .append within for loop
#Month Variable: create list for months
months = []

#Profit/Loss Variable: create list for the profits and losses
profitloss = []

#Change Variable: create list for monthly change of profits and losses, set total to 0
change = []
total = 0

#Read actual CSV file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    #find total months
    #forloop
    for row in csvreader:
        months.append(row[0])
        profitloss.append(row[1])
        total += int(row[1])

#month to month profits and losses change value calculation loop
#subtract a month from months because the first row does not show change as stated before
    for nr in range(len(months)-1):
        change.append(int(profitloss[nr+1]) - int(profitloss[nr]))

    #greates increase and decrease with .index to locate the max and min value related to change
    GrInc = change.index(max(change))
    GrDec = change.index(min(change))

    #match months to greatest increase and decrease and give srtings a new variable
    DateMax = months[GrInc]
    DateMin = months[GrDec]

    #change value average and round result
    ChngAvg = round(int(sum(change))/(int(len(months))-1),2)

print("Financial Analysis")
print("---------------------------------")
print(f'Total Months: {len(months)}')
print(f'Total: ${total}')
print (f'Average Change: ${ChngAvg}')
print (f'Greatest Increase in Profits: {DateMax} $({max(change)})') 
print (f'Greatest Decrease in Profits: {DateMin} $({min (change)})')


outputpath = os.path.join('Resources', "Analysis.txt")
Analysis=open(outputpath, "w")
Analysis.write("Financial Analysis \n")
Analysis.write("---------------------------- \n")
Analysis.write(f'Total Months: {len(months)}\n')
Analysis.write(f'Total: ${total}\n')
Analysis.write(f'Average Change: ${ChngAvg}\n')
Analysis.write(f'Greatest Increase in Profits: {DateMax} $({max(change)})\n') 
Analysis.write(f'Greatest Decrease in Profits: {DateMin} $({min (change)})\n')

Analysis.close()