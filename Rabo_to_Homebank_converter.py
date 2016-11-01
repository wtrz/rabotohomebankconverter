#!/usr/bin/env python
#Python 3.5 script 20161101 V2
#Author: Wouter Dunnes
#Purpose: Convert Rabobank's  "transactions.txt" into Homebank csv format


import csv
import time

#variables
current_date = time.strftime("%Y%m%d")
ifilename = "transactions.txt" #input file name. 
ifile = open(ifilename,"rb")
ofilename = "transactions_" + current_date + ".csv" #output file name
ofile = open(ofilename,"w+")
reader = csv.reader(ifile,delimiter=",")
writer = csv.writer(ofile,delimiter=";")
count = 0 #counter for number of processed transactions
keyword1 = 'Betaalautomaat' #identifier for debitcard transactions. These will be categorized accordingly. 

#iterate over each row
for idx, row in enumerate(reader):
    #count iterations
    count += 1


    #required order: fulldate,category,empty,description,memo,signedamount,empty,importtext


    #Date
    date = row[2]
    year = date[2:4]
    month = date[4:6]
    day = date[6:8]
    fulldate = month + "-" + day + "-" + year 
    
    #Category - 6 = debitcard; 4 = transfer. 
    if keyword1 in row[11]:
        category = 6
    else:
        category = 4


    
    #empty
    #Description
    if row[6] == "":
        description = row[10]
    else:
        description = row[6]
    

    #memo
    memo = row[10] + " " + row[11]
    #signedamount
  
    if row[3] == "D":
        sign = "-"
    else:
        sign = ""

    amount = row[4]
    signedamount = sign + amount

    #empty
    #importtext
    importtext = "import" + current_date
        
    #plist is the list to be added to ofile
    plist = [fulldate,category,'',description,memo,signedamount,'',importtext]
    print(count,plist)
    writer.writerow(plist)
    
#close + summary
ifile.close()
ofile.close()

print("""
\n
Transactions proccessed: {}
Output file: {} """.format(count,ofilename))


