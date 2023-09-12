import os
import csv
import pandas as pd 
#import numpy as np

month_col = []
pl_total_col = []
change_in_pl = []
period_one = []
period_two = []
greatest_inc = []
count = 0

df = pd.read_csv("C:/Users/jwoot/Documents/GWU-VIRT-DATA-PT-08-2023-U-LOLC/python-challenge/PyBank/resources/budget_data.csv")
with open("C:/Users/jwoot/Documents/GWU-VIRT-DATA-PT-08-2023-U-LOLC/python-challenge/PyBank/resources/budget_data.csv") as csvfile:
    csvreader = csv.reader(csvfile,delimiter = ',')
    #skip header
    csv_header = next(csvfile)
    for row in csvreader:
        
        

        #tally months
        month_col.append(row[0])
        total_months = len(str(month_col))

        #sum all profits and losses
         
        pl_total_col.append(int(row[1]))
        

        
        
for col in pl_total_col:
    count += 1
    if count % 2 == 1: 
        period_one.append(col)  
    elif count % 2 == 0:
        period_two.append(col)  
            #change in profit and loss
for col in range(len(period_one)):
    change_in_pl.append(period_two[col]- period_one[col])
        
pl_total = sum(i for i in pl_total_col)
pl_average = round(sum(change_in_pl)/len(change_in_pl),2)

#greatest increase and decrease
greatest_inc = df.loc[df['Profit/Losses'] == df['Profit/Losses'].max()]
greatest_dec = df[df['Profit/Losses'] == df['Profit/Losses'].min()]





total_month_row = f'Total Months: {total_months}' + "\n"
pl_total_row = f'Total: {pl_total}' + "\n"
average_change_row = f'Average Change: {pl_average}' + "\n"      
greatest_increase_row = f'Geatest Increase: {greatest_inc}'  + "\n"
greatest_decrease_row = f'Greatest Decrease: {greatest_dec}' + "\n"

#content_total_months = str(total_months)
#content_pl_total = str(pl_total)
#content_pl_average = str(pl_average)
#content_greatest_inc = str(greatest_inc)
#content_greatest_dec = str(greatest_dec)

with open("pybank.txt","w",encoding = 'UTF-8') as txtfile:
    txtfile.write('Financial Analysis' + "\n")
    txtfile.write('------------------------------' + "\n")
    txtfile.write(total_month_row)
    txtfile.write(pl_total_row)
    txtfile.write(average_change_row)
    txtfile.write(greatest_increase_row)
    txtfile.write(greatest_decrease_row)

