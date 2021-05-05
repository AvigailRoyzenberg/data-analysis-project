#!/usr/bin/env python3

from collections import Counter

fin = open("genderzipfinal.txt")
fout = open("zipgendercount.txt", "w")

femZips = {}
maleZips = {}


# for each line: tally key(zip codes) and data(M or F)
for line in fin:
    columns = line.split("|")
    gender = columns[1].strip() # because there was a \n attached to "M"
    key = columns[0]
    # making the maleTally:
    if "M" in columns[1]:   # if it's male
        if key in maleZips: # if it's already in the dic, add to the count
            maleZips[key] += 1
        else:
            maleZips[key] = 1   # if not, create it
    elif "F" in columns[1]:    # same thing
        if key in femZips:
            femZips[key] += 1
        else:
            femZips[key] = 1

for zip in maleZips:  # we want to write to a file
    if zip in femZips: # the zip code | how many male docs | how many fems
        # if it is is both:
        fout.write(zip + "|" + str(maleZips[zip]) + "|" + str(femZips[zip]) + "\n")
    else: # if the male zip isn't in the female:
        fout.write(zip + "|" + str(maleZips[zip])+ "|" + "0" + "\n")
for zip in femZips:
    if zip not in maleZips:  # if a fem zip code isn't in a male zip
        fout.write(zip + "|" + "0"+ "|" + str(femZips[zip]) + "\n")
        

fin.close()
fout.close()

        
    
