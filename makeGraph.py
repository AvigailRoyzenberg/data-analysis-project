#!/usr/bin/env python3

import matplotlib
import matplotlib.pyplot as plt
import numpy as np

f = plt.figure()  # create an instance for a pdf to be saved

finfem = open("women_meansEdit.txt")
finmale = open("men_meansEdit.txt")

womenList = []
maleList = []

femCount = 0
for line in finfem:
    if femCount != 18:
        columns = line.split("\n")  # there's a new line that we want o get rid of
        womenList.append(columns[0]) # append all of the fem  means to a list
        femCount += 1   # stop when you get to the 17th one

maleCount = 0
for line in finmale:
    if maleCount != 18:
        columns = line.split("\n") # there's a new line that we want o get rid of
        maleList.append(columns[0])  # append all of the male means to a list
        maleCount += 1  # stop when you get to the 17th one
    
women_means = [int(value) for value in womenList] # the womens list
men_means = [int(value) for value in maleList]    # the males list
labels = []                                       # the labels
for i in range(18):
    labels.append(i)

#_____________________ copied from matplotlib: "grouped bar chart with labels"

x = np.arange(len(labels))  # the label locations
width = 0.35  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, men_means, width, label='Men')
rects2 = ax.bar(x + width/2, women_means, width, label='Women')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Number of Doctors')
ax.set_title("Number of Docters per Community's Annual Income (in the 10 thousands) ")
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()


def autolabel(rects):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height = rect.get_height()
        #ax.annotate('{}'.format(height),
         #           xy=(rect.get_x() + rect.get_width() / 2, height),
          #          xytext=(0, 3),  # 3 points vertical offset
           #         textcoords="offset points",
            #        ha='center', va='bottom')

autolabel(rects1)
autolabel(rects2)

fig.tight_layout()

#plt.show()  IF THE PLOT DOESN'T DISPLAY UNCOMMENT THIS

# ___________ copied from matplotlib

# save the plot into a PDF file
f.savefig("docBarGraph.pdf")

finmale.close()
finfem.close()

