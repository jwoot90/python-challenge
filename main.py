import os
import csv
import pandas as pd



df = pd.read_csv("C:/Users/jwoot/Documents/GWU-VIRT-DATA-PT-08-2023-U-LOLC/python-challenge/PyPoll/resources/election_data.csv")

#tally otes
total_votes = df['Ballot ID'].count()
candidate_counts = df['Candidate'].value_counts()[['Charles Casper Stockham','Diana DeGette','Raymon Anthony Doane']]
winner = df['Candidate'].value_counts()[['Charles Casper Stockham','Diana DeGette','Raymon Anthony Doane']].max()


#Get candidate counts
charles_count = df['Candidate'].value_counts()[['Charles Casper Stockham']]
diana_count = df['Candidate'].value_counts()[['Diana DeGette']]
raymon_count = df['Candidate'].value_counts()[['Raymon Anthony Doane']]

#get candidate percentages
charles_percentage= round(df['Candidate'].value_counts()['Charles Casper Stockham']/total_votes,3) * 100 
diana_percentage = round(df['Candidate'].value_counts()['Diana DeGette']/total_votes,3) * 100
raymon_percentage = round(df['Candidate'].value_counts()['Raymon Anthony Doane']/total_votes,3) * 100 

#create variables for rows which will be passed to output file
total_row = f'Total Votes: {total_votes} ' + "\n"
diana_row = f'Diana DeGette: {diana_percentage}' + "%" +" " + f'{diana_count[0]}' + "\n"
charles_row = f'Charles Casper Stockham: {charles_percentage}' + "%" + " " + f'{charles_count[0]}'+ "\n"
raymon_row = f'Raymon Anthony Doane: {raymon_percentage}' + "%" + " " + f'{raymon_count[0]}'+ "\n"
winner_row = f'Winner:{winner}' 





#set up data for output file
with open("election_data.txt","w",encoding = 'UTF-8') as txtfile:
  txtfile.write("Election Results " + "\n")
  txtfile.write(total_row)
  txtfile.write(diana_row)
  txtfile.write(charles_row)
  txtfile.write(raymon_row)
  txtfile.write(winner_row)
  