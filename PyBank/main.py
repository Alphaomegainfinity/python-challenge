# import os module to work on any operating system
import os
#import csv module to read the csv file
import csv

#set the working directory to where the main file is:
os.chdir (os.path.dirname (__file__))

#locate the Resources file
pybank_csv = os.path.join ("Resources", "budget_data.csv")

total_month = 0
profit_losses = 0
total_change = 0
max_increase = 0
min_decrease = 0

#open the file to read
with open (pybank_csv) as pybank:
    csv_reader = csv.reader (pybank, delimiter= ",") 

    next(csv_reader) #to skip the first header row
    previous_row = None
    #start the loop to read the file
    for row in csv_reader:
        #calculate the number of months within the dataset
        total_month += 1

        #Calculate the net total amount of Profit/Losses over the entire period
        profit_losses = profit_losses + float(row[1])
        
        #Calculate the changes in each rows
        if previous_row != None:
            difference = ((float(row[1]))-float(previous_row[1]))
            total_change += (float(row[1]) - float(previous_row[1]))

        #Calculate the max increase and min decrease
            if difference >= max_increase:
               max_increase = round(difference)
               max_month = row[0] 
            
            if difference <= min_decrease:
                min_decrease = round(difference)
                min_month = row[0]

        previous_row = row

    #Calculate the average change
    average_change = round(total_change / (total_month-1),2)

    print ("Financial Analysis")
    print ("-----------------------------------")

    #print the total number of months  
    print (f"Total number of months is:  {str(total_month)}")
    print ("Net total amount of Profit & Losses over the entire period is: " + "$" + str(round(profit_losses)))
    
    #print the average change
    print ("The average_change is: $" + str(average_change))  

    #print the max increase in profits
    print ("The greatest increase in Profits is: {} (${}) ".format (max_month,max_increase))
   
    #print the greatest decrease in profits
    print ("The greatest decrease in Profits is: {} (${}) ".format (min_month,min_decrease))
   
    #export output as txt file:
    output_file = os.path.join ("analysis","outcome.txt")

    #open the output file
    with open (output_file, "w") as datafile:

        #print out the output
        data = (
        f"Financial Analysis \n"
        f"-------------------------------------\n"
        f"Total number of months is: {str(total_month)}\n"
        f"Net total amount of Profit & Losses over the entire period is: ${round(profit_losses)}\n"
        f"The greatest increase in Profits is: {max_month} (${max_increase})\n"
        f"The greatest decrease in Profits is: {min_month} (${min_decrease})\n"
        )
        datafile.write(data)

   