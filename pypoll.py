import os
import csv



with open("C:/Users/jwoot/Documents/GWU-VIRT-DATA-PT-08-2023-U-LOLC/python-challenge/PyPoll/resources/election_data.csv") as myFile:
    csv_reader = csv.reader(myFile)
  
    charles_count = 0
    diana_count = 0
    raymon_count = 0
    for row in csv_reader:
        candidate = row[2]
        if candidate == "Charles Casper Stockham":
           charles_count += 1; 
        elif candidate == "Diana DeGette":
             diana_count += 1;
        elif candidate == "Raymon Anthony Doane":
             raymon_count +=1;
        else :
            print("This person is not a canidate")
total_votes = charles_count + diana_count + raymon_count
charles = (charles_count/total_votes)*100
charles_percentage = round(charles,2)
diana = (diana_count/total_votes)*100
diana_percentage = round(diana,2)
raymon = (raymon_count/total_votes)*100
raymon_percentage = round(raymon,2)
winner = max(charles_count,diana_count,raymon_count)
#create variables for rows which will be passed to output file
total_row = f'Total Votes: {total_votes} ' + "\n"
diana_row = f'Diana DeGette: {diana_percentage}' + "%" +" " + f'{diana_count}' + "\n"
charles_row = f'Charles Casper Stockham: {charles_percentage}' + "%" + " " + f'{charles_count}'+ "\n"
raymon_row = f'Raymon Anthony Doane: {raymon_percentage}' + "%" + " " + f'{raymon_count}'+ "\n"
winner_row = f'Diana is the winner with {winner} votes' +"\n"

print(winner)
#set up data for output file
with open("election_data.txt","w",encoding = 'UTF-8') as txtfile:
  txtfile.write("Election Results " + "\n")
  txtfile.write(total_row)
  txtfile.write(diana_row)
  txtfile.write(charles_row)
  txtfile.write(raymon_row)
  txtfile.write(winner_row)