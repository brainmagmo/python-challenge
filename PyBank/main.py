#!/usr/bin/env python
# coding: utf-8
#Trevor kleinstuber, 2020/06/17

#os to interact with system, csv because we can't use pandas yet
import os
import csv
#in this folder, the path to the data is Resources/budget_data.csv
data_path = os.path.join('Resources', 'budget_data.csv')

#decalring variables for info wee want to track
count = 0
running_total = 0
months = []
max_increase = 0
pos_mon = ''
max_decrease = 0
neg_mon = ''
change = 0

#with closes autmaticatlly
with open(data_path) as data_file:

    # open iterator list as data-reader
    data_reader = csv.reader(data_file, delimiter=',')

    # skim the head
    data_header = next(data_reader)
    #print(f"CSV Header: {data_header}")

    for row in data_reader:
        #The total number of months included in the dataset

        count += 1

        if months.count(row[0]) == 0:
            months.append(row[0])
            
        change = int(row[1])
        #The net total amount of "Profit/Losses" over the entire period
        running_total += change
        
        #The greatest increase in profits (date and amount) over the entire period
        if change > max_increase:
            max_increase = change
            pos_mon = row[0]
        
        #The greatest decrease in losses (date and amount) over the entire period
        if change < max_decrease:
            max_decrease = change
            neg_mon = row[0]

avg = int((running_total/count)*100)/100

#In addition, your final script should both print the analysis to the terminal and export a text file with the results.
#  Financial Analysis
print("Financial Analysis")
#  ----------------------------
print("----------------------------")
#  Total Months: 86
print("Total Months: " + str(len(months)))
#  Total: $38382578
print("Total: $" + str(running_total))
#  Average  Change: $-2315.12
print("Average Change: $" + str(avg))
#  Greatest Increase in Profits: Feb-2012 ($1926159)
print("Greatest Increase in Profits: " + pos_mon + " ($" + str(max_increase) + ")")
#  Greatest Decrease in Profits: Sep-2013 ($-2196167)
print("Greatest Decrease in Profits: " + neg_mon + " ($" + str(max_decrease) + ")")

##The total number of months included in the dataset
#print(len(months))
#print(str(count))
#  #The net total amount of "Profit/Losses" over the entire period
#print(str(running_total))
  ##The average of the changes in "Profit/Losses" over the entire period

#print(str(avg))
  ##The greatest increase in profits (date and amount) over the entire period
#print(max_increase)
 # #The greatest decrease in losses (date and amount) over the entire period
#print(max_decrease)
    
#if len(months) != count:
#    print("Duplicate month data in source code")

