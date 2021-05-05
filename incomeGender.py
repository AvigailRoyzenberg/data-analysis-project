#!/usr/bin/env python3

import gzip

genderCountFile = open("zipgendercount.txt")
zipIncomeFile = gzip.open("IncomePop.gz", "rt")
foutwomen = open("women_meansEdit.txt", "w")
foutmale = open("men_meansEdit.txt", "w")

zipIncome = {}

femCount = {}
maleCount = {}

womenTot = {}
menTot = {}

# read the zip annd average income file:
for line in zipIncomeFile:
    columns = line.split("|")          # take just the:
    zipIncome[columns[0]] = columns[1] # zip: average income, into a dictionary
for line in genderCountFile:
    columns = line.split("|")          # put the number of females into a dictionary with the zip code as the key
    femCount[columns[0]] = columns[2]  # zipcode : femcount
    maleCount[columns[0]] = columns[1] # same for males

for zip in maleCount:                  # for the malezips
    if zip in zipIncome:               # if that zip code is in the list of zipIncome dic
        bin = int(int(zipIncome[zip])/10000) # create a bin- rounding incomes to the nearest bin, 
        if bin in womenTot:                  # create a women total and male total per bin of the # of docs in each
            womenTot[bin] += int(femCount[zip])  # add it in the bin if we saw it already
            menTot[bin] += int(maleCount[zip])
        else:
            womenTot[bin] = int(femCount[zip])  # if it hasn't been seen yet, create it
            menTot[bin] = int(maleCount[zip])

# now we need to sort the dic by key which is the bins by making it into a list
womenAns = []
for key in sorted(womenTot.keys()):
    womenAns.append("%s: %s" % (key, womenTot[key]))

#print("the double eidted womens ans is ")
for key in womenAns:
    columns = key.split(': ')
    values = columns[1]
   # print(values)
    foutwomen.write(values + "\n") # write the sorted dic which is a list to a file
                                   # that will be the womens means for the graph

#print("sorted men dic into a list is ")

maleAns = [] # making the male dic into a sorted list too
for key in sorted(menTot.keys()):
    maleAns.append("%s: %s" % (key, menTot[key]))
#print(maleAns) # the dic sorted into a list,

for key in maleAns:
    columns = key.split(': ')
    values = columns[1]
    #print(values)
    foutmale.write(values + "\n") # same with the males, the means for the graph

genderCountFile.close()
zipIncomeFile.close()
foutwomen.close()
foutmale.close()
