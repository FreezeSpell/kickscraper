###A script that runs main.py and sorts the outputs according to given settings.

###Settings
###WARNING: ONLY HAVE ONE SETTING ENABLED AT A TIME!
percentualSort = False #If True, the script will sort the outputs according to the percentage of the goal funded.
totalFundSort = False #If True, the script will sort the outputs according to the total amount of money funded.
totalRequestSort = False #If True, the script will sort the outputs according to the total amount of money requested.

###Checks whether more than one setting is enabled.
if percentualSort + totalFundSort + totalRequestSort > 1:
    print("Only one setting can be enabled at a time!")
    exit()

###Imports
from main import dataSet
import os

if percentualSort == True: ##NOT WORKING
    for i in dataSet:
        percent = int(i[2]) / int(i[3]) * 100
    dataSet.sort(key=percent)

if totalFundSort == True: ##NOT WORKING
    for i in dataSet:
        total = i[-2]
    dataSet.sort(key=total)


####Writes the sorted outputs to a file.
fileNumber = max(os.listdir("Academics-Antics/Python/Outreaching CB/Scraper/sortedOutputs"))
fileNumber = int(fileNumber)
fileNumber += 1

outputLocation = (f"Academics-Antics/Python/Outreaching CB/Scraper/outputs/{fileNumber}")

file = open(outputLocation, "w")

for i in dataSet:
    file.writelines(str(i))
    file.write("\n")

print("Success!")